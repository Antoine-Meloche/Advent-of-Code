with open('input.txt', 'r') as f:
    lines = f.readlines()

##################
###   Part 1   ###
##################

race_times = list(map(int, filter(None, lines[0].strip().split(" ")[1:])))
race_dists = list(map(int, filter(None, lines[1].strip().split(" ")[1:])))

races = zip(race_times, race_dists)

ans = 1

for race_time, race_dist in races:
    ways_to_beat = 0

    for time in range(race_time):
        speed = time
        moving_time = race_time - time

        if speed * moving_time > race_dist:
            ways_to_beat += 1

    ans *= ways_to_beat

print(f"Part 1: {ans}")

##################
###   Part 2   ###
##################

race_time = int(lines[0].strip().split(":")[1].replace(" ", ""))
race_dist = int(lines[1].strip().split(":")[1].replace(" ", ""))

start_beat = 0

for time in range(race_time):
    speed = time
    moving_time = race_time - time

    if speed * moving_time > race_dist:
        start_beat = time
        break

print(f"Part 2: {race_time - (start_beat * 2) + 1}")
