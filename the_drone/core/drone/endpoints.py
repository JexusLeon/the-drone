from typing import Final

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from the_drone.core.db.database import get_db
from the_drone.core.drone.models import DroneMdl
from the_drone.core.drone.schemas import DroneCreateSch
from the_drone.core.drone.schemas import DroneSch
from the_drone.core.drone.services import DroneSvc

r_drone: Final = APIRouter(
    prefix="/drone",
    tags=["Drone"],
    responses={404: {"description": "Not found"}},
)


@r_drone.post("/create")
def _create(
    drone_sch: DroneCreateSch,
    db: Session = Depends(get_db),
) -> DroneSch:
    drone_mdl: Final = DroneMdl(**drone_sch.dict())
    return DroneSvc.create(db, drone_mdl)
