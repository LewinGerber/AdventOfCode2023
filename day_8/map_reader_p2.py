import re


def parse_node_string_to_node(nodes: list[str]) -> {}:
    parsed_nodes = {}
    for node in nodes:
        normalized_node = re.sub(r'[=(),]', '', node)
        node_parts = re.sub(r'\s+', ' ', normalized_node).split(" ")
        parsed_nodes[node_parts[0]] = [node_parts[1], node_parts[2]]
    return parsed_nodes


def execute_instructions(instruction: list[str], nodes: {}, start_key, already_performed_steps) -> bool:
    steps = 0
    current_node_key: str = start_key

    while steps <= already_performed_steps + 1:
        print(f"executing for {start_key}, step: {steps} <= {already_performed_steps}")

        current_side = 1 if instruction[steps % len(instruction)] == "R" else 0
        current_node_key = nodes[current_node_key][current_side]

        steps += 1

    if current_node_key.endswith("Z"):
        return True
    return False


def find_starting_points(nodes: {}) -> list[str]:
    keys_ending_with_a = []
    for key in nodes.keys():
        if key.endswith("A"):
            keys_ending_with_a.append(key)
    return keys_ending_with_a


if __name__ == "__main__":
    with (open("./input.txt") as input):
        lines = input.readlines()
        instructions = list(lines[0].strip("\n"))
        nodes_as_dict = parse_node_string_to_node(lines[2:])
        starting_points = find_starting_points(nodes_as_dict)

        are_all_on_z = False
        steps_made = 0
        while not are_all_on_z:
            are_all_on_z = True

            for starting_point in starting_points:
                are_all_on_z = (are_all_on_z and execute_instructions(instructions, nodes_as_dict, starting_point,
                                                                     steps_made))
            steps_made += 1

        print(steps_made)
