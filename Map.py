# import numpy as np

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
        illegal = self.__is_allowed_move(direction)
        if illegal:
            print("Illegal movement. Try going through one of the open doors")
        else:
            self.__change_coordinates(direction)
            self.last_direction = direction
            if (self.x, self.y) in self.rooms:
                pass
            else:
                self.rooms[(self.x, self.y)] = Room(direction_from=direction)

    def get_current_room(self):
        return self.rooms[(self.x, self.y)]

    def print_coordinates(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))

    def __change_coordinates(self, direction):
        if direction == Compass.NORTH:
            self.y += 1
            print("You move North")
        elif direction == Compass.SOUTH:
            self.y -= 1
            print("You move South")
        elif direction == Compass.WEST:
            self.x -= 1
            print("You move West")
        elif direction == Compass.EAST:
            self.x += 1
            print("You move East")

    def __is_allowed_move(self, direction):
        if direction in self.rooms[(self.x, self.y)].doors:
            return False
        else:
            return True
