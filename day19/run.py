import sys
from computer import Computer            

def get_result(program, is_row, x, y):
    computer = Computer(program)
    computer.send(x if is_row else y)
    computer.send(y if is_row else x)
    computer.run()
    return computer.receive()


def divider():
    for i in range(1, 10001):
        if 10000 % i == 0:
            yield i

def find_place(program, is_row, index, start, end):


    # 

    return [7267, 9074]
    i = start 
    left = None
    while i <= end:
        if get_result(program, is_row, index, i) == 1:
            left = i
            break
        i+=1 
    i = end
    right = 0
    while i >= 0:
        if get_result(program, is_row, index, i) == 1:
            right = i
            break
        i-=1
    return [left, right]


def binary_search(program, n):

    row_place = find_place(program, True, n - 1, 0, n - 1)
    print(f"{row_place}")


def main():
    filename = "input.txt"
    second = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--second":
        second = True
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    if not second:
        beam = 0
        for i in range(50):
            for j in range(50):
                computer = Computer(memory)
                computer.send(i)
                computer.send(j)
                computer.run()
                if computer.receive() == 1:
                    beam += 1
        print(beam)
    else:
        binary_search(memory, 10000) 


if __name__== "__main__":
    main()
