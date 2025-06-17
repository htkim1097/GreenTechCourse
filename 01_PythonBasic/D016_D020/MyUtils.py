import math

def calc_dist(pos1: list, pos2: list):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

def min_value_idx(data):
    min_val = 99999999
    idx = -1

    if type(data) == list:
        for i, v in enumerate(data):
            if v < min_val:
                min_val = v
                idx = i

    return idx, min_val