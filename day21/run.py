import sys
from computer import Computer            


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
        #program = """NOT A J\nNOT B T\nAND T J\nNOT C T\nAND T J\nAND D J\nWALK\n"""
        program = "NOT A T\nAND D T\nNOT B J\nAND C J\nOR T J\nWALK\n"
        for c in program:
            computer.send(ord(c))

        while not computer.terminated():
            computer.run()
            while len(computer.writebuf) > 0:
                display += chr(computer.receive())

            print(display)


if __name__== "__main__":
    main()
