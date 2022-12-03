with open("day-1.input", "r") as f:
    lines = f.readlines()
    i = 0
    top_cal = 0
    top_elf = 0
    elf = 0
    while i < len(lines):
        line = 0
        calories = 0
        while line != None:
            calories += int(line)
            try:
                line = int(lines[i].strip())
            except ValueError:
                line = None
            i += 1
            if i == len(lines):
                break
        elf += 1
        if calories > top_cal:
            top_cal = calories
            top_elf = i
print(top_cal)

##############
#  Part Two  #
##############

with open("day-1.input", "r") as f:
    lines = f.readlines()
    i = 0
    top_cal = [0, 0, 0]
    while i < len(lines):
        line = 0
        calories = 0
        while line != None:
            calories += line
            try:
                line = int(lines[i].strip())
            except ValueError:
                line = None
            i += 1
            if i == len(lines):
                break

        if calories > min(top_cal):
            top_cal[top_cal.index(min(top_cal))] = calories
print(sum(top_cal))
