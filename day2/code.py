

f = open("input.txt")

s = f.readline()
#s = "1,0,0,0,99"

c = list(map(int, s.split(",")))

size = len(c)
index = 0

c[1] = 12
c[2] = 2

while index < size:
    op = c[index]
    if op == 99:
        break
    a = c[c[index + 1]]
    b = c[c[index + 2]]
    addr = c[index + 3]
    if op == 1:
        c[addr] = a + b
    elif op == 2:
        c[addr] = a * b
    index += 4

print(c[0])
