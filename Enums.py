from enum import Enum


class Compass(Enum):
    NORTH = "North"
    WEST = "West"
    EAST = "East"
    SOUTH = "South"


class Interaction(Enum):
    INSPECT = 0
    PICKUP = 1
    USE = 2
