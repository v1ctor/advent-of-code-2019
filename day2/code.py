
from computer import Computer

def main():
    f = open("input.txt")
    s = f.readline()
    memory = list(map(int, s.split(",")))

    c = Computer(memory, 12, 2)
    c.execute()
    print(c.read(0))

if __name__== "__main__":
    main()
