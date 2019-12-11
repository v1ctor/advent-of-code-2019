import sys


def get_direction(x, y):
    large = y
    small = x
    if abs(x) > abs(y):
        large = x
        small = y

    if abs(large) == abs(small):
        x /= abs(x)
        y /= abs(y)

    elif small != 0 and abs(large) % abs(small) == 0:
        x /= abs(small)
        y /= abs(small)


    elif x == 0:
        y /= abs(y)
    elif y == 0:
        x /= abs(x)

    return (x, y)

def compute_weight(x, y, rows):
    result = {}
   # print([x, y])
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if i == x and j == y:
                continue
            if rows[i][j] != '#':
                continue
            direction = get_direction(i - x, j - y)
            if direction not in result:
                result[direction] = []
            result[direction].append([i - x, j - y])


    # print(result)
    return len(result)


    

def main():
    filename = "input.txt"
    steps = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    rows = f.readlines()
    
    result = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == '#':
                candidate = compute_weight(i, j, rows)
                if candidate > result:
                    result = candidate

#    print(rows)
    print(result)


if __name__== "__main__":
    main()
