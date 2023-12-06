import random


class Sheep:
    def __init__(self, sequence_number, limit):
        self.sequence_number = sequence_number
        self.position = (random.uniform(-limit, limit), random.uniform(-limit, limit))
        self.is_alive = True

    def move(self, distance):
        direction = random.choice(['north', 'south', 'east', 'west'])
        if direction == 'north':
            self.position = (self.position[0], self.position[1] + distance)
        elif direction == 'south':
            self.position = (self.position[0], self.position[1] - distance)
        elif direction == 'east':
            self.position = (self.position[0] + distance, self.position[1])
        else:
            self.position = (self.position[0] - distance, self.position[1])
