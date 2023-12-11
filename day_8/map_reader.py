import re


def parse_node_string_to_node(nodes: list[str]) -> {}:
    parsed_nodes = {}
    for node in nodes:
        normalized_node = re.sub(r'[=(),]', '', node)
        node_parts = re.sub(r'\s+', ' ', normalized_node).split(" ")
        parsed_nodes[node_parts[0]] = [node_parts[1], node_parts[2]]
    return parsed_nodes

def execute_instructions(instruction: list[str], nodes: {}) -> int:
    steps = 0
    current_node_key: str = "AAA"

    while True:
        current_instruction = instruction[steps % len(instruction)]
        current_side = 1 if current_instruction == "R" else 0
        current_value = nodes[current_node_key][current_side]
        #print(f"{current_value} / {steps} % {len(instructions)} = {current_instruction}")
        if current_value == "ZZZ":
            return steps + 1
        steps += 1

        current_node_key = current_value



if __name__ == "__main__":
    with open("./input.txt") as input:
        lines = input.readlines()
        instructions = list(lines[0].strip("\n"))
        nodes_as_dict = parse_node_string_to_node(lines[2:])
        number_steps = execute_instructions(instructions, nodes_as_dict)
        print(number_steps)
