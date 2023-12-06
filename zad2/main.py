import sheep
import random




def generate_sheep(sheep_number,init_pos):
    sheep_list = [] #list of sheep
    for i in range(sheep_number):
      sheep_list.append(sheep(random.uniform(-init_pos,init_pos),
                              random.uniform(-init_pos,init_pos)))
      sheep[i].no = i
    return sheep_list







if __name__ == '__main__':
    round = 50
    sheep = 15
    init_pos_of_sheep = 10.0
    sheep_distance_move = 0.5
    wolf_distance_move = 1.0

