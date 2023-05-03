from typing import Final
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

# Create an instance of a database connection.
engine: Final = create_engine(
    "sqlite:///./the_drone/assets/the_drone.sqlite",
    connect_args={"check_same_thread": False},  # Needed only for SQLite.
)

# Create a session to interact with the database.
SessionLocal: Final = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Create a base class for table definitions.
BaseMdl: Final = declarative_base()


# Dependency
def get_db() -> Generator[Session, None, None]:
    db: Final = SessionLocal()
    try:
        yield db
    finally:
        db.close()
