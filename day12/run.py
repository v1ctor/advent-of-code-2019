import sys
import re
import functools 

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(numbers):
    return functools.reduce(lcm, numbers)


def gravity(x, y):
    if x == y:
        return 0
    if x > y:
        return -1
    if x < y:
        return 1

def run_simulation_iteration(positions, velocities, dimension):
    for i in range(len(positions) // 3):
        for j in range(i + 1, len(positions) // 3):
            velocities[i * 3 + dimension] += gravity(positions[i * 3 + dimension], positions[j * 3 + dimension])
            velocities[j * 3 + dimension] += gravity(positions[j * 3 + dimension], positions[i * 3 + dimension])

        positions[i * 3 + dimension] += velocities[i * 3 + dimension]


def find_period(positions, velocities, dimension):
    period = 1

    initial_positions = positions[dimension::3]
    run_simulation_iteration(positions, velocities, dimension)
    p = positions[dimension::3]
    v = velocities[dimension::3]
    while initial_positions != p or any(x != 0 for x in v):
        run_simulation_iteration(positions, velocities, dimension)
        positions = positions[dimension::3]
        velocities = velocities[dimension::3]
        period += 1
    return period

def find_universe_period(positions, velocities):
    periods = []
    for i in range(3):
        periods.append(find_period(positions, velocities, i))
        print(periods)

    return lcmm(periods)

def simulate_dimension(positions, velocities, dimension, iterations):
    while iterations > 0:
        iterations -= 1
        run_simulation_iteration(positions, velocities, dimension)


def simulate(positions, velocities, itter):
    for i in range(3):
        simulate_dimension(positions, velocities, i, itter)

def compute_energy(positions, velocities):
    energy = 0
    for i in range(len(positions) // 3):
        energy += sum(map(abs, positions[i * 3:(i + 1) * 3])) * sum(map(abs, velocities[i * 3: (i + 1) * 3]))
    return energy


def parse(lines):
    positions = []
    for line in lines:
         m = re.match("<x=([-]?[0-9]+), y=([-]?[0-9]+), z=([-]?[0-9]+)", line)
         positions.append(int(m.group(1)))
         positions.append(int(m.group(2)))
         positions.append(int(m.group(3)))

    return positions


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()
    positions = parse(lines)

    simulated_positions = list(positions)
    simulated_velocities = [0] * len(positions)
    itter = int(input("enter number of itterations: "))
    simulate(simulated_positions, simulated_velocities, itter)
    print(compute_energy(simulated_positions, simulated_velocities))

    
    print(find_universe_period(positions, [0] * len(positions)))


if __name__== "__main__":
    main()
