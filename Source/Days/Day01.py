
def execute_day(part):
    if part != 1 and part != 2:
        pass

    file = open("Data/Input/Day01.txt")

    data = [line.rstrip() for line in file]

    num_words = []

    if part == 2:
        num_words = [
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9)
        ]

    def determine_entry(entry):
        digits_str = ""
        for idx, i in enumerate(entry):
            if i.isnumeric():
                digits_str += i
            
            for word in num_words:
                for idx2 in range(idx+1, len(entry), 1):
                    if word[0] == entry[idx:idx2+1]:
                        digits_str += str(word[1])
                        break

        return digits_str

    sum = 0
    count = 0
    for entry in data:
        digits_str = ""
        digits_str += determine_entry(entry)
        if len(digits_str) >= 1:
            digits_str = digits_str[0] + digits_str[-1]

        digits_num = 0
        if digits_str != '':
            digits_num = int(digits_str)
            print(count, " ", digits_num)
            count += 1
        sum += digits_num
    
    print(sum)


execute_day(2)