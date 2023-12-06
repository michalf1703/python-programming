import math


class Wolf:
    def __init__(self):
        self.position = (0.0, 0.0)

    def find_closest_sheep(self, sheep_list):
        if sheep_list:
            return min(sheep_list, key=lambda s: math.dist(self.position, s.position))
        else:
            return None
