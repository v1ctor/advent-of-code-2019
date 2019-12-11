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
    for c in itertools.permutations(range(5), 5):
        signal = 0
        for i in c:
            a = Amplifier(memory, i, signal)
            signal = a.execute()
        if maxSignal < signal:
            maxSignal = signal
            result = c

    print("Result signal: {}".format(maxSignal))
    print("Combination: {}".format(result))

if __name__== "__main__":
    main()
