import itertools, copy
import numpy as np

moons = np.array([[(-7, 17, -11), (0, 0, 0)], [(9, 12, 5), (0, 0, 0)], [(-9, 0, -4), (0, 0, 0)], [(4, 6, 0), (0, 0, 0)]])
print(moons)
# moons={
#     'Io': {
#         'x': -7,
#         'y': 17,
#         'z': -11,
#         'vx': 0,
#         'vy': 0,
#         'vz': 0
#     },
#     'Europa': {
#         'x': 9,
#         'y': 12,
#         'z': 5,
#         'vx': 0,
#         'vy': 0,
#         'vz': 0
#     },
#     'Ganymede': {
#         'x': -9,
#         'y': 0,
#         'z': -4,
#         'vx': 0,
#         'vy': 0,
#         'vz': 0
#     },
#     'Callisto': {
#         'x': 4,
#         'y': 6,
#         'z': 0,
#         'vx': 0,
#         'vy': 0,
#         'vz': 0
#     }
# }

original: np.array = copy.deepcopy(moons)

def revolution() -> bool:
    if moons is not original:
        return False
    return True

def simulate(steps: int, part: int, moons: np.array):
    i: int = 0

    permutations = list(itertools.permutations(moons, r=2))

    while (i < steps and part == 1) or part == 2:
        for moon_0, moon_1 in permutations:
            for c in np.arange(3):
                if moon_0[0][c] < moon_1[0][c]:
                    moon_0[1][c] += 1
                elif moon_0[0][c] > moon_1[0][c]:
                    moon_0[1][c] -= 1
            
        # for moon in moons:
        #     for c in np.arange(3):
        #         moon[0][c] += moon[1][c]
        

        i += 1
        
        if revolution():
            break
    
    if part == 2:
        return i


simulate(1000, 1, moons)

energy: int = 0
for moon in moons:
    pot: int = sum(map(abs, moon[0]))
    kin: int = sum(map(abs, moon[1]))
    
    energy += np.multiply(pot, kin)

print(f'Part One: {energy}')

moons = copy.deepcopy(original)
steps: int = simulate(0, 2, moons)
print(f'Part Two: {steps}')
print(moons)