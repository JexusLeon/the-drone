from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from the_drone.core.db.database import BaseMdl


class BatteryRecordMdl(BaseMdl):
    __tablename__ = "battery_records"

    id = Column(Integer, primary_key=True, index=True)
    battery_level = Column(Integer)
    datetime = Column(DateTime(timezone=True), server_default=func.now())

    drone_id = Column(Integer, ForeignKey("drones.id"))
    drone = relationship("DroneMdl", back_populates="battery_records")  # type: ignore
