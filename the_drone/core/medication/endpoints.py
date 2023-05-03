from typing import Final

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from the_drone.core.db.database import get_db
from the_drone.core.medication.schemas import MedicationCreateSch
from the_drone.core.medication.schemas import MedicationSch
from the_drone.core.medication.services import MedicationSvc

r_medication: Final = APIRouter(
    prefix="/medication",
    tags=["Medication"],
    responses={404: {"description": "Not found"}},
)


@r_medication.post("/create")
def _create(
    medication_sch: MedicationCreateSch,
    db: Session = Depends(get_db),
) -> MedicationSch:
    medication_mdl: Final = MedicationSvc.create(db, medication_sch)
    return medication_mdl
