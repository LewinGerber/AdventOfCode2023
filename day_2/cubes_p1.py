import re

maximum_red_allowed = 12
maximum_green_allowed = 13
maximum_blue_allowed = 14

def find_possible_moves():
    with open("input.txt") as input:
        sum_of_valid_moves = 0

        for line in input.readlines():
            split_line = line.split(':')
            game_number = int(split_line[0].split(' ')[1])
            normalized_line = split_line[1].strip('\n')

            if is_largest_below_maximum(normalized_line):
                sum_of_valid_moves += game_number

        print(sum_of_valid_moves)

def is_largest_below_maximum(game_input: str) -> bool:
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

    if red > maximum_red_allowed or green > maximum_green_allowed or blue > maximum_blue_allowed:
        print(f"Red: {red}, Green: {green}, Blue: {blue} - INVALID")
        return False
    print(f"Red: {red}, Green: {green}, Blue: {blue} - VALID")
    return True

find_possible_moves()
