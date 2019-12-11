import sys

class Asteroid:
    def __init__(self, x, y, weight):
	self.x = x
	self.y = y
	self.weight = weight


def get_direction(x, y):

    limit = min(abs(x), abs(y))

    for factor in range(limit, 1, -1):
        if abs(x) % factor == 0 and abs(y) % factor == 0:
            x /= factor
            y /= factor
            break


    if x == 0 and y != 0:
        y /= abs(y)
    if y == 0 and x != 0:
        x /= abs(x)

    return (x, y)


def compute_asteroid_map(x, y, rows):
    result = {}
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

#    print("[{}] {}".format(len(result), result))
    return result

def get_nth_asteroid(x, y, rows, n):
	pass

def compute_weight(x, y, rows):
    return len(compute_asteroid_map(x, y, rows))
    
def get_target_point(rows):
    result = Asteroid(-1, -1, 0)
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == '#':
                candidate = compute_weight(i, j, rows)
                if candidate > result.weight:
                    result = Asteroid(i, j, candidate) 
    return result

def main():
    filename = "input.txt"
    destory = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--destroy":
	destroy = True
    f = open(filename)
    rows = f.readlines()
    
    result = get_target_point(rows)
    if not destory:
	print(result.weight)
    else:
	print(get_nth_asteroid(result.x, result.y, rows, 200))


if __name__== "__main__":
    main()
