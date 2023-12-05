with open('input.txt', 'r') as f:
    lines = f.readlines()

##################
###   Part 1   ###
##################

ans = 0

for line in lines:
    line = line.strip()

    winning_nums = line.split(":")[1].split("|")[0].split(" ")
    winning_nums = list(filter(None, winning_nums))

    card_nums = line.split("|")[1].split(" ")
    card_nums = list(filter(None, card_nums))

    nb_wins = 0
    for num in winning_nums:
        if num in card_nums:
            nb_wins += 1

    if nb_wins == 0:
        continue

    ans += 1 * 2**(nb_wins - 1)

print(f"Part 1: {ans}")

##################
###   Part 2   ###
##################

additional_scratchcards = 0
card_copies = {}

for line_num, line in enumerate(lines):
    line = line.strip()

    winning_nums = line.split(":")[1].split("|")[0].split(" ")
    winning_nums = list(filter(None, winning_nums))

    card_nums = line.split("|")[1].split(" ")
    card_nums = list(filter(None, card_nums))

    nb_wins = 0
    for num in winning_nums:
        if num in card_nums:
            nb_wins += 1

    if nb_wins == 0:
        continue

    multiplier = 1
    if line_num in card_copies.keys():
        multiplier = card_copies[line_num] + 1

    additional_scratchcards += nb_wins * multiplier

    for i in range(1, nb_wins + 1):
        key = line_num + i
        if key in card_copies.keys():
            card_copies[key] += multiplier
        else:
            card_copies[key] = multiplier

print(f"Part 2: {len(lines) + additional_scratchcards}")
