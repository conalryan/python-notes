"""psycopg 3 example: explicit credentials, parameter binding, and row factories."""

import os


def main() -> None:
    import psycopg
    from psycopg.rows import dict_row

    # DATABASE_URL is configured by the caller. Never print it or commit passwords.
    # Use sslmode=verify-full and a trusted CA for a remote production connection.
    with (
        psycopg.connect(
            os.environ["DATABASE_URL"], row_factory=dict_row, connect_timeout=5
        ) as connection,
        connection.cursor() as cursor,
    ):
        cursor.execute("SET statement_timeout = '5s'")
        # A temporary table makes this runnable without modifying an application schema.
        cursor.execute("CREATE TEMP TABLE clips (label TEXT, sample_rate INTEGER)")
        cursor.execute("INSERT INTO clips VALUES (%s, %s)", ("voice", 48_000))
        cursor.execute("SELECT * FROM clips WHERE label = %s", ("voice",))
        print(cursor.fetchall())
    # psycopg 3's connection context commits/rolls back AND closes the connection.


if __name__ == "__main__":
    main()
