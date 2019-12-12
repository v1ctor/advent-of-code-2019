import sys
import heapq
import math


def angle(x, y):
    angle = (math.atan2(y, x) + math.pi / 2) * rad
    if angle < 0:
        return angle + 360
    return angle:



class Asteroid:
    def __init__(self, x, y, weight):
	self.x = x
	self.y = y
	self.weight = weight

class Direction:
    direction = []

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

    d = Direction()
    d.direction = (x, y)
    return d


def compute_asteroid_map(x, y, rows):
    result = {}
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if j == x and i == y:
                continue
            if rows[i][j] != '#':
                continue
            d = get_direction(j - x, i - y)
            if d.direction not in result:
                result[d.direction] = []
            length = math.sqrt(math.pow(j - x, 2) + math.pow(i - y, 2))
	    heapq.heappush(result[d.direction], (length, [j, i]))
    return result


def process_sector(x, y, current, current_round, rounds, dirs, n):
    d = get_direction(x, y)
    if d.direction in dirs:
        if d.direction not in rounds:
	    rounds[d.direction] = 0
	if rounds[d.direction] < current_round:
	    rounds[d.direction] = current_round
	    current += 1
	    elem = heapq.heappop(dirs[d.direction])
            if len(dirs[d.direction]) == 0:
		del dirs[d.direction]
            print(elem)
	    if current == n:
		return (elem, None)
    return (None, current)


def get_nth_asteroid(x, y, rows, n):
    dirs = compute_asteroid_map(x, y, rows)
    rounds = {}
    current_round = 1
    current = 0
    
    while len(dirs) > 0:
        # x ^ y ^
    	for i in range(x, len(rows[0]) + 1):
	    for j in range(0, y):
	    	result = process_sector(i - x, j - y, current, current_round, rounds, dirs, n)
	    	if result[0] != None:
		    return result[0]
	    	current = result[1]

        # x v y ^
        for i in range(len(rows[0]), x - 1, -1):
	    for j in range(y, len(rows) + 1):
	        result = process_sector(i - x, j - y, current, current_round, rounds, dirs, n)
	        if result[0] != None:
		    return result[0]
	        current = result[1]

        # x v y v
        for i in range(x, -1, -1):
	    for j in range(len(rows), y - 1, -1):
	        result = process_sector(i - x, j - y, current, current_round, rounds, dirs, n)
	        if result[0] != None:
		    return result[0]
                current = result[1]

        # x ^ y v
        for i in range(0, x):
	    for j in range(y, -1, -1):
	        result = process_sector(i - x, j - y, current, current_round, rounds, dirs, n)
	        if result[0] != None:
		    return result[0]
	        current = result[1]

        current_round += 1
    return None
		         

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
	print(get_nth_asteroid(result.x, result.y, rows, 200))


if __name__== "__main__":
    main()

