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
        is_range_found = False
        for element in elements:
            dest, source, range_length = element
            source_end = source + range_length
            
            source_range = range(max(current_range[1], source), min(current_range[2], source_end))

            if source_range.start < source_range.stop:
                is_range_found = True
                new_lower = dest + (source_range.start - source)
                new_upper = dest + (source_range.stop - source)
                
                results = process_map((name, new_lower, new_upper), maps, idx+1)

                remainders = (source - current_range[1], current_range[2] - source_end)
                if remainders[0] > 0:
                    results.extend(process_map((current_range[0], current_range[1], source), maps, idx))
                if remainders[1] > 0:
                    results.extend(process_map((current_range[0], source_end, current_range[2]), maps, idx))
                for result in results:
                    if result not in final_ranges:
                        final_ranges.append(result)
            if is_range_found:
                break
        if not is_range_found:
            new_range = (name, current_range[1], current_range[2])
            results = process_map(new_range, maps, idx+1)
            for result in results:
                if result not in final_ranges:
                    final_ranges.append(result)
        
        final_ranges.sort(key=lambda x: x[1])
        return final_ranges
    
    new_seeds = []
    seeds_idx = 0
    while seeds_idx < len(seeds):
        new_seeds.append(("seeds", seeds[seeds_idx], seeds[seeds_idx] + seeds[seeds_idx + 1] - 1))
        seeds_idx += 2
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