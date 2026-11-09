# Current Database Examples

```sh
uv run python -m database_access.audio_catalog
uv run --extra database python -m database_access.sqlalchemy_catalog
# Only with a configured PostgreSQL connection:
uv run --extra database python -m database_access.postgres_catalog
```

SQLite and SQLAlchemy examples use disposable in-memory audio catalogs, not a
missing course database. PostgreSQL uses psycopg 3 and caller-provided
`DATABASE_URL`; no password is embedded. Connection, cursor, and transaction
lifetimes differ between drivers. SQLAlchemy 2 uses `Mapped`, `mapped_column`,
`select`, and explicit sessions rather than the old implicit execution patterns.

The old MySQL and psycopg2 course-server scripts were removed because they depended
on hardcoded credentials and an unavailable presidents schema. PyMySQL and
psycopg2 are not inherently obsolete; this learning path uses psycopg 3. Remaining
DB-API notes and SQL injection examples explain concepts, not deployment recipes.
Use bound values and driver identifier-composition APIs for dynamic table names;
a value placeholder cannot safely substitute a table identifier.