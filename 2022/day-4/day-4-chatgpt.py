input = open('day-4.input', 'r').readlines()

# parse the input to extract the range of section IDs for each pair of Elves
pairs = []
for line in input:
  # extract the start and end of the range for each Elf
  elf1, elf2 = line.split(",")
  start1, end1 = map(int, elf1.split("-"))
  start2, end2 = map(int, elf2.split("-"))
  # store the range for each Elf in the pair
  pairs.append([(start1, end1), (start2, end2)])

# iterate over the pairs and check if one range fully contains the other
count = 0
for pair in pairs:
  # get the range for each Elf in the pair
  range1, range2 = pair
  start1, end1 = range1
  start2, end2 = range2
  # check if one range fully contains the other
  if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
    # increment the counter
    count += 1

# print the number of pairs that have one range fully containing the other
print(count)

###############
##  Part Two ##
###############

# parse the input to extract the range of section IDs for each pair of Elves
pairs = []
for line in input:
  # extract the start and end of the range for each Elf
  elf1, elf2 = line.split(",")
  start1, end1 = map(int, elf1.split("-"))
  start2, end2 = map(int, elf2.split("-"))
  # store the range for each Elf in the pair
  pairs.append([(start1, end1), (start2, end2)])

# iterate over the pairs and check if the ranges overlap
count = 0
for pair in pairs:
  # get the range for each Elf in the pair
  range1, range2 = pair
  start1, end1 = range1
  start2, end2 = range2
  # check if the ranges overlap
  if end1 >= start2 and end2 >= start1:
    # increment the counter
    count += 1

# print the number of pairs that have overlapping ranges
print(count)
