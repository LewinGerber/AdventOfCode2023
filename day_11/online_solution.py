with open("input.txt", "r") as file:
    galaxy_map = [list(line) for line in file.read().splitlines()]

empty_rows = [i for i, row in enumerate(
    galaxy_map) if all(char == '.' for char in row)]

empty_cols = [i for i, col in enumerate(zip(*galaxy_map)) if all(
    char == '.' for char in col)]

galaxies = [(row, col) for row, line in enumerate(galaxy_map)
            for col, char in enumerate(line) if char == '#']

total_distance = 0
for i, (galaxy_row, galaxy_col) in enumerate(galaxies):
    for (other_galaxy_row, other_galaxy_col) in galaxies[:i]:
        for row in range(min(other_galaxy_row, galaxy_row), max(other_galaxy_row, galaxy_row)):
            total_distance += 2 if row in empty_rows else 1

        for col in range(min(other_galaxy_col, galaxy_col), max(other_galaxy_col, galaxy_col)):
            total_distance += 2 if col in empty_cols else 1

print(total_distance)