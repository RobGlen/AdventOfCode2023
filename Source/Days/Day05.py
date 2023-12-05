def execute_day(part):
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day05.txt")
    data = [line.rstrip() for line in file]
    seeds = [int(seed) for seed in data[0].removeprefix("seeds: ").split(" ")]
    print(seeds)

    seed_to_soil = []
    soil_to_fertilizer = []
    fertilizer_to_water = []
    water_to_light = []
    light_to_temperature = []
    temperature_to_humidity = []
    humidity_to_location = []

    maps = [
        ("seed_to_soil", seed_to_soil),
        ("soil_to_fertilizer", soil_to_fertilizer),
        ("fertilizer_to_water", fertilizer_to_water),
        ("water_to_light", water_to_light),
        ("light_to_temperature", light_to_temperature),
        ("temperature_to_humidity", temperature_to_humidity),
        ("humidity_to_location", humidity_to_location)
    ]

    idx = 3
    current_map_index = 0
    while idx != len(data):
        if data[idx] != '':
            if data[idx][0].isnumeric():
                dest, source, range_length = [int(value) for value in data[idx].split(" ")]
                if current_map_index < len(maps):
                    maps[current_map_index][1].append((dest, source, range_length))
        else:
            current_map_index += 1
        idx += 1
    
    current_dest = 0
    current_dest_range = 1
    locations = []

    for seed in seeds:
        path = [ seed ]
        current_seed = seed
        current_dest = current_seed

        for map in maps:
            is_dest_found = False
            name, elements = map
            for element in elements:
                dest, source, range_length = element
                for i in range(current_dest_range):
                    if current_dest + i >= source and current_dest + i <= source + range_length:
                        
                        current_dest = dest + (current_dest - source)
                        # current_dest_range = range_length
                        is_dest_found = True
                        path.append(current_dest)
                        break
                if is_dest_found:
                    break
            if not is_dest_found:
                path.append(current_dest)
        locations.append(current_dest)
        print(path)
    print(locations)
    lowest = locations[0]
    for location in locations:
        if location < lowest:
            lowest = location
    print(lowest)

execute_day(1)