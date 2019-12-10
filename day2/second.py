
from computer import Computer

def main():
    f = open("input.txt")
    s = f.readline()
    memory = list(map(int, s.split(",")))

    for i in range(100):
        for j in range(100):
            c = Computer(memory, i, j)
            c.execute()
            if (c.read(0) == 19690720):
                print(100 * i + j)
                return

if __name__== "__main__":
    main()
