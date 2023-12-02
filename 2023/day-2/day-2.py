with open('input.txt', 'r') as f:
    lines = f.readlines()

MAX_REDS   = 12
MAX_GREENS = 13
MAX_BLUES  = 14

output = 0

for line in lines:
    blues, reds, greens = 0, 0, 0

    game, raw_results = line.strip().split(':')
    game = int(game.split(' ')[1])
    
    results = []
    raw_results = raw_results.split(';')
    for cube_set in raw_results:
        results.extend(cube_set.strip().split(', '))

    for cubes in results:
        num = int(cubes.split(' ')[0])
        if 'red' in cubes:
            if num > reds: reds = num
        elif 'green' in cubes:
            if num > greens: greens = num
        else:
            if num > blues: blues = num

    if reds > MAX_REDS:
        continue
    if greens > MAX_GREENS:
        continue
    if blues > MAX_BLUES:
        continue

    output += game

print(f"Part 1: {output}")

output = 0

for line in lines:
    blues, reds, greens = 0, 0, 0

    game, raw_results = line.strip().split(':')
    game = int(game.split(' ')[1])
    
    results = []
    raw_results = raw_results.split(';')
    for cube_set in raw_results:
        results.extend(cube_set.strip().split(', '))

    for cubes in results:
        num = int(cubes.split(' ')[0])
        if 'red' in cubes:
            if num > reds: reds = num
        elif 'green' in cubes:
            if num > greens: greens = num
        else:
            if num > blues: blues = num

    # if reds > MAX_REDS:
    #     continue
    # if greens > MAX_GREENS:
    #     continue
    # if blues > MAX_BLUES:
    #     continue

    output += reds*greens*blues

print(f"Part 2: {output}")
