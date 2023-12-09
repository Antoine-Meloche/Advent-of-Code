with open('input.txt', 'r') as f:
    lines = f.readlines()

##################
###   Part 1   ###
##################

def all_zeros(level) -> bool:
    if level == [0]*len(level):
        return True
    return False

prevs = []
nexts = []

for line in lines:
    line = line.strip()
    nums = map(int, filter(None, line.split(" ")))

    levels = [list(nums)]
    while not all_zeros(levels[-1]):
        level = []
        for i in range(0, len(levels[-1]) - 1):
            level.append(levels[-1][i+1] - levels[-1][i])
        levels.append(level)

    next = 0

    for level in levels[::-1][1:]:
        next += level[-1]

    nexts.append(next)
    
    ##################
    ###   Part 1   ###
    ##################
    
    prev = 0

    for level in levels[::-1][1:]:
        prev = level[0] - prev

    prevs.append(prev)

print(f"Part 1: {sum(nexts)}")

print(f"Part 2: {sum(prevs)}")
