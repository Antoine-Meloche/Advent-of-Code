with open('day-4.input', 'r') as f:
    lines = f.readlines()
    total_overlaps = 0
    for line in lines:
        section1 = line.strip().split(',')[0]
        section2 = line.strip().split(',')[1]

        range1 = range(int(section1.split('-')[0]), int(section1.split('-')[1])+1)
        range2 = range(int(section2.split('-')[0]), int(section2.split('-')[1])+1)

        if (range1[0] in range2 and range1[-1] in range2) or (range2[0] in range1 and range2[-1] in range1):
            total_overlaps += 1

    print(total_overlaps)

################
##  Part Two  ##
################

with open('day-4.input', 'r') as f:
    lines = f.readlines()
    overlaps = 0
    for line in lines:
        section1 = line.strip().split(',')[0]
        section2 = line.strip().split(',')[1]

        range1 = range(int(section1.split('-')[0]), int(section1.split('-')[1])+1)
        range2 = range(int(section2.split('-')[0]), int(section2.split('-')[1])+1)

        if set(range1).intersection(range2):
            overlaps += 1

    print(overlaps)
