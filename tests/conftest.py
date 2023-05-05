from typing import Any
from typing import Final
from typing import Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from the_drone.core.db.database import BaseMdl
from the_drone.core.db.database import get_db
from the_drone.core.routes import routes

engine: Final = create_engine(
    "sqlite:///./the_drone_test.sqlite",
    connect_args={"check_same_thread": False},
)

SessionTestingLocal: Final = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def start_application() -> FastAPI:
    app: Final = FastAPI()
    app.include_router(routes)
    return app


@fixture(scope="function")
def app() -> Generator[FastAPI, Any, None]:
    """Create a fresh database on each test case."""
    BaseMdl.metadata.create_all(bind=engine)
    _app = start_application()
    yield _app
    BaseMdl.metadata.drop_all(bind=engine)


@fixture(scope="function")
def db(app: FastAPI) -> Generator[SessionTestingLocal, Any, None]:
    connection: Final = engine.connect()
    transaction: Final = connection.begin()
    session: Final = SessionTestingLocal(bind=connection)
    yield session  # Use the session in tests.
    session.close()
    transaction.rollback()
    connection.close()


@fixture(scope="function")
def client(
    app: FastAPI,
    db: SessionTestingLocal,
) -> Generator[TestClient, Any, None]:
    """Create a new FastAPI TestClient that uses the `db_session` fixture to
    override the `get_db` dependency that is injected into routes.
    """

    def _get_test_db():
        try:
            yield db
        finally:
            pass

    # noinspection PyUnresolvedReferences
    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as client:
        yield client


@fixture
def medications() -> list[dict]:
    medication1: Final = {
        "name": "Medication1",
        "weight": 50,
        "code": "MED_001",
        "image": "https://image.path/medication1.jpg"
    }
    medication2: Final = {
        "name": "Medication2",
        "weight": 100,
        "code": "MED_002",
        "image": "https://image.path/medication2.jpg"
    }
    medication3: Final = {
        "name": "Medication3",
        "weight": 150,
        "code": "MED_003",
        "image": "https://image.path/medication3.jpg"
    }
    return [medication1, medication2, medication3]
