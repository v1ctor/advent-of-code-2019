import sys

def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    line = f.readline().strip()


    commands = list(map(int, list(line)))

    print(commands)



if __name__== "__main__":
    main()
