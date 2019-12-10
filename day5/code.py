
from computer import Computer

def main():
    f = open("input.txt")
    s = f.readline()
    memory = list(map(int, s.split(",")))

    c = Computer(memory)
    c.run()

if __name__== "__main__":
    main()
