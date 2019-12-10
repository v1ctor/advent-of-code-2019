import sys

def is_between(a, b, c):
    if a > b:
        return a > c and c > b
    else:
        return a < c and c < b

def is_intersect(a, b, c, d):
    return (is_between(a[0], b[0], c[0]) and is_between(c[1], d[1], a[1])) or (is_between(a[1], b[1], c[1]) and is_between(c[0], d[0], a[0]))

def parse_coords(cmds):
    coords = []
    point = [0, 0]
    coords.append(point)
    for cmd in cmds:
        point = list(point)
        length = int(cmd[1:])
        direction = cmd[0]
        if direction == 'U':
            point[1] += length
        if direction == 'D':
            point[1] -= length
        if direction == 'L':
            point[0] -= length
        if direction == 'R':
            point[0] += length

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
                if wire1[i - 1][0] == wire1[i][0]:
                    point = [wire1[i][0], wire2[j][1]]
                else:
                    point = [wire2[j][0], wire1[i][1]]
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
