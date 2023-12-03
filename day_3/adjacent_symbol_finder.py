import re

def add_number_with_adjacent_symbol():
    with open("input.txt") as input:
        lines = input.readlines()
        sum_of_numbers = 0

        for line_index in range(len(lines)):
            if line_index == 0 and line_index <= len(lines) - 1:
                sum_of_numbers += find_numbers_with_adjacent_symbol(lines[line_index].strip('\n'),
                                                                    lines[line_index].strip('\n'),
                                                                    lines[line_index + 1].strip('\n'))
            elif line_index == len(lines) - 1:
                sum_of_numbers += find_numbers_with_adjacent_symbol(lines[line_index - 1].strip('\n'),
                                                                    lines[line_index].strip('\n'),
                                                                    lines[line_index].strip('\n'))
            else:
                sum_of_numbers += find_numbers_with_adjacent_symbol(lines[line_index - 1].strip('\n'),
                                                                    lines[line_index].strip('\n'),
                                                                    lines[line_index + 1].strip('\n'))

        print(sum_of_numbers)


def find_numbers_with_adjacent_symbol(previous_row: str, current_row: str, next_row: str) -> int:
    is_valid_number = False
    current_number = ''

    sum_for_row = 0
    for char_index in range(len(current_row)):
        char = current_row[char_index]

        if char.isdigit():
            current_number += char

            if len(previous_row) == len(current_row) == len(next_row):
                if is_special_char(previous_row[char_index]) or is_special_char(next_row[char_index]):
                    is_valid_number = True
                # END
                elif char_index < len(current_row) - 1 and (
                        is_special_char(previous_row[char_index + 1]) or is_special_char(
                        current_row[char_index + 1]) or is_special_char(next_row[char_index + 1])):
                    is_valid_number = True
                # START
                elif char_index > 0 and (is_special_char(previous_row[char_index - 1]) or is_special_char(
                        current_row[char_index - 1]) or is_special_char(next_row[char_index - 1])):
                    is_valid_number = True
            else:
                print("could not parse input")
        else:
            if is_valid_number:
                print("finishing number; " + str(current_number))
                sum_for_row += int(current_number)
            current_number = ''
            is_valid_number = False

    return sum_for_row


pattern = re.compile("[^0-9.]")
def is_special_char(char: str):
    return pattern.match(char)


add_number_with_adjacent_symbol()
