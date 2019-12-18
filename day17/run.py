import sys
from computer import Computer            

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

        


if __name__== "__main__":
    main()
