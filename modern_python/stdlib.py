"""Paths, configuration, and time zones without third-party dependencies."""

import tomllib
from datetime import UTC, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def read_project_name(path: Path = ROOT / "pyproject.toml") -> str:
    # tomllib reads TOML, not writes it. Binary mode lets it decode UTF-8 correctly.
    with path.open("rb") as source:
        config = tomllib.load(source)
    return str(config["project"]["name"])


def main() -> None:
    now = datetime.now(UTC)
    print(now.isoformat())
    print(now.astimezone(ZoneInfo("America/Los_Angeles")).isoformat())
    print(read_project_name())
    # Use UTC instants for storage, a named zone for presentation, and
    # perf_counter() for elapsed durations. A wall clock can jump backwards.
    print(sorted(path.name for path in (ROOT / "data").glob("*.json")))


if __name__ == "__main__":
    main()
