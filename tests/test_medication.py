from typing import Final

import pytest
from pydantic import ValidationError

from the_drone.core.medication.schemas import MedicationCreateSch


def test_medication_schema(client) -> None:
    medication1: Final = MedicationCreateSch(
        name="Medication1",
        weight=50,
        code="MED_001",
    )
    assert medication1.weight == 50
    assert medication1.name == "Medication1"

    # The "code" attribute does not meet the requirements
    # because it is in lowercase.
    with pytest.raises(ValidationError):
        MedicationCreateSch(name="Medication2", weight=100, code="med_002")
