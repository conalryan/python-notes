# A Frontend Engineer's Python Refresher

```sh
uv run python -m modern_python.language
uv run python -m modern_python.concurrency
uv run python -m modern_python.stdlib
uv run --python 3.14 python -m modern_python.python314
```

## Differences Worth Relearning

- Names refer to objects; assignment does not clone them. `list` slices copy the
  outer list, but nested objects remain shared. NumPy slices usually share buffers.
- Python collections are heterogeneous at runtime. `list[float]` is a tooling
  contract, while Pydantic validates incoming data. `None` is not `undefined`;
  compare it with `is None`, and use `==` for value equality.
- `dict` preserves insertion order. Iterators are one-shot streams; `range` is a
  reusable lazy sequence, not a generator. Comprehensions are idiomatic for data
  transforms, but use ordinary loops for side effects or complicated control flow.
- Mutable defaults are shared between calls. Use `None` and construct a new list
  inside the function, or use `field(default_factory=list)` in a dataclass.
- `frozen=True` prevents attribute rebinding, not deep mutation. Use immutable
  fields for immutable metadata; an array field still needs an ownership policy.
- Protocols describe structural behavior; dataclasses generate boring data-model
  methods; classes need not stand in for every object literal. Prefer composition.
- `asyncio` tasks cooperate at `await`. Creating a coroutine does not run it.
  TaskGroup owns task lifetimes and cancels siblings on failure. `except*` handles
  selected members of an ExceptionGroup; don't swallow cancellation exceptions.
- The GIL is not an application lock. Native numerical libraries may release it;
  thread pools fit blocking I/O, and processes/native work fit CPU-heavy routines.

## What Changed Since These Notes Were Written

Python 3.11 brought TaskGroup, ExceptionGroup/`except*`, `asyncio.timeout`, and
`tomllib`. Python 3.12 added PEP 695 type/generic syntax and `itertools.batched`.
Python 3.13 added an improved REPL, `copy.replace`, and optional free-threading.
Python 3.14 adds deferred annotations, template strings, UUIDv7, Zstandard,
interpreter executors, and officially supported optional free-threading. None of
these means native ML/audio extensions automatically support every build mode.

`python314.py` uses runtime APIs only on 3.14. A template literal looks like
`t"Track: {name}"`; unlike an f-string it retains interpolation objects for a
processor. It is not automatically a safe HTML template, SQL query, or shell
command. UUIDv7 is time-ordered, not a secret or authorization token. Annotation
introspection can execute expressions: do it only on trusted code.

Use [the official Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)
as the reference. All examples include comments explaining the behavior and its
tradeoffs; the new default tests exercise these contracts rather than importing
every old script with filesystem or network side effects.