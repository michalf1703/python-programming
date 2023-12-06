import random


class sheep:
    def __int__(self,x,y):
        self.x = x
        self.y = y
        self.status = "alive"
        self.no = 0

    def move_sheep(self, move_dist):
        options = random.choice(["north", "south", "east", "west"])
        if options == "north":
            self.y += move_dist
        elif options == "south":
            self.y -= move_dist
        elif options == "east":
            self.x += move_dist
        else:
            self.x -= move_dist

