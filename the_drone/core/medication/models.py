from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from the_drone.core.db.database import BaseMdl


class MedicationMdl(BaseMdl):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    weight = Column(Float)
    code = Column(String)
    image = Column(String)

    drone_id = Column(Integer, ForeignKey("drones.id"))
    drone = relationship("DroneMdl", back_populates="medications")  # type: ignore
