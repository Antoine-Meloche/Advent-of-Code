with open('input.txt', 'r') as f:
    lines = f.readlines()

##################
###   Part 1   ###
##################

def is_symbol(char: str) -> bool:
    if char == '.':
        return False

    if char.isdigit():
        return False

    return True

def find_adj_sym(num: str, start_i: int, start_j: int) -> bool:
    for i in range(start_i-1, start_i+2):
        if i < 0 or i >= len(lines):
            continue

        end_j = start_j + len(num) + 1
        j = start_j - 1

        if j < 0:
            j = 0

        if end_j >= len(lines[i]):
            end_j = len(lines[i]) - 1

        adjacent = lines[i][j:end_j]
        for char in adjacent.replace('.', ''):
            if is_symbol(char):
                return True
    return False

ans = 0

for i, line in enumerate(lines):
    start_i = i
    start_j = 0
    tracking_num = False
    num = ""
    for j, char in enumerate(line):
        if char.isdigit():
            if not tracking_num:
                start_j = j
                tracking_num = True
            num += char
        elif tracking_num:
            if find_adj_sym(num, start_i, start_j):
                ans += int(num)
            tracking_num = False
            num = ""

print(f"Part 1: {ans}")

##################
###   Part 2   ###
##################

ans = 0

def check_gear(start_i: int, start_j: int) -> list[tuple[int, int]]:
    nb_nums = 0
    nums = []
    for i in range(start_i-1, start_i+2):
        if i < 0 or i >= len(lines):
            continue

        tracking_num = False

        adjacent = lines[i][start_j-1:start_j+2]
        for j, char in enumerate(adjacent):
            if char.isdigit():
                if not tracking_num:
                    nb_nums += 1
                    nums.append((i, j+start_j-1))
                    tracking_num = True
            elif tracking_num:
                tracking_num = False

    if nb_nums == 2:
        return nums

    return []

def find_num(i: int, start_j: int):
    num = lines[i][start_j]

    j = start_j
    while True:
        j += 1
        if not lines[i][j].isdigit():
            break
        num += lines[i][j]

    j = start_j
    while True:
        j -= 1
        if not lines[i][j].isdigit():
            break
        num = lines[i][j] + num

    return num

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == '*':
            gear = check_gear(i, j)
            if gear:
                num1 = find_num(gear[0][0], gear[0][1])
                num2 = find_num(gear[1][0], gear[1][1])
                ans += int(num1) * int(num2)

print(f"Part 2: {ans}")
