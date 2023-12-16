part = 2

def add_tuple_component(a, b, idx):
    if idx == 0:
        return (a[0] + b, a[1])
    return (a[0], a[1] + b)

def subtract_tuple(a, b, is_abs=True):
    if is_abs:
        return (abs(a[0] - b[0]), abs(a[1] - b[1]))
    return (a[0] - b[0], a[1] - b[1])

def expand_universe(data):
    idx = 0
    while idx < len(data):
        row = data[idx]
        if row == '.' * len(row):
            data.insert(idx, row)
            idx += 2
        else:
            idx += 1

    idx = 0
    while idx < len(data[0]):
        is_empty = True
        for jdx, entry in enumerate(data):
            if data[jdx][idx] != '.':
                is_empty = False
                break
        if is_empty:
            for jdx, entry in enumerate(data):
                data[jdx] = data[jdx][:idx] + "." + data[jdx][idx:]
            idx += 2
        else:
            idx += 1

def expand_universe_efficient(data, galaxies, expansion_amount):
    new_galaxies = galaxies[:]
    for idx, row in enumerate(data):
        if row == '.' * len(row):
            for gdx, galaxy in enumerate(galaxies):
                if galaxy[1] > idx:
                    new_galaxies[gdx] = add_tuple_component(new_galaxies[gdx], expansion_amount - 1, 1)

    for idx, col in enumerate(data[0]):
        is_empty = True
        for jdx, entry in enumerate(data):
            if data[jdx][idx] != '.':
                is_empty = False
                break
        if is_empty:
            for gdx, galaxy in enumerate(galaxies):
                if galaxy[0] > idx:
                    new_galaxies[gdx] = add_tuple_component(new_galaxies[gdx], expansion_amount - 1, 0)
    return new_galaxies

def find_galaxies(data, galaxies):
    for idx, entry in enumerate(data):
        for jdx, char in enumerate(entry):
            if char == '#':
                galaxies.append((jdx, idx))

def execute_day():
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day11.txt")
    data = [line.rstrip() for line in file]

    for entry in data:
        print(entry)
    print("")

    #expand_universe(data)

    for entry in data:
        print(entry)
    
    galaxies = []
    find_galaxies(data, galaxies)

    expansion_amount = 2
    if part == 2:
        expansion_amount = 1000000
    
    print(galaxies)

    galaxies = expand_universe_efficient(data, galaxies, expansion_amount)
    
    print(galaxies)

    galaxy_dist_sum = 0
    for idx, galaxy in enumerate(galaxies):
        jdx = idx + 1
        while jdx < len(galaxies):
            other_galaxy = galaxies[jdx]
            # if galaxy == other_galaxy:
            #     continue
            galaxy_delta = subtract_tuple(galaxy, other_galaxy)
            dist = galaxy_delta[0] + galaxy_delta[1]
            galaxy_dist_sum += dist
            jdx += 1
    print(galaxy_dist_sum)



execute_day()