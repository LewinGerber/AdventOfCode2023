

def race_optimizer():
    with open("input.txt") as input:
        input_lines = input.readlines()

        time = int(input_lines[0].strip('\n').split(':')[1].strip().replace(" ", ""))
        distance = int(input_lines[1].strip('\n').split(':')[1].strip().replace(" ", ""))

        print(find_optimal_conditions(time, distance))


def find_optimal_conditions(time, distance_to_beat) -> int:
    possibilities = 0
    for millisecond in range(time - 1):
        charge_time = millisecond + 1
        race_time = time - charge_time
        if charge_time * race_time > distance_to_beat:
            possibilities += 1

    return possibilities

race_optimizer()
