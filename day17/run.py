import sys
from computer import Computer            

def calculate_alignment(display):
    display = display.strip()
    rows = display.split("\n")

    alignment = 0

    y = len(rows)
    for j in range(y):
        x = len(rows[j])
        for i in range(x):
            if rows[j][i] == '#' and i > 0 and i < x - 1 and j > 0 and j < y - 1 and rows[j][i - 1] == '#' and rows[j][i + 1] == '#' and rows[j - 1][i] == '#' and rows[j + 1][i] == '#':
                alignment += j * i

    return alignment


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    computer = Computer(memory)
    display = ""
    while not computer.terminated():
        computer.run()
        while len(computer.writebuf) > 0:
            display += chr(computer.receive())

    print(display)

    print(calculate_alignment(display))        


if __name__== "__main__":
    main()
