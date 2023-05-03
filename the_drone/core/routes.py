from typing import Final

from fastapi import APIRouter

from the_drone.core.medication.endpoints import r_medication

routes: Final = APIRouter()
routes.include_router(router=r_medication)
