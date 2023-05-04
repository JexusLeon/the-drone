from typing import Final

from the_drone.core.dispatch_controller.schemas import ResponseSch
from the_drone.core.drone.enums import DroneModel
from the_drone.core.drone.models import DroneMdl
from the_drone.core.drone.services import DroneSvc


def _create_drones(db) -> None:
    drone_1: Final = DroneMdl(
        serial_number="DRONE_1",
        model=DroneModel.LIGHTWEIGHT,
        weight_limit=100,
    )
    drone_2: Final = DroneMdl(
        serial_number="DRONE_2",
        model=DroneModel.MIDDLEWEIGHT,
        weight_limit=250,
        battery_capacity=24
    )
    drone_3: Final = DroneMdl(
        serial_number="DRONE_2",
        model=DroneModel.HEAVYWEIGHT,
        weight_limit=500,
    )
    DroneSvc.create(db, drone_1)
    DroneSvc.create(db, drone_2)
    DroneSvc.create(db, drone_3)


def test_load_drone(db, client, medications) -> None:
    _create_drones(db)

    # Load the drone.
    response = client.post(
        "/dispatch/load-drone",
        json={"drone_id": 1, "medications": medications[1:2]},
    )
    assert response.status_code == 200, response.text
    resp_sch = ResponseSch(**response.json())
    assert resp_sch.success
    assert resp_sch.message == "Drone loaded successfully."

    # Try load the drone again.
    response = client.post(
        "/dispatch/load-drone",
        json={"drone_id": 1, "medications": medications[1:2]},
    )
    assert response.status_code == 200, response.text
    resp_sch = ResponseSch(**response.json())
    assert not resp_sch.success
    assert resp_sch.message == "Drone can not carry."
