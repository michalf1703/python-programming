import math
import json
import csv

from sheep import Sheep
from wolf import Wolf


class Simulation:
    def __init__(self, num_sheep, limit, sheep_movement, wolf_movement, max_rounds):
        self.sheep_list = [Sheep(i, limit) for i in range(1, num_sheep + 1)]
        self.wolf = Wolf()
        self.max_rounds = max_rounds
        self.sheep_movement = sheep_movement
        self.wolf_movement = wolf_movement
        self.rounds_data = []

    def run(self):
        with open('alive.csv', 'w', newline='') as clean_csv_file:
            pass
        for round_num in range(1, self.max_rounds + 1):
            alive_sheep = sum(sheep.is_alive for sheep in self.sheep_list)

            # Sheep move
            for sheep in self.sheep_list:
                if sheep.is_alive:
                    sheep.move(self.sheep_movement)

            # Wolf moves
            closest_sheep = self.wolf.find_closest_sheep([sheep for sheep in self.sheep_list if sheep.is_alive])
            if closest_sheep:
                distance_to_sheep = math.dist(self.wolf.position, closest_sheep.position)
                if distance_to_sheep <= self.wolf_movement:
                    closest_sheep.is_alive = False
                    self.wolf.position = closest_sheep.position
                    self.wolf.chasing_sheep = None  # Wolf ate the sheep
                    print(f"Round {round_num}: Wolf ate sheep {closest_sheep.sequence_number}")
                else:
                    self.wolf.position = (
                        self.wolf.position[0] + (self.wolf_movement / distance_to_sheep) * (
                                    closest_sheep.position[0] - self.wolf.position[0]),
                        self.wolf.position[1] + (self.wolf_movement / distance_to_sheep) * (
                                    closest_sheep.position[1] - self.wolf.position[1])
                    )
                    self.wolf.chasing_sheep = closest_sheep.sequence_number

            else:
                print(f"Round {round_num}: No more alive sheep. Simulation over.")
                break
            alive_sheep = sum(sheep.is_alive for sheep in self.sheep_list)
            # Save number of alive sheep to csv file
            self.save_alive_count(round_num, alive_sheep)
            # Display simulation status
            self.display_status(round_num, alive_sheep)


            # Save positions to json file
            self.save_positions(round_num)



    def display_status(self, round_num, alive_sheep):
        print(f"Round {round_num}:")
        print(f"  Wolf Position: ({self.wolf.position[0]:.3f}, {self.wolf.position[1]:.3f})")
        print(f"  Alive Sheep: {alive_sheep}")
        if self.wolf.chasing_sheep is not None:
            print(f"  Wolf is chasing sheep {self.wolf.chasing_sheep}")

    def save_positions(self, round_num):
        positions = {
            'round_no': round_num,
            'wolf_pos': self.wolf.position,
            'sheep_pos': [sheep.position if sheep.is_alive else None for sheep in self.sheep_list]
        }
        self.rounds_data.append(positions)  # Dodaj dane rundy do listy

        with open('pos.json', 'w') as json_file:
            json.dump(self.rounds_data, json_file, indent=2)

    def save_alive_count(self, round_num, alive_sheep):
        with open('alive.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([round_num, alive_sheep])

# Example usage
simulation = Simulation(num_sheep=15, limit=10.0, sheep_movement=0.5, wolf_movement=1.0, max_rounds=50)
simulation.run()
