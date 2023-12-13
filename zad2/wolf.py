import math

class Wolf:
    def __init__(self):
        # Initialize the wolf's position at the origin (0.0, 0.0)
        self.position = (0.0, 0.0)

    # Method to find the closest sheep from a list of sheep
    def find_closest_sheep(self, sheep_list):
        if sheep_list:
            # Find the sheep with the minimum distance
            # Lambda s: ... calculates the Euclidean distance
            return min(sheep_list,
                       key=lambda s: math.dist(self.position, s.position))
        else:
            return None
