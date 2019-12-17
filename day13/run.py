import sys
from computer import Computer

class Game:
    sizeX = 0 
    sizeY = 0
    score = 0
    buf = None
    ball = None
    platform = None
    command = 0

    def init(self, display):
        for i in range(0, len(display), 3):
            op = display[i:i + 3]
            if op[0] == -1:
                continue
            else:
                if self.sizeX < op[0]:
                    self.sizeX = op[0]
                if self.sizeY < op[1]:
                    self.sizeY = op[1]
        self.buf = [[]] * (self.sizeY + 1)
        for i in range(self.sizeY + 1):
            self.buf[i] = ["."] * (self.sizeX + 1)

    def draw_game(self, display):
        if self.buf == None:
            self.init(display)
        
        for i in range(0, len(display), 3):        
            op = display[i:i + 3]         
            if op[0] == -1:
                self.score = op[2]
            if op[2] == 1: 
                self.buf[op[1]][op[0]] = "#"
            if op[2] == 2:
                self.buf[op[1]][op[0]] = "x"
            if op[2] == 3:
                if self.platform != None:
                    self.buf[self.platform[1]][self.platform[0]] = '.'
                self.buf[op[1]][op[0]] = "="
                self.platform = op[:2]
            if op[2] == 4:
                if self.ball != None:
                    self.buf[self.ball[1]][self.ball[0]] = '.'
                self.ball = op[:2]
                if self.platform != None:
                    if self.platform[0] > self.ball[0]:
                        self.command = -1
                    elif self.platform[0] < self.ball[0]:
                        self.command = 1
                    else:
                        self.command = 0 
                self.buf[op[1]][op[0]] = "o"

        for j in range(self.sizeY + 1):
            print(''.join(self.buf[j]))

        print(self.score)
            

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

   
    game = Game()
    if play:
        memory[0] = 2
        c = Computer(memory)
        while True:
            c.run()
            if len(c.writebuf) == 0:
                break
            game.draw_game(c.writebuf)
            c.writebuf = []
            c.readbuf.append(game.command)
    else:
        c = Computer(memory)
        c.run()
        print(c.writebuf[2::3].count(2))

if __name__== "__main__":
    main()
