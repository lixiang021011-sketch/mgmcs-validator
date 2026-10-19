"""给文档补上缺的机器轨：BeatThis、mapperatorinator、librosa —— 让页面上五条都看得见。

    python tools/docs/add_machine_lanes.py --song new_127
    python tools/docs/add_machine_lanes.py --runs-prefix new_

研究者 2026-10-12：`必须全都看见，并且很需要 librosa`。

现状：种子文档里只有 madmom + workbench 两条（那是 `import_workbench_grid` 的产出）。
BeatThis 和 Mapperatorinator **从来就不是文档里的 calibration**（34 那批也没有），
它们在 `runs/<歌>/beat_this.json` 与 `static/observations/` 里；librosa 那条要现跑
`tools/machine_beats.py`（纯 librosa、CPU、每首几秒）。

补的是**可见性**，不改任何一条既有校准的数值，也不动 34 那批（只碰 new_* 的文档）。
幂等：已经有这条 id 就跳过。
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
OBSERVATIONS = VALIDATOR / "static" / "observations"
RUNS = pathlib.Path(r"F:\vibe transcription\runs")
CATALOG = pathlib.Path(r"F:\vibe transcription\music_explorer\datasets\catalog_full.json")
# librosa 装在那个环境里（跟 merge_phone_taps.py 用的是同一个，见那里的 PY_BEATS）
PYTHON = r"D:\fa_tools\bp_venv\Scripts\python.exe"


def audio_of(song: str) -> str:
    return (json.loads(CATALOG.read_text(encoding="utf-8")).get(song) or {}).get("audio") or ""


def beatthis_lane(song: str) -> dict | None:
    """BeatThis：拍点/强拍原样搬，bpm 用跑批那张网格自报的值（只为显示）。"""
    path = RUNS / song / "beat_this.json"
    if not path.is_file():
        return None
    document = json.loads(path.read_text(encoding="utf-8"))
    beats = [float(x) for x in (document.get("beats") or [])]
    downs = [float(x) for x in (document.get("downbeats") or [])]
    if len(beats) < 2:
        return None
    report = RUNS / song / "report.json"
    bpm = None
    if report.is_file():
        bpm = ((json.loads(report.read_text(encoding="utf-8")).get("tempo")) or {}).get("bpm")
    return {"calibrationId": "BeatThis", "source": "machine", "bpm": bpm,
            "audioTime": beats[0], "beatsPerBar": 4, "beatUnit": 4,
            "note": "Beat This! 的拍点与强拍（原样搬自 runs/<歌>/beat_this.json；"
                    "bpm 一栏借的是同一批跑批自报的速度，只作显示）",
            "beats": beats, "downbeats": downs, "health": "ok", "suspectReasons": [],
            "reading": "BeatThis"}


def mapper_lane(song: str) -> dict | None:
    """Mapperatorinator：用它自己报的 measure 当小节线（局部观察者，带上有效区段）。"""
    path = OBSERVATIONS / ("%s.mapperatorinator.json" % song)
    if not path.is_file():
        return None
    document = json.loads(path.read_text(encoding="utf-8"))
    observations = document.get("observations") or {}
    measures = [float(x) for x in (observations.get("measures") or [])]
    beats = [float(x) for x in (observations.get("beats") or [])]
    redlines = observations.get("exportedRedlines") or []
    bpm = float(redlines[0]["bpm"]) if redlines else None
    if len(measures) < 2:
        return None
    return {"calibrationId": "mapperatorinator", "source": "machine", "bpm": bpm,
            "audioTime": measures[0], "beatsPerBar": 4, "beatUnit": 4,
            "note": "Mapperatorinator 自己报的 measure 当小节线；它是**局部**观察者"
                    "（有效区段 %s），出了区段别当真" % (document.get("validRanges") or "未标注"),
            "barLines": measures, "beats": beats, "health": "ok", "suspectReasons": [],
            "reading": "mapperatorinator", "validRanges": document.get("validRanges") or []}


def librosa_lane(song: str, tmp: pathlib.Path) -> dict | None:
    audio = audio_of(song)
    if not audio or not pathlib.Path(audio).is_file():
        return None
    out = tmp / ("%s.librosa.json" % song)
    result = subprocess.run([PYTHON, str(VALIDATOR / "tools" / "machine_beats.py"), audio,
                             "--out", str(out)], capture_output=True, text=True,
                            encoding="utf-8", errors="replace")
    if result.returncode != 0 or not out.is_file():
        return None
    document = json.loads(out.read_text(encoding="utf-8"))
    for entry in document.get("calibrations") or []:
        entry["calibrationId"] = "librosa"                  # 工具写的 id 是 machine
        entry["reading"] = "librosa"
        return entry
    return None


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--song", action="append", default=[])
    parser.add_argument("--runs-prefix", default="")
    parser.add_argument("--no-librosa", action="store_true")
    args = parser.parse_args(argv)
    songs = args.song or sorted(p.name for p in RUNS.iterdir()
                                if p.is_dir() and p.name.startswith(args.runs_prefix))
    songs = [s for s in songs if s]
    if not songs:
        parser.error("给 --song 或 --runs-prefix")
    tmp = VALIDATOR / "tmp"
    tmp.mkdir(exist_ok=True)
    for song in songs:
        target = DOCS / ("%s.mgmcs.json" % song)
        if not target.is_file():
            print("%-10s 没有文档，跳过" % song)
            continue
        document = json.loads(target.read_text(encoding="utf-8"))
        lanes = document.setdefault("calibrations", [])
        present = {entry.get("calibrationId") for entry in lanes}
        added = []
        for name, builder in (("BeatThis", lambda: beatthis_lane(song)),
                              ("mapperatorinator", lambda: mapper_lane(song))):
            if name in present:
                continue
            entry = builder()
            if entry:
                lanes.append(entry)
                added.append(name)
        if "librosa" not in present and not args.no_librosa:
            entry = librosa_lane(song, tmp)
            if entry:
                lanes.append(entry)
                added.append("librosa")
        if added:
            target.write_text(json.dumps(document, ensure_ascii=False, indent=1), encoding="utf-8")
        print("%-10s 补了：%s｜现在共 %d 条轨" % (song, "、".join(added) or "（没有可补的）",
                                              len(lanes)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
