from typing import Final

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

import versioneer
from the_drone.core.db.database import SessionLocal
from the_drone.core.db.database import engine
from the_drone.core.db.models import BaseMdl
from the_drone.core.dispatch_controller.services import DispatchCtlrSvc
from the_drone.core.routes import routes


def create_tables() -> None:
    """Create all tables in the database."""
    BaseMdl.metadata.create_all(bind=engine)  # type: ignore


def start_application() -> FastAPI:
    create_tables()
    return FastAPI(
        debug=True,
        title="The Drone",
        version=versioneer.get_version(),  # type: ignore
        description="""Focuses on creating useful functions for drones.""",
    )


app: Final = start_application()
app.include_router(routes)


@app.on_event("startup")
@repeat_every(seconds=10)
def _task_check_drone_battery() -> None:
    db: Final = SessionLocal()
    try:
        DispatchCtlrSvc.log_drone_battery(db)
    finally:
        db.close()
