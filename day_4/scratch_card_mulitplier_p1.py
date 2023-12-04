import re


def read_scratch_card():
    with open("input.txt") as input:
        scratch_card_total = 0
        for line in input.readlines():
            normalized_line: list[str] = line.strip('\n').split(':')[1].split('|')
            winning_numbers: list[str] = normalized_line[0].strip().split()
            card_numbers: list[str] = normalized_line[1].strip().split()
            scratch_card_total += evaluate_scratch_card([int(winning_number) for winning_number in winning_numbers],
                                                        [int(card_number) for card_number in card_numbers])

        print(scratch_card_total)


def evaluate_scratch_card(winning_numbers: list[int], card_numbers: list[int]) -> int:
    has_at_least_one = False
    total = 1

    for card_number in card_numbers:
        if card_number in winning_numbers:
            if not has_at_least_one:
                has_at_least_one = True
            else:
                total *= 2

    if has_at_least_one:
        return total
    return 0


read_scratch_card()
