import numpy as np

from Enums import Compass
from Room import Room


class Map:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rooms = dict()
        self.rooms[(0, 0)] = Room(direction_from="start")
        self.last_direction = None

    def move(self, direction):
        self.last_direction = direction

        #TODO: guard against illegal movement
        if direction == Compass.NORTH:
            self.y += 1
        elif direction == Compass.SOUTH:
            self.y -= 1
        elif direction == Compass.WEST:
            self.x -= 1
        elif direction == Compass.EAST:
            self.x += 1

        if (self.x, self.y) in self.rooms:
            pass
        else:
            self.rooms[(self.x, self.y)] = Room(direction_from=direction)

    def get_current_room(self):
        return self.rooms[(self.x, self.y)]

    def print_coordinates(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))
