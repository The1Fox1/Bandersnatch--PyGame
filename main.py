from Map import Map
from Room import Room
from User_Input import UserInput


Map = Map()

print("Welcome to Bandersnatch \n By Brandon Fox")
wants_tutorial = UserInput.input_to_bool(input("Do you want an explanation for how to play the game?"))

if wants_tutorial:
    print("Each room will have doors you can go through. To move to another room"
          "type key words such as ('East', 'North', etc) to move in the direction of available doors \n"
          "Some rooms will have interactable parts. Type 'Inspect' or 'Look' to get a better description of it"
          "and sometimes you can perform actions such as 'Pickup' to add it to your inventory or 'Use'/'x' to "
          "Use them in certain scenarios")

while True:
    print("_"*30)
    Map.print_coordinates()
    room = Map.get_current_room()
    room.print_layout()

    user_input = input("Where do you go?")
    direction = UserInput.input_to_compass(user_input)
    MyMap.move(direction)
