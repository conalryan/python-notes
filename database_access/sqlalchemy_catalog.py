"""SQLAlchemy 2: typed mappings, select(), and explicit transaction lifetimes."""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


class Base(DeclarativeBase):
    pass


class Clip(Base):
    __tablename__ = "clips"
    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str]
    sample_rate: Mapped[int]


def main() -> None:
    engine = create_engine("sqlite+pysqlite:///:memory:")
    try:
        # create_all is fine for a disposable demo; use Alembic migrations for real schemas.
        Base.metadata.create_all(engine)
        with Session(engine) as session, session.begin():
            session.add(Clip(label="voice", sample_rate=48_000))
        with Session(engine) as session:
            clips = session.scalars(select(Clip).where(Clip.label == "voice"))
            for clip in clips:
                print(clip.label, clip.sample_rate)
    finally:
        engine.dispose()


if __name__ == "__main__":
    main()
