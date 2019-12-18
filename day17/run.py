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
    run = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--run":
        run = True
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    if not run:
        computer = Computer(memory)
        display = ""
        while not computer.terminated():
            computer.run()
            while len(computer.writebuf) > 0:
                display += chr(computer.receive())

        print(display)

        print(calculate_alignment(display))
    else:
        memory[0] = 2
        computer = Computer(memory)
        display = "" 
        program = "A,C,A,C,B,B,C,A,C,B\nL,10,R,10,L,10,L,10\nR,12,L,12,R,6\nR,10,R,12,L,12\nn\n"
        for c in program:
            computer.send(ord(c))

        while not computer.terminated():      
            computer.run()
        
        while len(computer.writebuf) > 0:
            print(computer.receive())


if __name__== "__main__":
    main()
