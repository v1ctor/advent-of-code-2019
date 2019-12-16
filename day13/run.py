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
    print(c.writebuf[2::3].count(2))

if __name__== "__main__":
    main()
