"""No network access: test download limits and file ownership using mock transport."""

from pathlib import Path

import pytest

httpx = pytest.importorskip("httpx")

from network_programming.download import download


def test_download_writes_bytes_and_protects_existing_files(tmp_path: Path) -> None:
    destination = tmp_path / "asset.bin"
    transport = httpx.MockTransport(lambda request: httpx.Response(200, content=b"asset"))
    with httpx.Client(transport=transport) as client:
        assert download(client, "https://example.test/asset", destination) == 5
        with pytest.raises(FileExistsError):
            download(client, "https://example.test/asset", destination)
    assert destination.read_bytes() == b"asset"


def test_download_limit_removes_only_its_partial_file(tmp_path: Path) -> None:
    destination = tmp_path / "asset.bin"
    transport = httpx.MockTransport(lambda request: httpx.Response(200, content=b"too large"))
    with httpx.Client(transport=transport) as client, pytest.raises(ValueError, match="size limit"):
        download(client, "https://example.test/asset", destination, max_bytes=3)
    assert not destination.exists()


def test_download_http_errors_and_insecure_urls(tmp_path: Path) -> None:
    destination = tmp_path / "asset.bin"
    transport = httpx.MockTransport(lambda request: httpx.Response(404))
    with httpx.Client(transport=transport) as client:
        with pytest.raises(httpx.HTTPStatusError):
            download(client, "https://example.test/missing", destination)
        with pytest.raises(ValueError, match="HTTPS"):
            download(client, "http://example.test/asset", destination)
    assert not destination.exists()
