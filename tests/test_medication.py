from typing import Final

from the_drone.core.medication.schemas import MedicationSch


def test_create_medication(client) -> None:
    response = client.post(
        "/medication/create",
        json={
            "name": "Ibuprofen",
            "weight": 100.0,
            "code": "Z25123",
            "image": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAUDBAUEBAYGBQUGBgc...",
        },
    )
    assert response.status_code == 200, response.text
    medication_sch: Final = MedicationSch(**response.json())
    assert medication_sch.id == 1
    assert medication_sch.name == "Ibuprofen"
    assert medication_sch.code == "Z25123"
    assert medication_sch.weight == 100.0
