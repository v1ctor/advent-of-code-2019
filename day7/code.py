import sys
from computer import Computer
from amplifier import Amplifier

def main():
    filename = "input.txt"
    steps = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    a = Amplifier(memory, 3, 0)
    signal = a.execute()

    print("Result signal: {}".format(signal))

if __name__== "__main__":
    main()
