import sys
from computer import Computer
from robot import Robot

def main():
    filename = "input.txt"
    steps = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    robot = Robot(memory)
    print(robot.run())


if __name__== "__main__":
    main()
