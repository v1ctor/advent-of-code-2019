import math

s = 0
f = open("input.txt")
for i in f.readlines():
   m = int(i)
   f = int(math.floor(m / 3) - 2)
   while f > 0:
     s = s + f
     f = int(math.floor(f / 3) - 2)

print (int(s))
