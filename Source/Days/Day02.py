def part1_check_meets_constraints(count, constraints, colour, is_valid_to_constraints):
    if count > constraints[colour]:
        is_valid_to_constraints[colour] = False

def part1_add_game_sum(is_valid_to_constraints, game_num_sum, game_num):
    if all(value for value in is_valid_to_constraints.values()):
        game_num_sum += game_num
    return game_num_sum

def part2_check_min_viable_game(count, colour, colour_counts):
    if count > colour_counts[colour]:
        colour_counts[colour] = count

def part2_find_power_and_add_sum(colour_counts, game_num_sum):
    colour_power = 1
    for value in colour_counts.values():
        colour_power *= value
    game_num_sum += colour_power
    return game_num_sum

def execute_day(part):
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day02.txt")
    data = [line.rstrip() for line in file]

    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    game_num_sum = 0
    for line in data:
        sections = line.split(": ")
        game_num = int(sections[0].removeprefix("Game "))
        
        sets = sections[1].split("; ")
        #print(sets)

        is_valid_to_constraints = {
            "red": True,
            "green": True,
            "blue": True
        }

        colour_counts = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for set in sets:
            colours = set.split(", ")

            for colour_pairs in colours:
                num_colour_pair = colour_pairs.split(" ")
                count = int(num_colour_pair[0])
                colour = num_colour_pair[1]
                
                if part == 1:
                    part1_check_meets_constraints(count, constraints, colour, is_valid_to_constraints)
                else:
                    part2_check_min_viable_game(count, colour, colour_counts)
        if part == 1:
            game_num_sum = part1_add_game_sum(is_valid_to_constraints, game_num_sum, game_num)
        else:
            game_num_sum = part2_find_power_and_add_sum(colour_counts, game_num_sum)
        
    print(game_num_sum)

execute_day(2)