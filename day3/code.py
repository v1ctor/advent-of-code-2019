
def is_intersect(a, b, c, d):
    if a[0] == b[0] and c[1] == d[1]:
        if (a[1] > c[1] and c[1] > b[1]):
            return True
        elif (b[1] > c[1] and c[1] > a[1]):
            return True
    elif a[1] == b[1] and c[0] == d[0]:
        if (a[0] > c[0] and c[0] > b[0]):
            return True
        elif (b[0] > c[0] and c[0] > a[0]):
            return True
    return False

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
            point[1] += length

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
                if wire1[i - 1][0] == wire1[i][0]:
                    intersections.append([wire1[i][0], wire2[j][1]])
                else:
                    intersections.append([wire1[i][1], wire2[j][0]])
    return intersections


def main():
    f = open("input.txt")
    
    wire1 = read_wire(f)
    wire2 = read_wire(f)

#    print(wire1)
#    print(wire2)

    points = find_intersections(wire1, wire2)
    result = points[0] 
    length = abs(result[0]) + abs(result[1])
    for i in range(1, len(points)):
        current = abs(points[i][0]) + abs(points[i][1])
        if current < length:
            length = current 
            result = points[i]

    print(result)
    print(length)


    
if __name__== "__main__":
    main()
