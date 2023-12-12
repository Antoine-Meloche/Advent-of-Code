with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

##################
###   Part 1   ###
##################

from itertools import combinations
from math import sqrt

add_rows = []

for row, line in enumerate(lines):
    if '#' not in line:
        add_rows.append(row)

for i, add_row in enumerate(add_rows):
    lines.insert(add_row + i, '.' * len(lines[0]))

add_cols = []

for col in range(len(lines[0])):
    for line in lines:
        if line[col] == '#':
            break
    else:
        add_cols.append(col)

for i, add_col in enumerate(add_cols):
    for row in range(len(lines)):
        line = list(lines[row])
        line.insert(add_col + i, '.')
        lines[row] = ''.join(line)

galaxies = []

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '#':
            galaxies.append((row, col))

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
]

def distance(start: tuple[int, int], end: tuple[int, int]):
    return sqrt((start[1] - end[1]) ** 2 + (start[0] - end[0]) ** 2)

def shortest_path(start: tuple[int, int], end: tuple[int, int]):
    path = set()
    pos = start

    while pos != end:
        closest_dir_dist = float('inf')
        closest_pos = (0, 0)

        for dir in directions:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            dist = distance(new_pos, end)
            if dist < closest_dir_dist:
                closest_dir_dist = dist
                closest_pos = new_pos

        pos = closest_pos
        path.add(pos)

    return path

def fast_short_dist(start: tuple[int, int], end: tuple[int, int], expansion_multiplier: int = 0, empty_rows: list[int] = [], empty_cols: list[int] = []) -> int:
    dist_no_expansion = abs(start[0] - end[0]) + abs(start[1] - end[1])
    if not expansion_multiplier:
        return dist_no_expansion

    minmax_rows = sorted((start[0], end[0]))
    minmax_cols = sorted((start[1], end[1]))

    expansions = 0

    for row in range(*minmax_rows):
        if row in empty_rows:
            expansions += 1
    for col in range(*minmax_cols):
        if col in empty_cols:
            expansions += 1

    final_dist = dist_no_expansion + expansions * expansion_multiplier
    return final_dist

galaxy_pairs = combinations(galaxies, 2)

total = 0

for start, end in galaxy_pairs:
    # path = shortest_path(start, end)
    # total += len(path)
    shortest_distance = fast_short_dist(start, end)
    total += shortest_distance

print(f"Part 1: {total}")

##################
###   Part 2   ###
##################

with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def find_expansions(lines: list[str]) -> list[list[int]]:
    add_rows = []
    for row, line in enumerate(lines):
        if '#' not in line:
            add_rows.append(row)

    add_cols = []
    for col in range(len(lines[0])):
        for line in lines:
            if line[col] == '#':
                break
        else:
            add_cols.append(col)

    return add_rows, add_cols

expanded_rows, expanded_cols = find_expansions(lines)

galaxies = []

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '#':
            galaxies.append((row, col))

galaxy_pairs = combinations(galaxies, 2)

total = 0
for start, end in galaxy_pairs:
    shortest_distance = fast_short_dist(start, end, 999_999, expanded_rows, expanded_cols)
    total += shortest_distance

print(f"Part 2: {total}")
