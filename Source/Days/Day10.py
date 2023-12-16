part = 2

still = (0, 0)
up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

class PrintColors:
    PATH_HIGHLIGHT = '\033[93m'
    ENCLOSED_HIGHLIGHT = '\033[91m'
    ENDC = '\033[0m'

def add_tuple(a, b):
    return (a[0] + b[0], a[1] + b[1])

def create_procedures_dict():
    def vertical_pipe(pos, dir):
        if dir == down or dir == up:
            return True, add_tuple(pos, dir), dir
        return False, pos, still
    
    def horizontal_pipe(pos, dir):
        if dir == left or dir == right:
            return True, add_tuple(pos, dir), dir
        return False, pos, still
    
    def l_pipe(pos, dir):
        if dir == down:
            return True, add_tuple(pos, dir), right
        if dir == left:
            return True, add_tuple(pos, dir), up
        return False, pos, still
    
    def j_pipe(pos, dir):
        if dir == down:
            return True, add_tuple(pos, dir), left
        if dir == right:
            return True, add_tuple(pos, dir), up
        return False, pos, still

    def seven_pipe(pos, dir):
        if dir == up:
            return True, add_tuple(pos, dir), left
        if dir == right:
            return True, add_tuple(pos, dir), down
        return False, pos, still
    
    def f_pipe(pos, dir):
        if dir == up:
            return True, add_tuple(pos, dir), right
        if dir == left:
            return True, add_tuple(pos, dir), down
        return False, pos, still

    def s_node(pos, dir):
        return True, add_tuple(pos, dir), still
    
    procedures = {
        '|': vertical_pipe,
        '-': horizontal_pipe,
        'L': l_pipe,
        'J': j_pipe,
        '7': seven_pipe,
        'F': f_pipe,
        'S': s_node,
    }
    return procedures

def test_dir(pos, dir, data, procedures):
    new_pos = add_tuple(pos, dir)
    pipe = data[new_pos[1]][new_pos[0]]
    
    if pipe in procedures:
        return procedures[pipe](pos, dir)
    return False, pos, still

def print_loop(path, enclosed, data):
    for idx, entry in enumerate(data):
        print_str = ""
        for jdx, char in enumerate(entry):
            if (jdx, idx) in path:
                print_str += PrintColors.PATH_HIGHLIGHT + char + PrintColors.ENDC
            elif (jdx, idx) in enclosed:
                print_str += PrintColors.ENCLOSED_HIGHLIGHT + char + PrintColors.ENDC
            else:
                print_str += char
        print(print_str)
    print("")

def iterate_crawler(pos, dirs, data, procedures, path):
    for dir in dirs:
        is_success, new_pos, new_dir = test_dir(pos, dir, data, procedures)
        if is_success and new_pos not in path:
            path.append(new_pos)
            return new_pos, new_dir
    return pos, new_dir

def crawl_and_score_loop(start, data):
    procedures = create_procedures_dict()
    crawler1_pos = start
    steps = 1
    path = []

    start_dirs = [
        (0, 1),
        (1, 0),
        (-1, 0),
        (0, -1)
    ]

    dirs = start_dirs
    crawler1_pos, new_dir = iterate_crawler(crawler1_pos, dirs, data, procedures, path)
    dirs = [new_dir]
    while(data[crawler1_pos[1]][crawler1_pos[0]] != 'S'):
        new_pos, new_dir = iterate_crawler(crawler1_pos, dirs, data, procedures, path)
        crawler1_pos = new_pos
        dirs = [new_dir]
        steps += 1
    print(int(steps * 0.5))
    return path

def shoelace_formula(path, is_absolute=True):
    path_length = len(path)
    shoelace_area = [path[i][1] * (path[i - 1][0] - path[(i + 1) % path_length][0]) for i in range(0, path_length)]

    shoelace_sum = int(sum(shoelace_area) / 2.)
    if is_absolute:
        shoelace_sum = abs(shoelace_sum)
    return shoelace_area, shoelace_sum

def find_enclosed(path):
    enclosed, enclosed_sum = shoelace_formula(path)
    verts = len(enclosed)
    holes = 0
    picks_theorem = int(enclosed_sum - verts / 2 - holes + 1)
    print("Area: ", enclosed_sum, ", Verts: ", verts, ", Enclosed: ", picks_theorem)

def execute_day():
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day10.txt")
    data = [line.rstrip() for line in file]

    start = ()
    is_start_found = False
    for idx, entry in enumerate(data):
        for jdx, char in enumerate(entry):
            if char == 'S':
                start = (jdx, idx)
                is_start_found = True
                break
        if is_start_found:
            break
    path = crawl_and_score_loop(start, data)

    if part == 2:
        print_loop(path, [], data)
        find_enclosed(path)

execute_day()