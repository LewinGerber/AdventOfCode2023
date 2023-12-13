
def analyze_line(initial_line: list[str]):
    lists = []
    is_current_list_only_zeros = False
    current_line = initial_line
    next_line = []

    while not is_current_list_only_zeros:
        for index in range(len(current_line) - 1):
            new_value = int(current_line[index + 1]) - int(current_line[index])
            next_line.append(new_value)

        total_sum = 0
        for number in next_line:
            total_sum += number

        if total_sum == 0:
            is_current_list_only_zeros = True
        lists.append(current_line.copy())
        current_line = next_line.copy()
    return lists

if __name__ == "__main__":
    with open("input.txt") as input:
        lines = input.readlines()

        lists = analyze_line(lines[0].strip("\n").split())
        print(lists)
        for history in lists:
            pass
           #print(history)