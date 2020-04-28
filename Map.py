import Room


class Map:
    x: 100
    y: 100
    rooms: []
    # current_room: None

    def move(self, direction):
        if direction.lower() == 'w':
            self.y += 1
        elif direction.lower() == 's':
            self.y -= 1
        elif direction.lower() == 'a':
            self.x -= 1
        elif direction.lower() == 'd':
            self.x += 1

        self.rooms[self.x][self.y] = Room.Room(direction=direction)

    def print(self):
        print("Coordinates: ({},{})".format(self.x, self.y))

    def __init__(self, x=100, y=100):
        self.x = x
        self.y = y
        for i in range(0, 200):
            self.rooms[i] = []
        self.rooms[100][100] = Room.Room(direction="none")
