import re
import math


def calculate_energy(moons: list) -> int: return sum([sum(map(abs, moon.pos)) * sum(map(abs, moon.vel)) for moon in moons])


def set_moons():
    global moons
    moons = list(map(Moon, moons_coords))


class Moon:
    def __init__(self: object, coords: list) -> None:
        self.pos: list = list(map(int, coords))
        self.vel: list = [0] * 3


with open('input', "r") as f:
    moons_coords: list = [line.strip("\n<>") for line in f.readlines()]
    moons_coords = [re.findall(r"x=(-?\d+), y=(-?\d+), z=(-?\d+)", moon_coords)[0] for moon_coords in moons_coords]

def simulate(steps: int, part: int) -> None:
    set_moons()
    i = 0

    while (i < steps and part == 1) or part == 2:
        for moon in moons:
            for moon_1 in moons:
                for d in range(3):
                    if moon.pos[d] < moon_1.pos[d]:
                        moon.vel[d] += 1
                    elif moon.pos[d] > moon_1.pos[d]:
                        moon.vel[d] += -1

        for moon in moons:
            for d in range(3):
                moon.pos[d] += moon.vel[d]

        if part == 1:
            i += 1
            continue

        x = ((moons[0].pos[0], moons[0].vel[0]), (moons[1].pos[0], moons[1].vel[0]), (moons[2].pos[0], moons[2].vel[0]))
        y = ((moons[0].pos[1], moons[0].vel[1]), (moons[1].pos[1], moons[1].vel[1]), (moons[2].pos[1], moons[2].vel[1]))
        z = ((moons[0].pos[2], moons[0].vel[2]), (moons[1].pos[2], moons[1].vel[2]), (moons[2].pos[2], moons[2].vel[2]))


        if x in xs and y in ys and z in zs:
            break

        xs.add(x)
        ys.add(y)
        zs.add(z)

simulate(1000, 1)
print(f"12.1 Energy: {calculate_energy(moons)}")

xs, ys, zs = set(), set(), set()

simulate(0, 2)
iterations = math.lcm(len(xs), math.lcm(len(ys), len(zs)))

print(f"12.2 Iterations: {iterations}")