
def read_wire(f):
    s = f.readline()
    cmds = list(map(int, s.split(",")))
    return cmds

def main():
    f = open("input.txt")
    
    wire1 = read_wire(f)
    wire2 = read_wire(f)
    
if __name__== "__main__":
    main()
