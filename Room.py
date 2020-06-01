import random
from Enums import Compass


class Room:

    def __init__(self, direction_from, interactables=[]):
        self.doors = set()
        self.interactables = interactables
        # self.description = ""
        self.__open_door_from(direction_from)
        self.open_random_door()

    def open_random_door(self):
        ran_choice = random.choice(["N", "N", "S", "S", "W", "W", "E", "E", "None", "None",
                                    "SW", "SE", "NW", "NE", "WE", "NS", "NES", "ESW", "ENW", "SWN"])
        if 'N' in ran_choice:
            self.doors.add(Compass.NORTH)
        if 'W' in ran_choice:
            self.doors.add(Compass.WEST)
        if 'E' in ran_choice:
            self.doors.add(Compass.EAST)
        if 'S' in ran_choice:
            self.doors.add(Compass.SOUTH)

    def print_layout(self):
        print_string = "You come to a room with a door to "
        if self.doors:
            for door in self.doors:
                print_string += "the {}, ".format(door.value)
        else:
            print_string = "You reach a dead end with no doors"

        if self.interactables:
            for item in self.interactables:
                print_string += "\n You see " + item.description
        else:
            print_string += "\n There doesn't appear to be anything if interest in this room"
        print(print_string)

    def __open_door_from(self, direction_from):
        if direction_from == Compass.NORTH:
            self.doors.add(Compass.SOUTH)
        elif direction_from == Compass.SOUTH:
            self.doors.add(Compass.NORTH)
        elif direction_from == Compass.EAST:
            self.doors.add(Compass.WEST)
        elif direction_from == Compass.WEST:
            self.doors.add(Compass.EAST)
        elif direction_from.lower() == 'start':
            self.open_random_door()
        else:
            print("Error: could not determine direction({}) of previous room during "
                  "__init__ of new Room".format(direction_from))


