import sys
from computer import Computer

def draw_game(display):
    sizeX = 0
    sizeY = 0
    score = 0
    for i in range(0, len(display), 3):
        op = display[i:i + 3]
        if op[0] == -1:
            score = op[2]
        else:
            if sizeX < op[0]:
                sizeX = op[0]
            if sizeY < op[1]:
                sizeY = op[1]
    buf = [[]] * (sizeY + 1)
    for i in range(sizeY + 1):
        buf[i] = ["."] * (sizeX + 1)
        
    for i in range(0, len(display), 3):        
        op = display[i:i + 3]         
        if op[0] == -1:
            continue
        if op[2] == 1: 
            buf[op[1]][op[0]] = "#"
        if op[2] == 2:
            buf[op[1]][op[0]] = "x"
        if op[2] == 3:
            buf[op[1]][op[0]] = "="
        if op[2] == 4:
            buf[op[1]][op[0]] = "o"

    for j in range(sizeY + 1):
        print(''.join(buf[j]))
            

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

    
    if play:
        memory[0] = 2
        c = Computer(memory)
        while True:
            c.run()
            if len(c.writebuf) == 0:
                break
            draw_game(c.writebuf)
            c.writebuf = [] 
    else:
        c = Computer(memory)
        c.run()
        print(c.writebuf[2::3].count(2))

if __name__== "__main__":
    main()
