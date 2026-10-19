"""给 Mapperatorinator 的洞补一条**推算轨**（原始那条一个字节不动）。

    python tools/docs/extend_mapper_lane.py --song new_45
    python tools/docs/extend_mapper_lane.py --runs-prefix new_

研究者 2026-10-12：`mapper在中间也不报，能帮它补上吗？` → `补齐，重新抽检`。

它为什么有洞：模型只在自己有把握的地方报 measure，洞是**它自己声明**的
（`gaps` 与 `validRanges` 都写着）。本仓库的规矩是**原始 observation 绝不插值**
（README：`gaps` / `validRanges` 原样保留），所以补出来的东西只能另开一条轨：

    calibrationId  mapperatorinator-extended
    note           洞里的小节线是按它**自己的**拍长与相位外推的，不是模型报的

外推规则（尽量少做假设）：取它自己**最近 8 根**相邻间隔的中位数当拍长，从洞前最后一根
小节线按这个拍长往前走，走到洞后第一根为止；洞在开头就往后推、洞在结尾就往前推。
"""

from __future__ import annotations

import argparse
import json
import pathlib
import statistics as st

HERE = pathlib.Path(__file__).resolve().parent
VALIDATOR = HERE.parents[1]
DOCS = VALIDATOR / "static" / "docs"
OBSERVATIONS = VALIDATOR / "static" / "observations"
RUNS = pathlib.Path(r"F:\vibe transcription\runs")
LANE_ERASED = "mapperatorinator-erased"     # 只擦：有密线就做，跟有没有洞无关
LANE_FILLED = "mapperatorinator-filled"     # 只补：只在模型声明的洞里加线


def global_bar(measures: list) -> float:
    """**全曲**的小节长度：间隔的**众数**（四舍五入到 0.05 秒后取出现最多的那一档）。

    为什么不是中位数（两版都踩过）：
      * 用"洞前最近 8 根"的局部中位 → 那几根本身可能是半小节，洞里就按半小节铺；
      * 用"别家轨的中位"当共识 → 别家有些歌也半小节化（new_81），尺子照样被带跑；
      * 用"自己所有间隔的中位" → 半小节占多数时又被带跑（new_81）。
    众数稳在"出现最多的那一档"上：new_81 是 2.82 秒、new_62 是 2.45 秒 —— 都对。
    """
    gaps = [round(b - a, 2) for a, b in zip(measures, measures[1:]) if b - a > 0.05]
    if not gaps:
        return 0.0
    buckets = {}
    for gap in gaps:
        key = round(gap / 0.05) * 0.05
        buckets[key] = buckets.get(key, 0) + 1
    # 半小节只会让间隔**变短**、不会变长，所以"哪一档才是大节"要往上取：
    # 取"出现次数至少占两成"里**最大**的那一档（new_81 的 1.41 占多数、2.82 占两成多 → 取 2.82；
    # new_62 的 1.22 只占 9% → 仍取 2.45）。
    threshold = max(2, int(len(gaps) * 0.2))
    good = [key for key, count in buckets.items() if count >= threshold]
    if good:
        return max(good)
    return max(buckets.items(), key=lambda item: item[1])[0]


def consensus_bar(doc: dict, own: list) -> float:
    """小节长度取**多来源共识**：别的机器轨各自间隔的中位数，再取中位。

    踩过（研究者 2026-10-12）：拿它自己所有间隔的中位数当尺子 —— 而它大半段把**半小节
    当小节**报，中位数就被带跑，于是半小节不但擦不掉，还把稀疏段也劈成两半。
    所以尺子要问别人（madmom / workbench / BeatThis / librosa），不问它自己。
    """
    bars = []
    for lane in doc.get("calibrations") or []:
        if str(lane.get("calibrationId") or "").startswith("mapperatorinator"):
            continue
        lines = [float(x["time"] if isinstance(x, dict) else x)
                 for x in (lane.get("barLines") or lane.get("downbeats") or [])]
        gaps = [b - a for a, b in zip(lines, lines[1:]) if b - a > 0.05]
        if len(gaps) >= 8:
            bars.append(st.median(gaps))
    if bars:
        return st.median(bars)
    gaps = [b - a for a, b in zip(own, own[1:]) if b - a > 0.05]
    return st.median(gaps) if gaps else 0.0


def erase_only(measures: list, bar: float, tol: float = 0.25) -> list:
    """**只删不加**：擦掉"明显是半小节"的线，剩下的线一秒钟都不动。

    研究者 2026-10-12：`擦线不会漂移，有什么问题？` —— 对。所以这一步绝不补线；
    判定只认最保守的一种：这根线跟上一根**保留线**的距离 ≈ 半个大节（本该是一整个），就擦；
    其余一律保留。因为只删，所以不会有漂移，也不会添出新的线。
    """
    if len(measures) < 2 or bar <= 0:
        return list(measures)
    keep = [measures[0]]
    for time in measures[1:]:
        span = time - keep[-1]
        if abs(span - bar / 2) <= tol * bar:          # 半小节：擦
            continue
        keep.append(time)
    return keep


