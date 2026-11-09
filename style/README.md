# Python Style and Tooling

Use four spaces, `snake_case` for functions/variables, `PascalCase` for classes,
`UPPER_CASE` for constants, and a leading underscore for internal APIs. A global
variable is not automatically a constant. Prefer readable, explicit code over
clever one-liners. PEP 8 and PEP 257 remain useful references.

The modern learning track uses Ruff for linting/formatting, pytest for tests,
and a project-selected 100-character line length. That is a local convention,
not a claim that PEP 8's default changed. Comments explain intent, ownership,
and tradeoffs; docstrings explain public contracts. Add types at boundaries,
but use runtime validation for untrusted data.

```sh
uv run ruff check
uv run ruff format --check
uv run pytest
```

Prefer module docstrings, grouped imports, constants, helper definitions, then
`main()` and an `if __name__ == "__main__":` guard. Function bodies resolve names
when called, so `main()` does not have to be defined before its helpers. Optional
native imports can live inside explicit entry points so imports do not initialize
hardware or load models. Avoid `import *` outside the retained cautionary exercises.

Ruff and the default pytest discovery intentionally target the modern learning
track. Old standalone scripts remain supplementary examples, not import-safe
application modules. Run only the exercise you have read; some demonstrate
filesystem writes, network access, or intentionally bad patterns.
