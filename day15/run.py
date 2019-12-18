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

    def backtrack(self):
        direction = self.path[-1]
        self.path = self.path[:-1] 
        if direction == 1:
            return 2
        elif direction == 2:
            return 1
        elif direction == 3:
            return 4
        else:
            return 3

    def search_oxygen(self):   

        # THIS CODE ISN'T READY
        # The idea is to implement DFS with backtracking and keeping a minimum path
        # The droid cannot do BFS because it has to return to the starting position anyway
        oxygen = False
        while not oxygen:
            for i in range(1,5):
                c.send(i)
                c.run()
                status = c.receive()


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
