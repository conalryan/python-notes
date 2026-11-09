# Iterables, Iterators, and Collections

An iterable can produce an iterator with `iter()`. An iterator produces values
with `next()` and is usually consumed once. A generator is a particular kind of
iterator created by a function containing `yield` or a generator expression.

| Category | Examples | Important behavior |
| --- | --- | --- |
| Sequence | `str`, `bytes`, `list`, `tuple`, `range` | Indexed; `range` is lazy and reusable, not a generator |
| Mapping | `dict`, `defaultdict`, `Counter` | Key/value lookup; dictionaries preserve insertion order |
| Set | `set`, `frozenset` | Unique elements, no guaranteed iteration order; not a mapping |
| Iterator | `zip`, `enumerate`, `reversed`, file objects | Consumed incrementally; generally one-shot |
| View | `dict.keys()`, `dict.items()` | Reflects the underlying mapping; not an independent copy |
| Eager result | `sorted()`, list/set/dict comprehensions | Materializes the result in memory |

Use `zip(..., strict=True)` when paired inputs must have equal lengths. Python 3
`zip()` already iterates lazily; the old `itertools.izip` does not exist. Use
`itertools.batched()` for bounded chunks. `open()` returns a resource-owning file
object, not a generator; use a context manager even when iterating lazily.

For audio, NumPy arrays are typed numerical buffers, not Python lists.
Slicing a list copies the outer list; slicing a NumPy array generally returns a
shared-memory view. The audio workbench demonstrates explicit shapes and ownership.
