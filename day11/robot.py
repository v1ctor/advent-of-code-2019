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


    def compute_colors(self):
        coords = (0, 0)
        result = {}
        while not self.computer.terminated():
            self.computer.run()
            if len(self.computer.writebuf) == 2:
                color = self.computer.writebuf[0]
                turn = self.computer.writebuf[1]
                self.computer.writebuf = self.computer.writebuf[2:]

                # color  
                result[coords] = color

                # move
                if turn == 0:
                    self.direction = self.direction.turn_left()
                else:
                    self.direction = Direction.turn_right(self.direction)
                diff = Direction.diff(self.direction)
        #        print("coords {}, diff {}, color {}, turn {}".format(coords, diff, color, turn))
                
                coords = (coords[0] + diff[0], coords[1] + diff[1])

                instruction = 0
                if coords in result:
                    instruction = result[coords]

                self.computer.readbuf.append(instruction)


        return result

    def draw_picture(self):
        self.computer.readbuf = []
        self.computer.readbuf.append(1)

        colors = self.compute_colors()
        minX = 0
        minY = 0
        maxX = 0
        maxY = 0

        for key in colors.keys():
            if key[0] < minX:
                minX = key[0]
            if key[0] > maxX:
                maxX = key[0]
            if key[1] < minY:
                minY = key[1]
            if key[1] > maxY:
                maxY = key[1]


        sizeX = maxX - minX + 1
        sizeY = maxY - minY + 1

        result = [[]] * sizeY
        for j in range(sizeY):
            result[j] = ['.'] * sizeX
            for i in range(sizeX):
                coords = (i - minX, j - minY)
                if coords in colors:
                    if colors[coords] == 1:
                        result[j][i] = "#"

        for row in result:
            print(''.join(row))


    def run(self):
        return len(self.compute_colors())












