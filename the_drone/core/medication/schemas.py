from pydantic import BaseModel
from pydantic import Field


class MedicationBaseSch(BaseModel):
    name: str = Field(regex=r"^[a-zA-Z0-9_-]+$", min_length=1)
    code: str = Field(regex=r"^[A-Z0-9_]+$", min_length=1)
    weight: float
    image: str = ""

    class Config:
        orm_mode = True


class MedicationCreateSch(MedicationBaseSch):
    pass


class MedicationSch(MedicationBaseSch):
    id: int
