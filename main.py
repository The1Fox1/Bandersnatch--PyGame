from Map import Map
from Room import Room
from User_Input import UserInput


MyMap = Map()

while True:
    print("_"*30)
    MyMap.print_coordinates()
    room = MyMap.get_current_room()
    room.print_layout()

    user_input = input("Where do you go?")
    direction = UserInput.input_to_compass(user_input)
    MyMap.move(direction)
