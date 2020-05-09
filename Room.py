import random
from Enums import Compass


class Room:

    def __init__(self, direction_from):
        self.open_doors = []
        # for every move, the direction from where user came must be open
        # ie. open the opposite door of direction_from
        #TODO: abstract this
        if direction_from == Compass.NORTH:
            self.open_doors: [Compass.SOUTH]
        elif direction_from == Compass.SOUTH:
            self.open_doors: [Compass.NORTH]
        elif direction_from == Compass.EAST:
            self.open_doors: [Compass.WEST]
        elif direction_from == Compass.WEST:
            self.open_doors: [Compass.EAST]
        elif direction_from.lower() == 'start':
            pass
        else:
            print("Error: could not determine direction({}) of previous room during __init__ of new Room"
                  .format(direction_from))

        self.open_random_door()

    def open_random_door(self):
        ran_choice = random.choice(["N", "N", "S", "S", "W", "W", "E", "E", "None", "None",
                                    "SW", "SE", "NW", "NE", "WE", "NS", "NES", "ESW", "ENW", "SWN"])
        if 'N' in ran_choice:
            self.open_doors.append(Compass.NORTH)
        if 'W' in ran_choice:
            self.open_doors.append(Compass.WEST)
        if 'E' in ran_choice:
            self.open_doors.append(Compass.EAST)
        if 'S' in ran_choice:
            self.open_doors.append(Compass.SOUTH)

    def print_layout(self):
        print_string = "You come to a room with a door to "
        if self.open_doors:
            for door in self.open_doors:
                print_string += "the {}, ".format(door.value)
        else:
            print_string = "You reach a dead end with no doors"
        print(print_string)
