from typing import Final

from fastapi import APIRouter

from the_drone.core.dispatch_controller.endpoints import r_dispatch
from the_drone.core.drone.endpoints import r_drone

routes: Final = APIRouter()
routes.include_router(router=r_drone)
routes.include_router(router=r_dispatch)
