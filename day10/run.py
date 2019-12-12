import sys
import heapq
import math


def angle(x, y):
    rad = 180 / math.pi
    angle = math.atan2(-y, x) * rad
    if angle < 0:
        return angle + 360
    return angle


class Asteroid:
    def __init__(self, x, y, weight):
	self.x = x
	self.y = y
	self.weight = weight


def compute_asteroid_map(x, y, rows):
    result = {}
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if j == x and i == y:
                continue
            if rows[i][j] != '#':
                continue
            a = angle(y - i, x - j)
            if a not in result:
                result[a] = []
            length = math.sqrt(math.pow(j - x, 2) + math.pow(i - y, 2))
	    heapq.heappush(result[a], (length, [j, i]))
    return result


def compute_weight(x, y, rows):
    return len(compute_asteroid_map(x, y, rows))
    
def get_target_point(rows):
    result = Asteroid(-1, -1, 0)
    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if rows[y][x] == '#':
                candidate = compute_weight(x, y, rows)
                if candidate > result.weight:
                    result = Asteroid(x, y, candidate) 

    return result

def compute_asteroid_queue(x, y, rows):
    result = []
    dirs = compute_asteroid_map(x, y, rows)
    for key, value in dirs.items():
        heapq.heappush(result, (key, value))
    return result


def get_nth_asteroid(x, y, rows, nth):
    first = compute_asteroid_queue(x, y, rows)
    second = []
    k = 0
    while len(first) > 0:
        direction = heapq.heappop(first)
        asteroid = heapq.heappop(direction[1])
        print("angle {}, coords {}".format(direction[0], asteroid[1]))
        k += 1
        if k == nth:
            return asteroid[1]
        if len(direction[1]) > 0:
            heapq.heappush(second, direction)
        if len(first) == 0:
            first, second = second, first
    return None


def main():
    filename = "input.txt"
    destroy = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--destroy":
	destroy = True
    f = open(filename)
    rows = f.readlines()
    
    result = get_target_point(rows)
    print("[{}, {}]".format(result.x, result.y))
    if not destroy:
	print(result.weight)
    else:
	coords = get_nth_asteroid(result.x, result.y, rows, 200)
        print(coords[0] * 100 + coords[1])


if __name__== "__main__":
    main()

