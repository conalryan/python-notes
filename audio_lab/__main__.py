"""Run python -m audio_lab --help for explicit file and hardware commands."""

import argparse
from pathlib import Path

from audio_lab.codecs import export
from audio_lab.processing import (
    Track,
    fade,
    gain,
    load,
    mix,
    normalize_peak,
    pan,
    tone,
    trim,
    write_wav,
)
from audio_lab.record import record


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline audio and opt-in recording examples")
    commands = parser.add_subparsers(dest="command", required=True)
    demo = commands.add_parser("demo")
    demo.add_argument("output", type=Path)
    edit = commands.add_parser("edit")
    edit.add_argument("source", type=Path)
    edit.add_argument("output", type=Path)
    edit.add_argument("--start", type=float, default=0)
    edit.add_argument("--stop", type=float)
    edit.add_argument("--gain-db", type=float, default=0)
    edit.add_argument("--fade-seconds", type=float, default=0.01)
    conversion = commands.add_parser("export")
    conversion.add_argument("source", type=Path)
    conversion.add_argument("output", type=Path)
    recording = commands.add_parser("record")
    recording.add_argument("output", type=Path)
    recording.add_argument("--seconds", type=float, default=5)
    recording.add_argument("--sample-rate", type=int, default=48_000)
    recording.add_argument("--channels", type=int, default=1)
    recording.add_argument("--device", type=int)
    commands.add_parser("devices")
    arguments = parser.parse_args()

    match arguments.command:
        case "demo":
            voice = pan(fade(tone(440, 1)), -0.5)
            harmony = pan(fade(tone(660, 1)), 0.5)
            master = normalize_peak(mix([Track(voice), Track(harmony, start=0.25, decibels=-3)]))
            write_wav(master, arguments.output)
            print(f"{master.duration:.2f}s, {master.channels} channels, {master.sample_rate} Hz")
        case "edit":
            audio = load(arguments.source)
            stop = audio.duration if arguments.stop is None else arguments.stop
            edited = fade(
                gain(trim(audio, arguments.start, stop), arguments.gain_db), arguments.fade_seconds
            )
            write_wav(edited, arguments.output)
        case "export":
            export(arguments.source, arguments.output)
        case "record":
            overflows = record(
                arguments.output,
                seconds=arguments.seconds,
                sample_rate=arguments.sample_rate,
                channels=arguments.channels,
                device=arguments.device,
            )
            print(f"Input overflow reports: {overflows}")
        case "devices":
            import sounddevice as sd

            print(sd.query_devices())


if __name__ == "__main__":
    main()
