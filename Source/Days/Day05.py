def execute_day_part1(data, maps, seeds):
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

def execute_day_part2(data, maps, seeds):
    def process_map(current_range, maps, idx):
        if idx >= len(maps):
            final_range = (maps[-1][0], current_range[1], current_range[2])
            print(final_range)
            return [final_range]
        name, elements = maps[idx]
        print(current_range)
        found_ranges = []
        final_ranges = []
        ranges_to_test = [(current_range[1], current_range[2])]
        unfound_ranges = []
        while len(ranges_to_test) != 0:
            was_range_found = False
            for element in elements:
                if len(ranges_to_test) == 0:
                    break
                range_to_test = ranges_to_test[0]
                dest, source, range_length = element
                # new_lower = range_to_test[0]
                # new_upper = range_to_test[1]
                
                source_range = range(max(range_to_test[0], source), min(range_to_test[1], source + range_length))

                if source_range.start < source_range.stop:
                    ranges_to_test.remove(range_to_test)
                    was_range_found = True
                    new_lower = dest + (source_range.start - source)
                    new_upper = dest + (source_range.stop - source)
                    found_ranges.append((name, new_lower, new_upper))

                    remainders = (source_range.start - range_to_test[0], range_to_test[1] - source_range.stop)
                    if remainders[0] > 0:
                        ranges_to_test.append((range_to_test[0], source_range.start))
                    if remainders[1] > 0:
                        ranges_to_test.append((source_range.stop, range_to_test[1]))
            if not was_range_found:
                unfound_ranges.append(range_to_test)
                ranges_to_test.remove(range_to_test)
        found_ranges.sort(key=lambda x: x[1])
        for found_range in found_ranges:
            final_ranges.extend(process_map(found_range, maps, idx+1))
        for unfound in unfound_ranges:
            new_range = (name, unfound[0], unfound[1])
            final_ranges.extend(process_map(new_range, maps, idx+1))
        if len(found_ranges) == 0:
            new_range = (name, range_to_test[0], range_to_test[1])
            final_ranges.extend(process_map(new_range, maps, idx+1))
        
        final_ranges.sort(key=lambda x: x[1])
        return final_ranges
    
    new_seeds = []
    new_seeds.append(("seeds", seeds[0], seeds[0] + seeds[1] - 1))
    new_seeds.append(("seeds", seeds[2], seeds[2] + seeds[3] - 1))
    seeds = new_seeds

    locations = []
    for seed in seeds:
        print("")
        locations.extend(process_map(seed, maps, 0))
    locations.sort(key=lambda x: x[1] if len(x) > 2 else 0)
    print(" ")
    for location in locations:
        print(location)
    print(locations[0][1])

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
    
    if part == 1:
        execute_day_part1(data, maps, seeds)
    else:
        execute_day_part2(data, maps, seeds)

execute_day(2)