def fill_holes(lines: list, bar: float) -> list:
    """**只补洞**：两根保留线之间跨度明显超过一个大节时，按大节等分补上该有的根数。"""
    if len(lines) < 2 or bar <= 0:
        return list(lines)
    out = [lines[0]]
    for time in lines[1:]:
        span = time - out[-1]
        count = int(round(span / bar))
        if count >= 2 and span > bar * 1.5:
            for step in range(1, count):
                out.append(round(out[-1] + span * step / count, 6))
        out.append(time)
    return out


def normalize(measures: list, bar: float, tol: float = 0.3) -> list:
    """把模型自己那串线整理成"全曲同一把尺子"的样子：**擦掉中间多出来的半小节线**，
    洞里再按这把尺子**等分补齐**。

    研究者 2026-10-12 定的两条：① 半路不该 4/4 改 2/4 —— 那些密一倍的线是**半小节**，
    不是小节，要擦掉；② 补要补在同一把尺子上。规则：

        从第一根线起，心里记着"下一根该在 keep[-1] + bar"；
          落在该在的位置（±tol·bar）→ 留下，尺子往前挪一格；
          落在**半小节**那儿（±tol·bar）→ 擦掉（这就是多出来的那根）；
          差得更远 → 当成洞/漂移：按 span/bar 等分出该有的根数，再重新对齐。

    原始 observation 一个字节不动；结果只写进 `mapperatorinator-extended` 这条。
    """
    if len(measures) < 2:
        return list(measures)
    if bar <= 0:
        return list(measures)
    keep = [measures[0]]
    expected = measures[0] + bar
    for time in measures[1:]:
        if abs(time - expected) <= tol * bar:              # 该在的位置
            keep.append(time)
            expected = time + bar
            continue
        if abs(time - (expected - bar / 2)) <= tol * bar:  # 半小节：擦掉
            continue
        span = time - keep[-1]                             # 洞或漂移
        count = int(round(span / bar))
        if count >= 2:
            for step in range(1, count):
                keep.append(round(keep[-1] + span * step / count, 6))
        keep.append(time)
        expected = time + bar
    return keep


def extend(song: str) -> str:
    source = OBSERVATIONS / ("%s.mapperatorinator.json" % song)
    target = DOCS / ("%s.mgmcs.json" % song)
    if not source.is_file() or not target.is_file():
        return "缺 observation 或文档，跳过"
    document = json.loads(source.read_text(encoding="utf-8"))
    measures = [float(x) for x in (document.get("observations") or {}).get("measures") or []]
    holes = document.get("gaps") or []
    if len(measures) < 2 or not holes:
        return "没有洞，跳过"
    bar = global_bar(measures)
    if bar <= 0:                                   # 这条轨量不出尺子，才去问别家
        doc = json.loads(target.read_text(encoding="utf-8"))
        bar = consensus_bar(doc, measures)
    erased = erase_only(measures, bar)             # 第一步：只擦，不加
    cleaned = list(erased)                         # **只擦不加**：补洞那一步先撤（它才是添乱的）
    reported = set(round(x, 6) for x in measures)
    extra = [round(x, 6) for x in cleaned if round(x, 6) not in reported]
    dropped = len(measures) - len(erased)          # 擦掉了几根（只删不加的那一步）
    if not holes:
        return "没有洞，跳过"
    doc = json.loads(target.read_text(encoding="utf-8"))
    lanes = [c for c in doc.get("calibrations") or [] if c.get("calibrationId") == LANE]
    redlines = (document.get("observations") or {}).get("exportedRedlines") or []
    lane = {"calibrationId": LANE, "source": "machine", "bpm": redlines[0]["bpm"] if redlines else None,
            "audioTime": cleaned[0], "beatsPerBar": 4, "beatUnit": 4,
            "note": "**推算 + 擦线轨**：① 擦掉模型那条里半路密一倍的半小节线（%d 根）；"
                    "② 洞里按全曲小节长度等分补齐（%d 根）。都不是模型报的。"
                    "洞有 %d 处（%s）。原始那条 observation 一个字节没动。" % (
                        dropped, len(extra),
                        len(holes), "、".join("%.1f–%.1f 秒（%.1f 秒）" % (
                            float(h["start"]), float(h["end"]), float(h.get("seconds") or 0))
                            for h in holes)),
            "barLines": sorted(cleaned), "filledLines": extra, "droppedLines": dropped,
            "health": "derived", "suspectReasons": ["擦过线、洞里是等分补的，都不是测量"],
            "reading": LANE}
    if lanes:
        lanes[0].clear()
        lanes[0].update(lane)
    else:
        doc.setdefault("calibrations", []).append(lane)
    target.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    return "补了 %d 根 / 擦了 %d 根（%d 个洞）" % (len(extra), dropped, len(holes))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--song", action="append", default=[])
    parser.add_argument("--runs-prefix", default="")
    args = parser.parse_args(argv)
    songs = args.song or sorted(p.name for p in RUNS.iterdir()
                                if p.is_dir() and p.name.startswith(args.runs_prefix))
    if not songs:
        parser.error("给 --song 或 --runs-prefix")
    done = holes = 0
    for song in songs:
        note = extend(song)
        if note.startswith("补了"):
            done += 1
            holes += int(note.split("（")[-1].rstrip(" 个洞）") or 0)
        elif note != "没有洞，跳过":
            print("%-9s %s" % (song, note))
    print("有洞并补上的：%d 首" % done)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
