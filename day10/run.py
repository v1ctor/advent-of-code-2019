import sys


def get_direction(x, y):
    large = abs(y)
    small = abs(x)
    if abs(x) > abs(y):
        large = x
        small = y

    if abs(large) == abs(small):
        x /= abs(x)
        y /= abs(y)

    for factor in range(small, 0, -1):
        if abs(large) % factor == 0 and abs(small) % factor == 0:
            x /= factor
            y /= factor
            break


    if x == 0 and y != 0:
        y /= abs(y)
    if y == 0 and x != 0:
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


    print("[{}] {}".format(len(result), result))
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
