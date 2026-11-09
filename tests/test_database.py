"""A current DB-API example that does not rely on an external course database."""

from database_access.audio_catalog import find_clips


def test_bound_parameters_do_not_become_sql() -> None:
    assert find_clips("voice") == [{"label": "voice", "sample_rate": 48_000}]
    assert find_clips("' OR 1=1 --") == []
