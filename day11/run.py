import sys
from robot import Robot

def main():
    filename = "input.txt"
    draw = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--draw":
        draw = True
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    robot = Robot(memory)
    if not draw:
        print(robot.run())
    else:
        robot.draw_picture()

if __name__== "__main__":
    main()
