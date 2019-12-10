import sys
from computer import Computer

def main():
    filename = "input.txt"
    steps = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    c = Computer(memory)
    c.run()

if __name__== "__main__":
    main()
