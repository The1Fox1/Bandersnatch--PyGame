from Enums import Compass, Interaction


class UserInput:
    def __init__(self):
        pass

    @staticmethod
    def input_to_compass(user_input):
        if user_input.casefold() == 'n' or "north":
            return Compass.NORTH
        elif user_input.casefold() == 'w' or "west":
            return Compass.WEST
        elif user_input.casefold() == 's' or "south":
            return Compass.SOUTH
        elif user_input.casefold() == 'e' or "east":
            return Compass.EAST
        else:
            return None

    @staticmethod
    def input_to_interaction(user_input):
        inputs = user_input.split(" ")
        if inputs[0].casefold() == "inspect" or "look":
            return Interaction.INSPECT
        elif inputs[0].casefold() == "pickup" or "grab" or "take":
            return Interaction.PICKUP
        elif inputs[0].casefold() == "use" or "x":
            return Interaction.USE
        else:
            return None

    @staticmethod
    def input_to_bool(user_input):
        if user_input.casefold() == "yes" or 'y' or "true":
            return True
        elif user_input.casefold() == "no" or 'n' or "false":
            return False
        else:
            return None
