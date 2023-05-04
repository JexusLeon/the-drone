from __future__ import annotations

from typing import Final
from typing import TYPE_CHECKING

from the_drone.core.medication.models import MedicationMdl

if TYPE_CHECKING:
    from sqlalchemy.orm import Session
    from the_drone.core.medication.schemas import MedicationCreateSch


class MedicationSvc:
    @staticmethod
    def create(
        db: Session,
        drone_id: int,
        med_sch: MedicationCreateSch,
    ) -> MedicationMdl:
        med_mdl: Final = MedicationMdl(**med_sch.dict(), drone_id=drone_id)
        db.add(med_mdl)
        db.commit()
        db.refresh(med_mdl)
        return med_mdl
