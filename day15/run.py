import sys
from computer import Computer            

class Droid:
    def __init__(self, memory):
        self.x = 0
        self.y = 0
        self.path = []
        self.visited = {}
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


    def target(self, direction):
        if direction == 1:
            return (self.x, self.y - 1)
        elif direction == 2:
            return (self.x, self.y + 1)
        elif direction == 3:
            return (self.x - 1, self.y)
        else:
            return (self.x + 1, self.y)
        

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
    print(droid.search_oxygen())

if __name__== "__main__":
    main()
