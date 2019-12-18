import sys


entrance = "@"
wall = "#"
empty = "."


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()
    
    print(lines)

if __name__== "__main__":
    main()
