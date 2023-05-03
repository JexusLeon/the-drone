from enum import unique

from strenum import StrEnum


@unique
class DroneModel(StrEnum):
    LIGHTWEIGHT = "Lightweight"
    MIDDLEWEIGHT = "Middleweight"
    CRUISERWEIGHT = "Cruiserweight"
    HEAVYWEIGHT = "Heavyweight"


@unique
class DroneState(StrEnum):
    IDLE = "IDLE"
    LOADING = "LOADING"
    LOADED = "LOADED"
    DELIVERING = "DELIVERING"
    DELIVERED = "DELIVERED"
    RETURNING = "RETURNING"
