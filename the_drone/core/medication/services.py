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
        medication_sch: MedicationCreateSch,
    ) -> MedicationMdl:
        medication_mdl: Final = MedicationMdl(**medication_sch.dict())
        db.add(medication_mdl)
        db.commit()
        db.refresh(medication_mdl)
        return medication_mdl
