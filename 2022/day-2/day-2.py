score_card = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3
}

losses = ['AZ', 'BX', 'CY']

with open('day-2.input', 'r') as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        oponnent, you = line.strip().split(' ')
        if score_card[oponnent] == score_card[you]:
            score += 3
        elif oponnent+you not in losses:
            score += 6
        score += score_card[you]

    print(score)


################
##  Part Two  ##
################

wins = {
        'A': 2,
        'B': 3,
        'C': 1
        }
losses = {
        'A': 3,
        'B': 1,
        'C': 2
        }
ties = {
        'A': 1,
        'B': 2,
        'C': 3
        }

with open('day-2.input', 'r') as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        oponnent, result = line.strip().split(' ')
        if result == 'X':
            score += losses[oponnent]
        elif result == 'Y':
            score += ties[oponnent]
            score += 3
        elif result == 'Z':
            score += wins[oponnent]
            score += 6
    print(score)
