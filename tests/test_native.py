"""Run after installing the Rust extension; base Python tests can skip this slice."""

import pytest

native = pytest.importorskip("rusty_audio")


def test_native_python_boundary() -> None:
    assert native.gain([0.25, -0.5], 0.0) == [0.25, -0.5]
    assert native.normalize([0.0, 0.0], -1.0) == [0.0, 0.0]
    assert native.normalize([-2.0, 1.0], -6.0) == pytest.approx(
        [-(10 ** (-6 / 20)), 10 ** (-6 / 20) / 2]
    )
    with pytest.raises(ValueError):
        native.gain([float("nan")], 0.0)
    with pytest.raises(ValueError):
        native.normalize([1.0], 1.0)
