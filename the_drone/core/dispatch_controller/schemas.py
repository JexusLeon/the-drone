from pydantic import BaseModel

from the_drone.core.medication.schemas import MedicationCreateSch


class CheckDroneSch(BaseModel):
    drone_id: int


class LoadDroneSch(CheckDroneSch):
    medications: list[MedicationCreateSch]


class ResponseSch(BaseModel):
    message: str
    success: bool
