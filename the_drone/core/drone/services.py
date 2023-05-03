from __future__ import annotations

from typing import Final
from typing import TYPE_CHECKING

from the_drone.core.drone.models import DroneMdl

if TYPE_CHECKING:
    from sqlalchemy.orm import Session
    from the_drone.core.drone.schemas import DroneCreateSch


class DroneSvc:
    @staticmethod
    def create(
        db: Session,
        drone_sch: DroneCreateSch,
    ) -> DroneMdl:
        drone_mdl: Final = DroneMdl(**drone_sch.dict())
        db.add(drone_mdl)
        db.commit()
        db.refresh(drone_mdl)
        return drone_mdl
