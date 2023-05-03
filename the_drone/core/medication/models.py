from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from the_drone.core.db.database import BaseMdl


class MedicationMdl(BaseMdl):
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    weight = Column(Float)
    code = Column(String)
    image = Column(String)
