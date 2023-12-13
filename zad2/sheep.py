import random


# Define the Sheep class
class Sheep:
    def __init__(self, sequence_number, limit):
        self.sequence_number = sequence_number
        # Initialize the position with random coordinates
        self.position = (random.uniform(-limit, limit),
                         random.uniform(-limit, limit))
        # Set the initial status of the sheep as alive
        self.is_alive = True

    def move(self, distance):
        # Randomly choose a direction
        direction = random.choice(['north', 'south', 'east', 'west'])
        if direction == 'north':
            self.position = (self.position[0], self.position[1] + distance)
        elif direction == 'south':
            self.position = (self.position[0], self.position[1] - distance)
        elif direction == 'east':
            self.position = (self.position[0] + distance, self.position[1])
        else:
            self.position = (self.position[0] - distance, self.position[1])
