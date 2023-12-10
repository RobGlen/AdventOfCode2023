import re

def make_races(data):
    race_lengths = [int(value.strip()) for value in re.findall(r'\b\d+\b', data[0])]
    record_distances = [int(value.strip()) for value in re.findall(r'\b\d+\b', data[1])]
    races = []
    for i in range(len(race_lengths)):
        races.append((race_lengths[i], record_distances[i]))
    return races

def make_one_big_race(data):
    race_length = int(''.join(re.findall(r'\b\d+\b', data[0])))
    record_distance = int(''.join(re.findall(r'\b\d+\b', data[1])))
    return [ (race_length, record_distance) ]

def execute_day(part):
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day06.txt")
    data = [line.rstrip() for line in file]
    if part == 1:
        races = make_races(data)
    else:
        races = make_one_big_race(data)

    win_multiplier = 1
    for race in races:
        num_wins = 0
        race_length, record_distance = race
        for i in range(race_length):
            time_left = race_length - i
            speed = time_left * i
            if speed > record_distance:
                num_wins += 1
        win_multiplier *= num_wins
    print(win_multiplier)

execute_day(2)