"""Fast checks for the learning examples, including cancellation semantics."""

import asyncio
import sys
from dataclasses import FrozenInstanceError

import pytest

from modern_python.concurrency import map_bounded
from modern_python.language import Clip, Gain, apply_effect, blocks, export_description
from modern_python.python314 import latest_features
from modern_python.stdlib import read_project_name


def test_language_contracts() -> None:
    clip = Clip(name="voice")
    with pytest.raises(FrozenInstanceError):
        clip.name = "changed"
    with pytest.raises(ValueError):
        Clip(name="voice", sample_rate=0)
    assert list(blocks(range(5), 2)) == [(0, 1), (2, 3), (4,)]
    assert apply_effect((0.5, -0.5), Gain(0)) == (0.5, -0.5)
    assert export_description({"format": "wav", "bits": 24}).endswith("24-bit")
    with pytest.raises(ValueError):
        export_description({"format": "wav", "bits": 8})
    assert read_project_name() == "python-audio-notes"


def test_concurrency_preserves_order_and_bounds_workers() -> None:
    async def scenario() -> None:
        active = 0
        peak = 0

        async def operation(value: int) -> int:
            nonlocal active, peak
            active += 1
            peak = max(peak, active)
            await asyncio.sleep(0)
            active -= 1
            return value * 2

        assert await map_bounded(list(range(10)), operation, concurrency=2) == list(range(0, 20, 2))
        assert peak == 2
        assert await map_bounded([], operation) == []

    asyncio.run(scenario())


@pytest.mark.skipif(sys.version_info < (3, 14), reason="Python 3.14 runtime APIs")
def test_python314_runtime_features() -> None:
    features = latest_features()
    assert features["annotations"] == {"name": "str", "return": "str"}
    assert features["session_uuid_version"] == 7
    assert features["template_parts"] == 2
    assert features["compression_round_trip"] is True
    assert features["partial_result"] == 16


def test_failure_cancels_sibling_work() -> None:
    async def scenario() -> None:
        ready = asyncio.Event()
        cancelled = asyncio.Event()

        async def operation(value: int) -> int:
            if value == 0:
                await ready.wait()
                raise ValueError("invalid clip")
            ready.set()
            try:
                await asyncio.Event().wait()
            finally:
                cancelled.set()
            return value

        with pytest.raises(ExceptionGroup) as error:
            await map_bounded([0, 1], operation, concurrency=2)
        assert isinstance(error.value.exceptions[0], ValueError)
        assert cancelled.is_set()

    asyncio.run(scenario())


def test_timeout_and_invalid_limits() -> None:
    async def scenario() -> None:
        async def operation(value: int) -> int:
            await asyncio.Event().wait()
            return value

        with pytest.raises(TimeoutError):
            async with asyncio.timeout(0.01):
                await map_bounded([1], operation)
        with pytest.raises(ValueError):
            await map_bounded([1], operation, concurrency=0)

    asyncio.run(scenario())
