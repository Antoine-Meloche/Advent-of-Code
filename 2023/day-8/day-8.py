with open('input.txt', 'r') as f:
    lines = f.readlines()

##################
###   Part 1   ###
##################

instructions = lines[0].strip()

mappings = {}

for line in lines[2:]:
    line = line.strip()
    
    pos = line.split(" ")[0]
    mapping = line.split("=")[1][2:-1].split(", ")

    mappings[pos] = mapping

position = "AAA"

counter = 0
steps = 0

while position != "ZZZ":
    if instructions[counter] == 'R':
        position = mappings[position][1]
    else:
        position = mappings[position][0]

    steps += 1
    counter += 1
    
    if counter == len(instructions):
        counter = 0

print(f"Part 1: {steps}")


##################
###   Part 2   ###
##################

from math import lcm

positions = []
for mapping in mappings.keys():
    if mapping[-1] == 'A':
        positions.append(mapping)

solved = []

for i, pos in enumerate(positions):
    steps = 0
    counter = 0
    while positions[i][-1] != "Z":
        if instructions[counter] == 'R':
            positions[i] = mappings[positions[i]][1]
        else:
            positions[i] = mappings[positions[i]][0]

        steps += 1
        counter += 1
        
        if counter == len(instructions):
            counter = 0

    solved.append(steps)

steps = lcm(*map(int, solved))

print(f"Part 2: {steps}")
