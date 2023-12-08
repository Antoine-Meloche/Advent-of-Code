with open('input.txt', 'r') as f:
    lines = f.readlines()

##################
###   Part 1   ###
##################

card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

five_kind  = []
four_kind  = []
full_house = []
three_kind = []
two_pair   = []
one_pair   = []
high_card  = []

def calc_power(hand: str) -> list[int]:
    res = []

    for card in hand:
        res.append(card_values[card])

    return res

def sort(hand_list):
    return sorted(hand_list, key=lambda h: (h[2], h[3], h[4], h[5], h[6]))

for line in lines:
    line = line.strip()

    hand, bid = line.split(" ")
    bid = int(bid)

    lshand = len(set(hand))

    result = [hand, bid]
    power = calc_power(hand)
    result.extend(power)

    match lshand:
        case 1:
            five_kind.append(result)
        case 2:
            sorted_hand = "".join(sorted(list(hand)))

            if hand[0]*4 in sorted_hand or hand[1]*4 in sorted_hand:
                four_kind.append(result)
            else:
                full_house.append(result)

        case 3:
            sorted_hand = "".join(sorted(list(hand)))

            if hand[0]*3 in sorted_hand or hand[1]*3 in sorted_hand or hand[2]*3 in sorted_hand:
                three_kind.append(result)
            else:
                two_pair.append(result)

        case 4:
            one_pair.append(result)
        case 5:
            high_card.append(result)

ranking = []
ranking.extend(sort(high_card))
ranking.extend(sort(one_pair))
ranking.extend(sort(two_pair))
ranking.extend(sort(three_kind))
ranking.extend(sort(full_house))
ranking.extend(sort(four_kind))
ranking.extend(sort(five_kind))

ans = 0
for i, hand in enumerate(ranking):
    ans += hand[1] * (i + 1)

print(f"Part 1: {ans}")

##################
###   Part 2   ###
##################

card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14,
}

five_kind  = []
four_kind  = []
full_house = []
three_kind = []
two_pair   = []
one_pair   = []
high_card  = []

hand_types = {
   "five_kind": 6,
   "four_kind": 5,
   "full_house": 4,
   "three_kind": 3,
   "two_pair": 2,
   "one_pair": 1,
   "high_card": 0
}

def force_hand(hand: str) -> int:
    hand_no_j = hand.replace('J', '')
    ilevel = max([hand_no_j.count(c) for c in hand_no_j])

    llevel = ilevel + hand.count('J')

    if llevel >= 4:
        return llevel + 1

    if llevel == 2:
        return 1

    if llevel == 3:
        if len(set(hand)) == 3:
            return 4
        return 3

    print('never?')



for line in lines:
    line = line.strip()

    hand, bid = line.split(" ")
    bid = int(bid)

    lshand = len(set(hand))

    result = [hand, bid]
    power = calc_power(hand)
    result.extend(power)

    match lshand:
        case 1:
            five_kind.append(result)

        case 2:
            if 'J' in hand:
                five_kind.append(result)

            else:
                sorted_hand = "".join(sorted(list(hand)))

                if hand[0]*4 in sorted_hand or hand[1]*4 in sorted_hand:
                    four_kind.append(result)
                else:
                    full_house.append(result)

        case 3:
            if 'J' in hand:
                level = force_hand(hand)

                match level:
                    case 3:
                        three_kind.append(result)
                    case 4:
                        full_house.append(result)
                    case 5:
                        four_kind.append(result)
                    case 6:
                        five_kind.append(result)

            else:
                sorted_hand = "".join(sorted(list(hand)))

                if hand[0]*3 in sorted_hand or hand[1]*3 in sorted_hand or hand[2]*3 in sorted_hand:
                    three_kind.append(result)
                else:
                    two_pair.append(result)

        case 4:
            if 'J' in hand:
                level = force_hand(hand)

                match level:
                    case 2:
                        print('never?')
                        two_pair.append(result)
                    case 3:
                        three_kind.append(result)
                    case 4:
                        full_house.append(result)
                    case 5:
                        four_kind.append(result)
                    case 6:
                        five_kind.append(result)

            else:
                one_pair.append(result)

        case 5:
            if 'J' in hand:
                level = force_hand(hand)

                match level:
                    case 1:
                        one_pair.append(result)
                    case 2:
                        print('never?')
                        two_pair.append(result)
                    case 3:
                        three_kind.append(result)
                    case 4:
                        full_house.append(result)
                    case 5:
                        four_kind.append(result)
                    case 6:
                        five_kind.append(result)
            else:
                high_card.append(result)

ranking = []
ranking.extend(sort(high_card))
ranking.extend(sort(one_pair))
ranking.extend(sort(two_pair))
ranking.extend(sort(three_kind))
ranking.extend(sort(full_house))
ranking.extend(sort(four_kind))
ranking.extend(sort(five_kind))

ans = 0
for i, hand in enumerate(ranking):
    ans += hand[1] * (i + 1)

print(f"Part 2: {ans}")
