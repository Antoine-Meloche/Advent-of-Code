with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

##################
###   Part 1   ###
##################

pipes = "|-LJ7F"

pipe_direction_mapping = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1 ,0), (0, 1)],
}

for i, line in enumerate(lines):
    if 'S' in line:
        start = (i, line.index('S'))

def find_direction(current_direction: tuple[int, int], pos: tuple[int, int]) -> tuple[int, int]:
    char = lines[pos[0]][pos[1]]

    if char == 'S':
        return

    for dir_choice in pipe_direction_mapping[char]:
        if -dir_choice[0] == current_direction[0] or -dir_choice[1] == current_direction[1]:
            pass
        else:
            return dir_choice

def starting_direction(start: tuple[int, int]):
    for dir_offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        pos = (start[0] + dir_offset[0], start[1] + dir_offset[1])

        if pos[0] >= len(lines) or pos[1] >= len(lines[pos[0]]):
            continue

        if pos[0] < 0 or pos[1] < 0:
            continue

        char = lines[pos[0]][pos[1]]

        if char not in pipes:
            continue

        for dir_choice in pipe_direction_mapping[char]:
            if pos[0] + dir_choice[0] != start[0] or pos[1] + dir_choice[1] != start[1]:
                continue

            return (-dir_choice[0], -dir_choice[1])

def find_loop(start: tuple[int, int]) -> int:
    path = []
    pos = start

    direction = starting_direction(start)

    while pos[0] != start[0] or pos[1] != start[1] or not len(path):
        pos = (pos[0] + direction[0], pos[1] + direction[1])
        next_direction = find_direction(direction, pos)

        if next_direction:
            direction = next_direction

        path.append(pos)

    return path

path = find_loop(start)

print(f"Part 1: {len(path) // 2}")

##################
###   Part 2   ###
##################
