from sqlalchemy import Column
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from the_drone.core.db.database import BaseMdl
from the_drone.core.drone.enums import DroneModel
from the_drone.core.drone.enums import DroneState


class DroneMdl(BaseMdl):
    __tablename__ = "drones"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String(100))
    model = Column(Enum(DroneModel))
    weight_limit = Column(Float)
    battery_capacity = Column(Integer, default=100)
    state = Column(Enum(DroneState), default=DroneState.IDLE)

    medications = relationship("MedicationMdl", back_populates="drone")  # type: ignore
    battery_records = relationship("BatteryRecordMdl", back_populates="drone")  # type: ignore
