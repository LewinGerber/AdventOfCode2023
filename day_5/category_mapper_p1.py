def map_seed_to_location():
    with open("input.txt") as input:
        input_lines = input.readlines()
        mappers: list[dict] = []

        for line in input_lines[1:]:
            if line != '\n':
                if "map:" in line:
                    # create mew dictionary
                    mappers.append({})
                else:
                    mappers[len(mappers) - 1] = extend_dict_by_instruction(mappers[len(mappers) - 1], line.strip('\n'))


        # resolve mappers
        seeds: list[str] = input_lines[0].split(':')[1].strip().split()
        #for mapper in mappers:
        #    print(mapper)
        # print("<< SEEDS >>")

        locations: list[int] = []
        for seed in seeds:
            current_mapped_value = int(seed)
            for mapper in mappers:
                if current_mapped_value in mapper.keys():
                    current_mapped_value = mapper[current_mapped_value]
            locations.append(current_mapped_value)
            print(current_mapped_value)
        print("MIN: " + str(min(locations)))




def extend_dict_by_instruction(mapper: dict, instruction: str) -> dict:
    instruction_parts = instruction.split()
    destination_range_start = int(instruction_parts[0])
    key_range_start = int(instruction_parts[1])
    range_size = int(instruction_parts[2])

    for index in range(range_size):
        mapper[key_range_start + index] = destination_range_start + index

    return mapper


map_seed_to_location()
