"""Run python -m database_access.audio_catalog; no external database is required."""

import sqlite3
from contextlib import closing


def find_clips(label: str) -> list[dict[str, object]]:
    # A connection's context manager commits/rolls back; closing also releases it.
    # Python 3.12 added autocommit: choose explicit transactions, not legacy defaults.
    with closing(sqlite3.connect(":memory:", autocommit=False)) as connection:
        connection.row_factory = sqlite3.Row
        with connection:
            connection.execute("CREATE TABLE clips (label TEXT, sample_rate INTEGER)")
            connection.executemany(
                "INSERT INTO clips VALUES (?, ?)", [("voice", 48_000), ("drums", 48_000)]
            )
        # Bind values, never interpolate SQL; quote characters stay data.
        rows = connection.execute("SELECT * FROM clips WHERE label = ?", (label,))
        return [dict(row) for row in rows]


if __name__ == "__main__":
    print(find_clips("voice"))
    print(find_clips("' OR 1=1 --"))
