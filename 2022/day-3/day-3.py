priorities = "abcdefghijklmnopqrstuvwxyz"

with open('day-3.input', 'r') as f:
    lines = f.readlines()
    total = 0
    for line in lines:
        items_in_compartment = len(line) // 2
        compartment_1 = line[:items_in_compartment]
        compartment_2 = line[items_in_compartment:]
        for letter in compartment_1:
            if letter in compartment_2:
                total += priorities.index(letter.lower())+(27 if letter.isupper() else 1)
                break
    print(total)

################
##  Part Two  ##
################

with open('day-3.input', 'r') as f:
    lines = f.readlines()
    total = 0
    for i in range(0,len(lines),3):
        sack_1 = lines[i]
        sack_2 = lines[i+1]
        sack_3 = lines[i+2]
        for letter in sack_1:
            if letter in sack_2 and letter in sack_3:
                total += priorities.index(letter.lower())+(27 if letter.isupper() else 1)
                break
    print(total)
