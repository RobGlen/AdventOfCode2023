part = 2

def execute_day():
    if part != 1 and part != 2:
        pass
    file = open("Data/Input/Day09.txt")
    data = [line.rstrip() for line in file]

    sum_of_new_history = 0
    for entry in data:
        history = [int(value) for value in entry.split(" ")]
        diffs = [history]

        while diffs[-1] != len(diffs[-1]) * [0]:
            new_history_diff = []
            current_diff = diffs[-1]
            for idx, num in enumerate(diffs[-1]):
                if idx + 1 == len(current_diff):
                    continue
                new_hist_num = current_diff[idx+1] - current_diff[idx]
                new_history_diff.append(new_hist_num)
            diffs.append(new_history_diff)
        
        if part == 1:
            idx = len(diffs) - 2
            while(idx >= 0):
                diff = diffs[idx][-1]
                diffs[idx].append(diff + diffs[idx+1][-1])
                idx -= 1
            sum_of_new_history += diffs[0][-1]
        else:
            idx = len(diffs) - 2
            while(idx >= 0):
                diff = diffs[idx][0]
                diffs[idx].insert(0, diff - diffs[idx+1][0])
                idx -= 1
            sum_of_new_history += diffs[0][0]
    print(sum_of_new_history)

execute_day()