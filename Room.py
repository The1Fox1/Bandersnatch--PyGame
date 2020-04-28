import random


class Room:
    north_door: False
    west_door: False
    south_door: False
    east_door: False

    def open_random_door(self):
        ran_choice = random.choice(['N', 'S', 'W', 'E', 'None', 'None'])

        if ran_choice == 'N':
            self.north_door = True
        elif ran_choice == 'W':
            self.west_door = True
        elif ran_choice == 'E':
            self.east_door = True
        elif ran_choice == 'S':
            self.south_door = True
        else:
            pass

    def __init__(self, direction):
        if direction.lower() == 'n':
            self.south_door = True
        elif direction.lower() == 's':
            self. north_door = True
        elif direction.lower() == 'w':
            self.east_door = True
        elif direction.lower() == 'e':
            self.west_door = True
        elif direction.lower() == 'none':
            pass
        else:
            print("Error: could not determine direction({}) of previous room during __init__ of new Room"
                  .format(direction))
