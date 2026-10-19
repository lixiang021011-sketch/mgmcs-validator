"""把 Mapperatorinator 的两件事拆成两条独立的轨（研究者 2026-10-12 定的）。

    python tools/docs/split_mapper_lanes.py --runs-prefix new_

**有洞** 和 **有密线** 是两回事，分别处理，互不依赖：

    mapperatorinator-erased   只擦：跟上一根保留线的距离 ≈ 半个大节就删掉（只删不加，
                              所以剩下的线一秒不动、不会有漂移）。**不管有没有洞。**
    mapperatorinator-filled   只补：只在模型自己声明的洞里，按大节等分出该有的根数，
                              洞外一根不动。**只在有洞的歌上出现。**

两条都是派生轨，原始那条 `mapperatorinator` 一个字节不动；旧的 `mapperatorinator-extended`
（把两件事混在一起的那条）会被删掉，免得页面上出现第三种说法。
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
ERASED, FILLED, OLD = "mapperatorinator-erased", "mapperatorinator-filled", "mapperatorinator-extended"


def big_bar(measures: list) -> float:
    """大节长度：间隔分档后，取"占两成以上"里**最大**的那一档（半小节只会让间隔变短）。"""
    gaps = [round(b - a, 2) for a, b in zip(measures, measures[1:]) if b - a > 0.05]
    if not gaps:
        return 0.0
    buckets = {}
    for gap in gaps:
        key = round(gap / 0.05) * 0.05
        buckets[key] = buckets.get(key, 0) + 1
    good = [k for k, c in buckets.items() if c >= max(2, int(len(gaps) * 0.2))]
    return max(good) if good else max(buckets.items(), key=lambda i: i[1])[0]


def erased_of(measures: list, bar: float) -> list:
    """只擦：跟上一根**保留线**差约半个大节就删，其余保留。"""
    keep = [measures[0]]
    for time in measures[1:]:
        if abs(time - keep[-1] - bar / 2) <= 0.25 * bar:
            continue
        keep.append(time)
    return keep


def filled_of(measures: list, bar: float, holes: list) -> list:
    """只补：在模型声明的每个洞里，按大节等分出该有的根数；洞外一根不动。"""
    extra = []
    for hole in holes:
        start, end = float(hole["start"]), float(hole["end"])
        span = end - start
        count = int(round(span / bar))
        for step in range(1, count):
            extra.append(round(start + span * step / count, 6))
    return extra


def run(song: str) -> str:
    source = OBSERVATIONS / ("%s.mapperatorinator.json" % song)
    target = DOCS / ("%s.mgmcs.json" % song)
    if not source.is_file() or not target.is_file():
        return ""
    document = json.loads(source.read_text(encoding="utf-8"))
    measures = [float(x) for x in (document.get("observations") or {}).get("measures") or []]
    holes = document.get("gaps") or []
    if len(measures) < 2:
        return ""
    bar = big_bar(measures)
    if bar <= 0:
        return ""
    erased = erased_of(measures, bar)
    filled = filled_of(measures, bar, holes)
    if len(erased) == len(measures) and not filled:
        return ""
    doc = json.loads(target.read_text(encoding="utf-8"))
    lanes = [c for c in doc.setdefault("calibrations", []) if c.get("calibrationId") != OLD]
    doc["calibrations"] = lanes
    redlines = (document.get("observations") or {}).get("exportedRedlines") or []
    bpm = redlines[0]["bpm"] if redlines else None
    notes = []
    for lane_id, body, note in ((ERASED, erased, "只擦：擦掉密一倍的半小节线（%d 根），"
                                            "只删不加，剩下的线一秒不动" % (len(measures) - len(erased))),
                                (FILLED, sorted(measures + filled),
                                 "只补：只在模型自己声明的洞里按大节等分补线（%d 根），洞外不动"
                                 % len(filled))):
        if lane_id == FILLED and not filled:
            continue
        if lane_id == ERASED and len(erased) == len(measures):
            continue
        lanes[:] = [c for c in lanes if c.get("calibrationId") != lane_id]
        lanes.append({"calibrationId": lane_id, "source": "machine", "bpm": bpm,
                      "audioTime": body[0], "beatsPerBar": 4, "beatUnit": 4, "note": note,
                      "barLines": body,
                      "droppedLines": len(measures) - len(erased) if lane_id == ERASED else 0,
                      "filledLines": filled if lane_id == FILLED else [],
                      "health": "derived", "suspectReasons": ["派生轨，不是测量"],
                      "reading": lane_id})
        notes.append("%s(%d)" % (lane_id.split("-")[-1], len(body)))
    target.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    return "、".join(notes)


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
    erased = filled = 0
    for song in songs:
        note = run(song)
        if "erased" in note:
            erased += 1
        if "filled" in note:
            filled += 1
        if note and (args.song or "filled" in note):
            print("%-9s %s" % (song, note))
    print("擦了线的：%d 首；补了洞的：%d 首" % (erased, filled))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
