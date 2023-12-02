import re

maximum_red_allowed = 12
maximum_green_allowed = 13
maximum_blue_allowed = 14

def find_possible_moves():
    with open("input.txt") as input:
        sum_of_powersets = 0

        for line in input.readlines():
            split_line = line.split(':')
            normalized_line = split_line[1].strip('\n')
            sum_of_powersets += powerset_of_minimum_occurence(normalized_line)

        print(sum_of_powersets)

def powerset_of_minimum_occurence(game_input: str) -> int:
    red = 0
    green = 0
    blue = 0

    values = re.split(', |; ', game_input.strip())
    for value in values:
        quantity = value.split(' ')[0]
        color = value.split(' ')[1]
        if color == 'red':
            red = max(red, int(quantity))
        elif color == 'green':
            green = max(green, int(quantity))
        elif color == 'blue':
            blue = max(blue, int(quantity))

    return red * green * blue

find_possible_moves()
