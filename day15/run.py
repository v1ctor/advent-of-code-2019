import sys
from computer import Computer            

class Droid:
    def __init__(self, memory):
        self.x = 0
        self.y = 0
        self.path = []
        self.visited = {}
        self.oxygen = None
        self.computer = Computer(memory)

    def move(self, direction):
        self.path.append(direction)
        if direction == 1:
            self.y -= 1
        elif direction == 2:
            self.y += 1
        elif direction == 3:
            self.x -= 1 
        else:
            self.x += 1

    def direction(self, source, direction):
        if direction == 1:
            return (source[0], source[1] - 1)
        elif direction == 2:
            return (source[0], source[1] + 1)
        elif direction == 3:
            return (source[0] - 1, source[1])
        else:
            return (source[0] + 1, source[1])


    def target(self, direction):
       return self.direction((self.x, self.y), direction)


    def backtrack(self):
        direction = self.path[-1]
        if direction == 1:
            self.move(2)
            self.path = self.path[:-2] 
            return 2
        elif direction == 2:
            self.move(1)
            self.path = self.path[:-2] 
            return 1
        elif direction == 3:
            self.move(4)
            self.path = self.path[:-2] 
            return 4
        else:
            self.move(3)
            self.path = self.path[:-2] 
            return 3

    def __dfs(self):
        min_path = None
        # The idea is to implement DFS with backtracking and keeping a minimum path
        # The droid cannot do BFS because it has to return to the starting position anyway
        for i in range(1, 5):
            target = self.target(i)
            if target in self.visited:
                continue
            self.computer.send(i)
            self.computer.run()
            status = self.computer.receive()
            self.visited[target] = status 

            print("target {} direction {} status {} path {}".format(target, i, status, self.path))

            if status != 0:
                self.move(i)

            # oxygen
            if status == 2:
                # if we found oxygen it means tha none of the neighbours of this node can have a shorter path
                self.oxygen = target
                min_path = len(self.path)
                break

            # moved
            if status != 0:
                result = self.__dfs()
                if result != None and (min_path is None or result < min_path):
                    min_path = result

        direction = self.backtrack()
        self.computer.send(direction)
        self.computer.run()
        if self.computer.receive() == 0:
            print("Error!")
            return None
            
        return min_path


    def search_oxygen(self):   

        self.visited = {}
        return self.__dfs()


    def draw_map(self):
        maxX = 0
        minX = 0
        maxY = 0
        minY = 0
        for key in self.visited.keys():
            if key[0] < minX:
                minX = key[0]
            if key[0] > maxX:
                maxX = key[0]
            if key[1] < minY:
                minY = key[1]
            if key[1] > maxY:
                maxY = key[1]
        sizeX = abs(minX) + maxX + 1
        sizeY = abs(minY) + maxY + 1

        result = [[]] * sizeY
        for y in range(sizeY):
            result[y] = ["."] * sizeX
            for x in range(sizeX):
                pos = (x - abs(minX), y - abs(minY))
                if pos in self.visited:
                    status = self.visited[pos]
                    if status == 0:
                        result[y][x] = "#"
                    if status == 2:
                        result[y][x] = "o"
            print(''.join(result[y]))


    def fill_oxygen(self):
        if self.oxygen is None or self.oxygen not in self.visited or self.visited[self.oxygen] != 2:
            return None
        visited = {}
        queue = []
        time = 0
        queue.append((self.oxygen, 0))
        while len(queue) > 0:
            current = queue[0][0]
            time = queue[0][1]
            queue = queue[1:]
            for i in range(1, 5):
                direction = self.direction(current, i)
                if direction not in visited and direction in self.visited and self.visited[direction] == 1:
                    visited[direction] = True
                    queue.append((direction, time + 1))

        return time




def main():
    filename = "input.txt"
    play = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--play":
        play = True
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    droid = Droid(memory)
    source = droid.search_oxygen()
    print(source)

    droid.draw_map()

    time = droid.fill_oxygen()
    print(time)

if __name__== "__main__":
    main()
