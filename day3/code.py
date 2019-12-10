import sys

class Node:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = step


def is_between(a, b, c):
    if a > b:
        return a > c and c > b
    else:
        return a < c and c < b

def is_intersect(a, b, c, d):
    return (is_between(a.x, b.x, c.x) and is_between(c.y, d.y, a.y)) or (is_between(a.y, b.y, c.y) and is_between(c.x, d.x, a.x))

def parse_coords(cmds):
    coords = []
    point = Node(0, 0, 0)
    coords.append(point)
    for cmd in cmds:
        length = int(cmd[1:])
        direction = cmd[0]
        if direction == 'U':
            point = Node(point.x, point.y + length, point.step + length)
        if direction == 'D':
            point = Node(point.x, point.y - length, point.step + length)
        if direction == 'L':
            point = Node(point.x - length, point.y, point.step + length)
        if direction == 'R':
            point = Node(point.x + length, point.y, point.step + length)

        coords.append(point)
    return coords


def read_wire(f):
    s = f.readline()
    cmds = list(s.split(","))
    return parse_coords(cmds)


def find_intersections(wire1, wire2):
    size1 = len(wire1)
    size2 = len(wire2)
    intersections = []
    for i in range(1, size1):
        for j in range(1, size2):
            if is_intersect(wire1[i - 1], wire1[i], wire2[j - 1], wire2[j]):
                point = []
                if wire1[i - 1].x == wire1[i].x:
                    step1 = wire1[i - 1].step + abs(wire1[i - 1].y - wire2[j].y);
                    step2 = wire2[j - 1].step + abs(wire2[j - 1].x - wire1[i].x);
                    point = Node(wire1[i].x, wire2[j].y, step1 + step2)
                else:
                    step1 = wire1[i - 1].step + abs(wire1[i - 1].x - wire2[j].x);
                    step2 = wire2[j - 1].step + abs(wire2[j - 1].y - wire1[i].y);
                    point = Node(wire2[j].x, wire1[i].y, step1 + step2)
                intersections.append(point)
    return intersections


def main():
    filename = "input.txt"
    steps = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--steps":
        steps = True

    f = open(filename)
    
    wire1 = read_wire(f)
    wire2 = read_wire(f)
   
    points = find_intersections(wire1, wire2)

    if not steps:
        result = points[0] 
        length = abs(result.x) + abs(result.y)
        for i in range(1, len(points)):
            current = abs(points[i].x) + abs(points[i].y)
            if current < length:
                length = current 
                result = points[i]

        print(length)
    else:
        result = points[0]
        step = points[0].step

        for i in range(1, len(points)):             
            if points[i].step < step:                 
                step = points[i].step                 
                result = points[i]          
        print(step)


    
if __name__== "__main__":
    main()
