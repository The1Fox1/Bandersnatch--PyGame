from Map import Compass


class UserInput:
    def __init__(self):
        pass

    @staticmethod
    def input_to_compass(user_input):
        if user_input.casefold() == 'n':
            return Compass.NORTH
        elif user_input.casefold() == 'w':
            return Compass.WEST
        elif user_input.casefold() == 's':
            return Compass.SOUTH
        elif user_input.casefold() == 'e':
            return Compass.EAST
        else:
            return None
