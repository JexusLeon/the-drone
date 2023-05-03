from pydantic import BaseModel
from pydantic import Field

from the_drone.core.drone.enums import DroneModel
from the_drone.core.drone.enums import DroneState


class DroneBaseSch(BaseModel):
    serial_number: str = Field(min_length=1, max_length=100)
    model: DroneModel
    battery_capacity: int = 100
    state: DroneState = DroneState.IDLE
    weight_limit: float = Field(gt=0, lt=500)

    class Config:
        orm_mode = True


class DroneCreateSch(DroneBaseSch):
    pass


class DroneSch(DroneBaseSch):
    id: int
