def read_scratch_card():
    with open("input.txt") as input:
        input_lines = input.readlines()
        scratch_card_copies = {}
        max_input_lines = len(input_lines)

        for index in range(len(input_lines)):
            normalized_line: list[str] = input_lines[index].strip('\n').split(':')[1].split('|')
            winning_numbers: list[str] = normalized_line[0].strip().split()
            card_numbers: list[str] = normalized_line[1].strip().split()

            if index in scratch_card_copies:
                scratch_card_copies[index] += 1
            else:
                scratch_card_copies[index] = 1

            scratch_card_matches = evaluate_scratch_card([int(winning_number) for winning_number in winning_numbers],
                                                         [int(card_number) for card_number in card_numbers])
            print("At card: " + str(index + 1) + " // " + str(scratch_card_matches))

            for copy_index in range(scratch_card_matches):
                multiplied_card_index = index + copy_index + 1
                if multiplied_card_index < max_input_lines:
                    print("+1 for index " + str(multiplied_card_index))
                    if multiplied_card_index in scratch_card_copies:
                        scratch_card_copies[multiplied_card_index] += 1 * scratch_card_copies[index]
                    else:
                        scratch_card_copies[multiplied_card_index] = 1 * scratch_card_copies[index]

        scratch_card_total = 0
        for index in scratch_card_copies:
            print(str(index + 1) + " // " + str(scratch_card_copies[index]))
            scratch_card_total += scratch_card_copies[index]

        print(scratch_card_total)


def evaluate_scratch_card(winning_numbers: list[int], card_numbers: list[int]) -> int:
    total = 0

    for card_number in card_numbers:
        if card_number in winning_numbers:
            total += 1

    return total


read_scratch_card()
