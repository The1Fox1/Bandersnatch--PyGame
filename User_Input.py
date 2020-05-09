from Map import Compass


class UserInput:
    def __init__(self):
        pass

    @staticmethod
    def input_to_compass(user_input):
        if user_input.lower() == 'w':
            return Compass.NORTH
        elif user_input.lower() == 'a':
            return Compass.WEST
        elif user_input.lower() == 's':
            return Compass.SOUTH
        elif user_input.lower() == 'd':
            return Compass.EAST
        else:
            return None
