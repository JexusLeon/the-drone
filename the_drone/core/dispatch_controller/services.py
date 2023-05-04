from __future__ import annotations

from typing import Final
from typing import TYPE_CHECKING

from the_drone.core.dispatch_controller.schemas import CheckDroneSch
from the_drone.core.dispatch_controller.schemas import LoadDroneSch
from the_drone.core.dispatch_controller.schemas import ResponseSch
from the_drone.core.drone.enums import DroneState
from the_drone.core.drone.models import DroneMdl
from the_drone.core.drone.services import DroneSvc
from the_drone.core.medication.models import MedicationMdl
from the_drone.core.medication.services import MedicationSvc

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


# noinspection PyTypeChecker
class DispatchCtlrSvc:
    """Dispatch Controller Service."""

    @staticmethod
    def load_drone(
        db: Session,
        load: LoadDroneSch,
    ) -> ResponseSch:
        drone_mdl: Final = DroneSvc.get(db, load.drone_id)
        if drone_mdl is None:
            message: str = "Drone do not exist."
            return ResponseSch(success=False, message=message)

        if (
            drone_mdl.state != DroneState.IDLE
            or drone_mdl.battery_capacity < 25
        ):
            message = "Drone can not carry."
            return ResponseSch(success=False, message=message)

        total_weight: Final = sum(med.weight for med in load.medications)
        if total_weight > drone_mdl.weight_limit:
            message = "Too much weight to carry."
            return ResponseSch(success=False, message=message)

        for med in load.medications:
            med_mdl: MedicationMdl = MedicationSvc.create(
                db=db,
                drone_id=drone_mdl.id,  # type: ignore
                med_sch=med,
            )
            drone_mdl.medications.append(med_mdl)
        drone_mdl.state = DroneState.LOADED  # type: ignore
        db.commit()
        message = "Drone loaded successfully."
        return ResponseSch(success=True, message=message)

    @staticmethod
    def get_loaded_medications(
        db: Session,
        check_drone: CheckDroneSch,
    ) -> list[MedicationMdl]:
        drone_mdl: Final = DroneSvc.get(db, check_drone.drone_id)
        return drone_mdl.medications if drone_mdl else []  # type: ignore

    @staticmethod
    def drone_for_loading(db: Session) -> list[DroneMdl]:
        query: Final = db.query(DroneMdl)
        return query.filter(DroneMdl.state == DroneState.IDLE).all()

    @staticmethod
    def drone_battery_level(
        db: Session,
        check_drone: CheckDroneSch,
    ) -> float | None:
        drone_mdl: Final = DroneSvc.get(db, check_drone.drone_id)
        return drone_mdl.battery_capacity if drone_mdl else None  # type: ignore
