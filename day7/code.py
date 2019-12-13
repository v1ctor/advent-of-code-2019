import sys
from amplifier import Amplifier
import itertools 

def main():
    filename = "input.txt"
    feedback = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--feedback":
        feedback = True
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    maxSignal = 0
    result = None
    signal = 0
    permutations = None
    if not feedback:
        permutations = itertools.permutations(range(5), 5)
    else:
        permutations = itertools.permutations(range(5, 10), 5)

    for perm in permutations:
        signal = 0
        amplifiers = []
        for i in range(len(perm)):
            amplifiers.append(Amplifier("{}".format(i), memory, perm[i]))
        
        running = True
        while running:
            terminated = True
            for a in amplifiers:
                out = a.amplify(signal)
                if out != None:
                    signal = out
                terminated &= a.terminated()
            running = not terminated


        if maxSignal < signal:
            maxSignal = signal
            result = perm

    print("Result signal: {}".format(maxSignal))
    print("Combination: {}".format(result))

if __name__== "__main__":
    main()
