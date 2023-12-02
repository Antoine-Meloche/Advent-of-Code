with open('input.txt', 'r') as f:
    lines = f.readlines()

output = 0

for line in lines:
    line = line.strip()
    line_nums = []
    for c in line:
        if c.isalpha():
            continue
        line_nums.append(c)
    output += int(f"{line_nums[0]}{line_nums[-1]}")

print(f"Part one: {output}")

word_nums = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

output = 0

for line in lines:
    line = line.strip()
    line_nums = []

    for i, c in enumerate(line):
        for word in word_nums.keys():
            if line[i:].startswith(word):
                line_nums.append(word_nums[word])
                continue
        if c.isalpha(): continue
        line_nums.append(c)
    output += int(f"{line_nums[0]}{line_nums[-1]}")

print(f"Part two: {output}")
