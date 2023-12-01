def unscramble():
    with open('input.txt') as scrambledInput:
        lines = scrambledInput.readlines()
        total = 0
        for line in lines:
            total += get_calibration_from_line(line)

        print(total)


def get_calibration_from_line(text: str) -> int:
    left_digit = 0
    right_digit = 0

    left = 0
    right = len(text) - 1

    while left < len(text):
        if text[left].isdigit():
            left_digit = text[left]
            break
        left += 1

    while right >= 0:
        if text[right].isdigit():
            right_digit = text[right]
            break
        right -= 1

    print(left_digit + right_digit)
    return int(left_digit + right_digit)


unscramble()
