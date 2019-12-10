import sys

class Node:
    def __init__(self, x, y, step):
        self.x = x
        self.y = y
        self.step = 0



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
                    point = [wire1[i].x, wire2[j].y]
                else:
                    point = [wire2[j].x, wire1[i].y]
                #print ("{} {} {} {} {} {} {}".format(i, j, point, wire1[i - 1], wire1[i], wire2[j - 1], wire2[j]))
                intersections.append(point)
    return intersections


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    
    wire1 = read_wire(f)
    wire2 = read_wire(f)
   
    points = find_intersections(wire1, wire2)

    result = points[0] 
    length = abs(result[0]) + abs(result[1])
    for i in range(1, len(points)):
        current = abs(points[i][0]) + abs(points[i][1])
        if current < length:
            length = current 
            result = list(points[i])

    print(result)
    print(length)


    
if __name__== "__main__":
    main()
