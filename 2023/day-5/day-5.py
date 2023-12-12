from functools import reduce

with open('input.txt', 'r') as f:
    seeds, *mappings = f.read().split('\n\n')

mappings = [mapping.strip() for mapping in mappings]
seeds = list(map(int, seeds.split(" ")[1:]))

##################
###   Part 1   ###
##################

def map_seed(start, mapping):
    for map_ in mapping.split('\n')[1:]:
        dest, src, length = map(int, map_.split(" "))

        if start in range(src, src + length):
            return dest + (start - src)
    else:
        return start

locations = [reduce(map_seed, mappings, seed) for seed in seeds]

print(f"Part 1: {min(locations)}")

##################
###   Part 2   ###
##################
