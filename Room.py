import random
from Enums import Compass


class Room:

    def __init__(self, direction_from):
        self.open_doors = []
        # for every move, the direction from where user came must be open
        # ie. open the opposite door of direction_from
        #TODO: abstract this
        if direction_from == Compass.NORTH:
            self.open_doors: ['south']
        elif direction_from == Compass.SOUTH:
            self.open_doors: ['north']
        elif direction_from == Compass.EAST:
            self.open_doors: ['west']
        elif direction_from == Compass.WEST:
            self.open_doors: ['east']
        elif direction_from.lower() == 'start':
            pass
        else:
            print("Error: could not determine direction({}) of previous room during __init__ of new Room"
                  .format(direction_from))

    def open_random_door(self):
        ran_choice = random.choice(["N", "N", "S", "S", "W", "W", "E", "E", "None", "None",
                                    "SW", "SE", "NW", "NE", "WE", "NS", "NES", "ESW", "ENW", "SWN"])
        if 'N' in ran_choice:
            self.open_doors.append('north')
        if 'W' in ran_choice:
            self.open_doors.append('west')
        if 'E' in ran_choice:
            self.open_doors.append('east')
        if 'S' in ran_choice:
            self.open_doors.append('south')

    def print_layout(self):
        print_string = "You come to a room with a door to "

        if self.open_doors:
            for door in self.open_doors:
                print_string += "the {},".format(door)
        else:
            print_string = "You reach a dead end with no doors"
        print(print_string)
