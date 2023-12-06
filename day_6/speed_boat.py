

def race_optimizer():
    with open("input.txt") as input:
        input_lines = input.readlines()

        times_txt: list[str] = input_lines[0].strip('\n').split(':')[1].strip().split()
        times = [int(speed) for speed in times_txt]

        distances_txt: list[str] = input_lines[1].strip('\n').split(':')[1].strip().split()
        distances = [int(distance) for distance in distances_txt]

        multiplied_possibilities = 1;
        for index in range(len(times)):
            possibilities = find_optimal_conditions(times[index], distances[index])
            if possibilities > 0:
                multiplied_possibilities *= possibilities

        if multiplied_possibilities == 1:
            print(0)
        print(multiplied_possibilities)


def find_optimal_conditions(time, distance_to_beat) -> int:
    possibilities = 0
    for millisecond in range(time - 1):
        charge_time = millisecond + 1
        race_time = time - charge_time
        if charge_time * race_time > distance_to_beat:
            possibilities += 1

    return possibilities

race_optimizer()
