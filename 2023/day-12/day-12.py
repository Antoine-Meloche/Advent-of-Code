with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

gear_sets  = [line.split(" ")[0] for line in lines]
groups = [list(map(int, line.split(" ")[1].split(","))) for line in lines]

##################
###   Part 1   ###
##################

def count_groups(gears: str) -> list[int]:
    groups = []

    group_count = 0
    prev_gear = ''

    for i, gear in enumerate(gears):
        if gear == '.':
            if prev_gear == '#':
                groups.append(group_count)
                group_count = 0
        else:
            group_count += 1
            if i == len(gears) - 1:
                groups.append(group_count)

        prev_gear = gear

    return groups

from itertools import product

arrangements = 0

for i, gear_set in enumerate(gear_sets):
    unknowns = gear_set.count('?')

    unknowns_possibilities = product('#.', repeat=unknowns)
    for possibility in unknowns_possibilities:
        test_gear_set = gear_set

        for gear in possibility:
            test_gear_set = test_gear_set.replace('?', gear, 1)

        test_groups_count = count_groups(test_gear_set)
        if test_groups_count == groups[i]:
            arrangements += 1


print(f"Part 1: {arrangements}")
