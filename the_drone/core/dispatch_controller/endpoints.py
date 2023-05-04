from typing import Final
from typing import Sequence

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from the_drone.core.db.database import get_db
from the_drone.core.dispatch_controller.schemas import CheckDroneSch
from the_drone.core.dispatch_controller.schemas import LoadDroneSch
from the_drone.core.dispatch_controller.schemas import ResponseSch
from the_drone.core.dispatch_controller.services import DispatchCtlrSvc
from the_drone.core.drone.schemas import DroneSch
from the_drone.core.medication.schemas import MedicationSch

r_dispatch: Final = APIRouter(
    prefix="/dispatch",
    tags=["Dispatch Controller"],
    responses={404: {"description": "Not found"}},
)


@r_dispatch.post("/load-drone")
def _load_drone(
    load: LoadDroneSch,
    db: Session = Depends(get_db),
) -> ResponseSch:
    return DispatchCtlrSvc.load_drone(db, load)


@r_dispatch.get("/check-drone-battery")
def _check_drone_battery(
    check_drone: CheckDroneSch,
    db: Session = Depends(get_db),
) -> JSONResponse:
    battery: Final = DispatchCtlrSvc.drone_battery_level(db, check_drone)
    return JSONResponse(content={"battery_level": battery})


@r_dispatch.get("/drone-for-loading")
def _drone_for_loading(db: Session = Depends(get_db)) -> Sequence[DroneSch]:
    return DispatchCtlrSvc.drone_for_loading(db)


@r_dispatch.get("/check-loaded-drone")
def _check_loaded_drone(
    check_drone: CheckDroneSch,
    db: Session = Depends(get_db),
) -> Sequence[MedicationSch]:
    return DispatchCtlrSvc.get_loaded_medications(db, check_drone)
