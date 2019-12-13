from computer import Computer

class Direction:
    N = 1
    W = 2
    S = 3
    E = 4

    def __init__(self, d):
        self.d = d

    
    def turn_left(self):
        if self.d == Direction.N:
            return Direction(Direction.W)
        if self.d == Direction.W:
            return Direction(Direction.S)
        if self.d == Direction.S:
            return Direction(Direction.E)
        if self.d == Direction.E:
            return Direction(Direction.N)
    

    def turn_right(self):
        if self.d == Direction.N:
            return Direction(Direction.E)
        if self.d == Direction.E:
            return Direction(Direction.S)
        if self.d == Direction.S:
            return Direction(Direction.W)
        if self.d == Direction.W:
            return Direction(Direction.N)

    
    def diff(self):
        if self.d == Direction.N:
            return [0, -1]
        if self.d == Direction.E:
            return [1, 0]
        if self.d == Direction.S:
            return [0, 1]
        if self.d == Direction.W:
            return [-1, 0]


class Robot:
    def __init__(self, program):
        self.computer = Computer(program)
        # black pixel initialy
        self.computer.readbuf.append(0)
        self.direction = Direction(Direction.N)

    def run(self):
        coords = (0, 0)
        result = {}
        while not self.computer.terminated():
            self.computer.run()
            if len(self.computer.writebuf) == 2:
                color = self.computer.writebuf[0]
                turn = self.computer.writebuf[1]
                self.computer.writebuf = self.computer.writebuf[2:]
               

                # color  
                if coords not in result:
                    result[coords] = 1
                else:
                    result[coords] += 1

                # move
                if turn == 0:
                    self.direction = self.direction.turn_left()
                else:
                    self.direction = Direction.turn_right(self.direction)
                diff = Direction.diff(self.direction)
                coords = (coords[0] + diff[0], coords[1] + diff[1])

                self.computer.readbuf.append(color)

        return len(result)










