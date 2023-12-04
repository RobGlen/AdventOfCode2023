def find_part_no(data, idx, jdx):
    part_nos = []
    pos_to_test = [
        (idx-1, jdx),
        (idx+1, jdx),
        (idx, jdx-1),
        (idx, jdx+1),
        (idx-1, jdx-1),
        (idx+1, jdx-1),
        (idx-1, jdx+1),
        (idx+1, jdx+1),
    ]

    for pos in pos_to_test:
        current_row = data[pos[0]]
        if current_row[pos[1]].isnumeric():
            start_pos = pos[1]
            end_pos = pos[1]

            while start_pos - 1 >= -1 and current_row[start_pos - 1].isnumeric():
                start_pos -= 1

            while end_pos + 1 < len(current_row) and current_row[end_pos + 1].isnumeric():
                end_pos += 1

            part_no = current_row[start_pos:end_pos+1]
            part_no_num = int(part_no)

            if part_no_num not in part_nos:
                #print(part_no)
                part_nos.append(part_no_num)
    return part_nos

def execute_day(part):
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day03.txt")
    data = [line.rstrip() for line in file]

    part_nos = []
    gear_sum = 0
    for idx, entry in enumerate(data):
        for jdx, digit in enumerate(entry):
            if digit != '.' and not digit.isnumeric():
                new_part_nos = find_part_no(data, idx, jdx)
                part_nos.extend(new_part_nos)

                if part == 2:
                    if digit == '*' and len(new_part_nos) == 2:
                        gear_sum += new_part_nos[0] * new_part_nos[1]
    
    if part == 1:
        part_no_sum = 0
        for part_no in part_nos:
            part_no_sum += part_no
        print(part_no_sum)
    else:
        print(gear_sum)


execute_day(2)