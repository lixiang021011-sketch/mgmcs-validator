"""给"只有机器产物、没有手机打点"的歌造一份种子文档，好让它进得了那条链。

    python tools/docs/seed_machine_docs.py --song new_07            # 先造一首看形状
    python tools/docs/seed_machine_docs.py --song new_07 --dry-run

为什么要有它：README 那条链的起点是**手机打点会话**（`merge_phone_taps.py` 挑一份当底再并机器网格）。
159 那批一首打点都没有，于是 `static/docs/new_*.mgmcs.json` 是 0 份，后面
`deviation_report → triage → timing_health_table` 扫不到它们，准入表里自然也是 0 首。

这个脚本只做"没有人工底"的那一半：

1. 建 `<短名>.mgmcs.json`，`calibrations` 里先放 **madmom**（从 `cache/<歌>/raw/madmom/madmom_v1.json`
   原样搬 —— 那是 `downbeats_madmom.py` 自己写的条目，含 barLines/downbeats）；
2. 再把 **workbench** 那条按 `import_workbench_grid.py` 的规矩写进来（锁定度当标注不当闸门）。
   为什么不直接调它：它的白名单只认那 34 首（`songs` 来自曲库清单），159 那批一律进 missing。
   这里**照抄它的构造规则**，不动它；**已知差异**：小节里有 odd_bars 的歌它会把 barLines 展开并标
   needsEars，本版只把 odd_bars 的条数写进 note、暂不展开 —— 铺到全库前要把这段补上。
3. **不碰人工那一层**：不造 `human` 校准，不写 `human_verdicts.json`。人工听审是输入，不是这个脚本能代替的。

Mapperatorinator 不进文档 —— 它住在 `static/observations/`，`deviation_report.py` 自己会去读
（`mapperatorinator_sources`），文档里再放一份就重复了。

幂等：文档已存在就跳过（要重建请先自己删或备份）。
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
VALIDATOR = HERE.parents[1]
DOCS = VALIDATOR / "static" / "docs"
RUNS = pathlib.Path(r"F:\vibe transcription\runs")
CACHE = pathlib.Path(r"F:\vibe transcription\music_explorer\cache")
MAIN_PYTHON = r"C:\Python314\python.exe"


def madmom_calibration(song: str) -> dict:
    """cache 里 madmom 自己写的那条校准，原样搬（不解释、不改数）。"""
    path = CACHE / song / "raw" / "madmom" / "madmom_v1.json"
    if not path.is_file():
        raise FileNotFoundError("%s 不在（先跑 tools/timing_on_drums.py）" % path)
    document = json.loads(path.read_text(encoding="utf-8"))
    for entry in document.get("calibrations") or []:
        if entry.get("calibrationId") == "madmom":
            return entry
    raise FileNotFoundError("%s 里没有 calibrationId=madmom 的条目" % path)


LOCK_OK = 0.9


def bar_lines(bpm, origin, beats_per_bar, odd_bars, count):
    """从起点走一遍，遇到 odd_bars 里记的短小节就按它自己的拍数走（照抄 import_workbench_grid）。"""
    lines, time = [], origin
    for _ in range(max(0, count)):
        lines.append(round(time, 6))
        beats = beats_per_bar
        for odd in odd_bars:
            # 我们 report.json 里 odd_bars 的元素是 [audio_time, beats] 两元组，
            # import_workbench_grid 里写的是 {"audio_time":…, "beats":…} —— 两种都认
            if isinstance(odd, dict):
                at, length = float(odd.get("audio_time", -1)), odd.get("beats")
            else:
                at, length = float(odd[0]), odd[1]
            if abs(at - time) < 1e-6:
                beats = float(length or beats_per_bar)
                break
        time += beats * 60.0 / bpm
    return lines


def workbench_calibration(song: str) -> dict:
    """workbench 那条校准，规则照 import_workbench_grid.py（锁定度只当标注）。"""
    report = json.loads((RUNS / song / "report.json").read_text(encoding="utf-8"))
    tempo = report.get("tempo") or {}
    down = report.get("downbeats") or {}
    bars = report.get("bars") or {}
    bpm, origin = float(tempo.get("bpm") or 0), float(down.get("first_downbeat") or 0)
    lock = float(down.get("beat_this_lock") or 0)
    if not (bpm > 0 and origin >= 0):
        raise FileNotFoundError("%s 的 report.json 里没有可用的 bpm/起点" % song)
    grid = {"calibrationId": "workbench", "source": "machine", "bpm": round(bpm, 6),
            "audioTime": round(origin, 6), "beatsPerBar": 4, "beatUnit": 4,
            "note": "隔壁 workbench 的读法：鼓起音定 16 分格 + Beat This! 定相位与强拍；速度恒定才成立",
            "sixteenthLock": tempo.get("sixteenth_lock"), "beatThisLock": lock,
            "health": "ok" if lock >= LOCK_OK else "suspect"}
    if not lock >= LOCK_OK:
        grid["suspectReasons"] = ["beatThisLock %.2f（< %.1f）：这是 workbench 这条校准的 source-health "
                                  "规则，不代表歌曲健康" % (lock, LOCK_OK)]
    odd = bars.get("odd_bars") or []
    if odd:
        lines = bar_lines(bpm, origin, 4, odd, int(bars.get("count") or 0))
        if lines:
            grid["barLines"] = [{"time": t} for t in lines]
            grid["needsEars"] = True
            grid["needsEarsNote"] = ("含 %d 个规则推出来的短小节：这是本读法按当前规则提出的局部 "
                                     "bar-structure 假设，需要耳朵确认；不是测量结果" % len(odd))
            grid["note"] += "；含 %d 个规则推出来的短小节（needsEars，只作人工审校提示）" % len(odd)
    if report.get("gates"):
        grid["gateNotes"] = report["gates"]
    return grid


CATALOG = pathlib.Path(r"F:\vibe transcription\music_explorer\datasets\catalog_v2.json")


def song_meta(song: str) -> dict:
    """文档里的 `song` 是**字典**（桥那边就是这个形状：songId/title/audioFileName）。

    踩过：我先写成字符串 `"new_07"`，`timing_health_table.audio_twins()` 直接
    `AttributeError: 'str' object has no attribute 'get'` —— 它读的正是这个字段。
    audioFileName 取**原曲**文件名（不是分轨），title 从 catalog 取、取不到就用短名。
    """
    state = json.loads((RUNS / song / "song.json").read_text(encoding="utf-8"))
    audio = pathlib.Path(state.get("song") or "")
    title = song
    if CATALOG.is_file():
        for row in (json.loads(CATALOG.read_text(encoding="utf-8")).get("songs") or []):
            if song in (row.get("displayName"), row.get("usedBy")):
                title = row.get("title") or song
                break
    return {"songId": song, "title": title, "audioFileName": audio.name}


def seed(song: str, dry_run: bool = False) -> str:
    target = DOCS / ("%s.mgmcs.json" % song)
    if target.exists():
        # 只有本脚本自己造的那种才允许重刷；别人（folding/人工）写的文档一律不碰
        existing = json.loads(target.read_text(encoding="utf-8"))
        if "seed_machine_docs.py" not in str(existing.get("generatedBy") or ""):
            return "已有文档且不是本脚本造的，跳过"
    document = {"schemaVersion": "0.1",
                "generatedBy": "seed_machine_docs.py（无人工底：只有机器来源）",
                "song": song_meta(song),
                "calibrations": [madmom_calibration(song), workbench_calibration(song)],
                "events": []}
    if dry_run:
        return "会写 %s（calibrations=%s）" % (target, [c["calibrationId"] for c in document["calibrations"]])
    DOCS.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(document, ensure_ascii=False, indent=1), encoding="utf-8")
    return "写好 %s（%s）" % (target.name, "、".join(c["calibrationId"]
                                                  for c in document["calibrations"]))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--song", action="append", default=[])
    parser.add_argument("--runs-prefix", default="")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    songs = args.song or sorted(path.name for path in RUNS.iterdir()
                                if path.is_dir() and args.runs_prefix
                                and path.name.startswith(args.runs_prefix))
    if not songs:
        parser.error("给 --song <歌>（可重复）或 --runs-prefix <前缀>")
    for song in songs:
        try:
            print("%-10s %s" % (song, seed(song, args.dry_run)))
        except FileNotFoundError as error:
            print("%-10s 跳过：%s" % (song, error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
