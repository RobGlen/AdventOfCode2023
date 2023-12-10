import math

part = 2

def handle_part1(directions_dict, turnings):
    current_loc = "AAA"

    turning_idx = 0
    steps = 0
    while(current_loc != "ZZZ"):
        current_loc = directions_dict[current_loc][turnings[turning_idx]]
        turning_idx = (turning_idx + 1) % len(turnings)
        steps += 1
    print(steps)

def one_z(current_locs):
    for loc in current_locs:
        if loc.count("Z") != 0:
            return True
    return False

def all_zs(current_locs):
    for loc in current_locs:
        if loc.count("Z") == 0:
            return False
    return True

def handle_part2(directions_dict, turnings):
    current_locs = list(filter(lambda x: 'A' in x, directions_dict.keys()))

    turning_idx = 0

    lengths = []
    for idx, current_loc in enumerate(current_locs):
        steps = 0
        while(current_loc.count('Z') == 0):
            current_loc = directions_dict[current_loc][turnings[turning_idx]]
            turning_idx = (turning_idx + 1) % len(turnings)
            steps += 1
        lengths.append(steps)

    result = math.lcm(*lengths)

    print(result)

def execute_day():
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day08.txt")
    data = [line.rstrip() for line in file]

    turnings = data[0]

    idx = 2
    directions_dict = {}
    while(idx < len(data)):
        entry = data[idx]
        node, directions_str = entry.split(" = ")
        directions = directions_str.removeprefix("(").removesuffix(")").split(", ")

        directions_dict[node] = {
            'L': directions[0],
            'R': directions[1]
        }
        idx += 1

    if part == 1:
        handle_part1(directions_dict, turnings)
    else:
        handle_part2(directions_dict, turnings)

execute_day()