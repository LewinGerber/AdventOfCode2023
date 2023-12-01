def unscramble():
    with open('input.txt') as scrambledInput:
        lines = scrambledInput.readlines()
        total = 0
        for line in lines:
            total += get_calibration_from_line(line.rstrip('\n'))

        print(total)


def get_calibration_from_line(text: str) -> int:
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    left_digit = '0'
    right_digit = '0'

    left_buffer = '______'
    right_buffer = '____'

    left = 0
    right = len(text) - 1

    while left < len(text):
        if text[left].isdigit():
            left_digit = text[left]
            break
        left_buffer += text[left]

        if len(left_buffer) > 5:
            left_buffer = left_buffer[1:]

        if len(left_buffer) > 2:
            length = len(left_buffer)
            result_1 = numbers.get(left_buffer[:length - 2])
            result_2 = numbers.get(left_buffer[1:length - 1])
            result_3 = numbers.get(left_buffer[3:])
            result_4 = numbers.get(left_buffer[:length - 1])
            result_5 = numbers.get(left_buffer[2:])
            # print(left_buffer + ' >> ' + left_buffer[1:])
            result_6 = numbers.get(left_buffer[1:])
            # print(left_buffer + ' >> ' + left_buffer[1:])
            # print(numbers.get(left_buffer))

            if result_1:
                left_digit = result_1
                break

            if result_2:
                left_digit = result_2
                break

            if result_3:
                left_digit = result_3
                break

            if result_4:
                left_digit = result_4
                break

            if result_5:
                left_digit = result_5
                break

            if result_6:
                left_digit = result_6
                break

        # print(left_buffer)
        left += 1

    while right >= 0:
        if text[right].isdigit():
            right_digit = text[right]
            break

        right_buffer = text[right] + right_buffer

        if len(right_buffer) > 5:
            # print(right_buffer + ' >> ' + right_buffer[:len(right_buffer) - 1])
            right_buffer = right_buffer[:len(right_buffer) - 1]
            # print(right_buffer)

        if len(right_buffer) > 2:
            length = len(right_buffer)
            result_1 = numbers.get(right_buffer[:length - 2])
            result_2 = numbers.get(right_buffer[1:length - 1])
            result_3 = numbers.get(right_buffer[2:])
            result_4 = numbers.get(right_buffer[:length - 1])
            result_5 = numbers.get(right_buffer[1:])
            result_6 = numbers.get(right_buffer)

            if result_1:
                right_digit = result_1
                break

            if result_2:
                right_digit = result_2
                break

            if result_3:
                right_digit = result_3
                break

            if result_4:
                right_digit = result_4
                break

            if result_5:
                right_digit = result_5
                break

            if result_6:
                right_digit = result_6
                break

        right -= 1

    print(left_digit + right_digit)
    return int(str(left_digit) + str(right_digit))


unscramble()
