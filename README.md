# Python Notes: Modern Python, AI, and Audio

Notes and runnable examples for Python.
The current language target is **Python 3.14**. The practical examples use a
**Python 3.12+** baseline so native audio and machine-learning wheels have a
broader compatibility window. Use regular CPython first; free-threaded builds
are opt-in and require compatible extensions.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run:

```sh
uv python install 3.14
uv sync --python 3.14
uv run python -m modern_python.language
uv run pytest
uv run ruff check
```

To exercise the audio, API, and database tracks together:

```sh
uv sync --python 3.14 --extra audio --extra ai --extra database
uv run --no-sync pytest
```

Optional checks skip when their dependencies are absent. The CI matrix runs
Python 3.12/3.14 with FFmpeg and also builds/tests the Rust extension. It does not
access microphones, download models, or connect to an external database.

If an optional dependency does not provide a wheel for your interpreter, create
the environment with `uv sync --python 3.12 --extra audio` instead. Do not disable
TLS verification or compile large ML dependencies just to run these notes.
`uv sync` creates an isolated `.venv`; no global `pip install` is required.
The resolved Python dependencies are recorded in `uv.lock`. Use `uv sync --locked`
in CI. After dependency changes, regenerate the lock with `uv lock` and commit it.
For pip-only environments: `python3 -m venv .venv`, activate it, then
`python -m pip install -e '.[dev]'`.

## Learning Path

| Topic | Where to start | Frontend connection |
| --- | --- | --- |
| Typed data, matching, iterators, errors | [modern_python/language.py](modern_python/language.py) | Types are tooling contracts, not runtime validation; dataclasses are not JS objects |
| Structured concurrency | [modern_python/concurrency.py](modern_python/concurrency.py) | `asyncio` is cooperative, like the event loop; cancellation and CPU work need explicit handling |
| Paths, time zones, configuration | [modern_python/stdlib.py](modern_python/stdlib.py) | Use `pathlib`, aware datetimes, and TOML rather than string-built paths |
| Python 3.14 runtime features | [modern_python/python314.py](modern_python/python314.py) | Templates preserve interpolations; annotations are deferred; interpreter workers isolate state |
| HTTP and validated API boundaries | [ai_examples/README.md](ai_examples/README.md) | HTTPX + Pydantic + FastAPI; distinguish untrusted JSON from typed application data |
| PCM editing, mixing, export, recording | [audio_lab/README.md](audio_lab/README.md) | Frames, channels, sample rate, and callback deadlines replace browser-only media abstractions |
| Native DSP with Rust | [rust_audio/README.md](rust_audio/README.md) | PyO3 + maturin move measured hot loops into Rust; orchestration stays in Python |
| Modern relational access | [database_access/README.md](database_access/README.md) | Bound SQL values, explicit sessions, SQLAlchemy 2 mappings, and psycopg 3 |

The original topic folders remain as supplementary language exercises where the
concept is still useful. They are not production services and some deliberately
illustrate mistakes. Historical framework projects and obsolete drivers are
replaced by smaller current examples. New examples have explicit entry points
and avoid network, microphone, and model-loading side effects on import.

Removed material includes Python 2 sorters, unsupported Django snapshots,
duplicated course-database scripts with embedded credentials/missing fixtures,
automatic SSH host-key trust, and the deprecated `os.popen` demonstration.
The original core language, serialization, and unittest exercises remain useful
supplementary material; not all are included in the default test/lint discovery.

## Working Practices

- Prefer readable functions, dataclasses, and composition. Python objects are
  not all dictionaries; slots, descriptors, and native objects behave differently.
- Use built-in generics (`list[str]`), unions (`str | None`), and `Protocol` for
  structural interfaces. Type annotations do not validate external input.
- Use context managers for files and resources, UTF-8 for text, parameterized
  SQL, and timeouts for subprocesses and HTTP requests.
- Use pytest for behavior and Ruff for linting/formatting. Run examples as
  modules from the repository root so imports and paths are predictable.
- Python 3.14 adds deferred annotation evaluation and template string literals.
  Do not depend on eager annotation side effects; use `typing.get_type_hints`
  for ordinary runtime inspection. Template strings need a trusted processor;
  they are not automatic SQL or HTML escaping.
- The GIL does not make shared state race-free. Threads suit blocking I/O;
  processes or native extensions suit CPU work. Benchmark before rewriting DSP.
- For AI, start with arrays, inference, and validated boundaries before training.
  Keep tokens in environment variables, redact logs, and treat model output as
  untrusted data. Audio recordings may contain sensitive personal information.

## Libraries Worth Knowing

Use NumPy/SciPy for numerical work; SoundFile and sounddevice for file/device
audio; FFmpeg for codecs; PyTorch, Transformers, or faster-whisper for local ML;
HTTPX, Pydantic, and FastAPI for service boundaries; SQLAlchemy 2 and psycopg 3
for relational applications; and PyO3/maturin for Rust extensions. Each optional
example explains its system dependencies and tradeoffs. Requests, Flask, and
the standard `unittest` library are still valid, not obsolete just because newer
alternatives exist.

For distribution, prefer wheels and a `pyproject.toml`. PyInstaller bundles an
application for the platform on which it is built, not a universal executable.
Python 2 has been unsupported since 2020; its syntax and setup instructions are
not part of this learning path.
