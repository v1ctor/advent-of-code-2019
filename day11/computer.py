
import sys

class Computer:

    def __init__(self, memory, stdin = sys.stdin, stdout = sys.stdout):
        self.memory = list(memory) + [0] * 10000 
        self.pc = 0
        self.rb = 0
        self.stdin = stdin
        self.stdout = stdout

    def mode(self, mode, pos):
	for i in range(1, pos):
	    mode = mode / 10
	return mode % 10


    def write(self, pos, value, mode):
        addr = self.memory[self.pc + pos]
        value_mode = self.mode(mode, pos)
	if value_mode == 0:
	    self.memory[addr] = value
        elif value_mode == 2:
            self.memory[self.rb + addr] = value

    def read(self, pos, mode = -1):
        value = self.memory[self.pc + pos]
        if mode == -1:
	    return value
        value_mode = self.mode(mode, pos)
	if value_mode == 0:
	    return self.memory[value]
        elif value_mode == 2:
            return self.memory[self.rb + value]
        else:
	    return value

    # op 1
    def add(self, mode):
	val1 = self.read(1, mode)
	val2 = self.read(2, mode)
        addr = self.write(3, val1 + val2, mode)
        self.pc += 4

    # op 2
    def mult(self, mode):
        val1 = self.read(1, mode)
        val2 = self.read(2, mode)
        addr = self.write(3, val1 * val2, mode)
        self.pc += 4

    # op 5 
    def jump_if_true(self, mode):
	cond = self.read(1, mode)
	if cond != 0:
	    addr = self.read(2, mode)
	    self.pc = addr
	else:
	    self.pc += 3

    # op 6
    def jump_if_false(self, mode):
	cond = self.read(1, mode)
	if cond == 0:
	    addr = self.read(2, mode)
	    self.pc = addr
	else:
	    self.pc += 3

    # op 7
    def less_than(self, mode):
	first = self.read(1, mode)
        second = self.read(2, mode)
	if first < second:
	    self.write(3, 1, mode)
	else:
	    self.write(3, 0, mode)
	self.pc += 4

    # op 8
    def equals(self, mode):
	first = self.read(1, mode)
        second = self.read(2, mode)
	if first == second:
	    self.write(3, 1, mode)
        else:
	    self.write(3, 0, mode)
	self.pc += 4

    # op 9
    def relative_base(self, mode):
        val = self.read(1, mode)
        self.rb += val
        self.pc += 2

    # op 3
    def input(self, mode):
	val = int(self.stdin.readline())
        self.write(1, val, mode)
        self.pc += 2

    # op 4
    def output(self, mode):
        val = self.read(1, mode)
	self.stdout.write(str(val) + "\n")
        self.pc += 2


    def execute(self, op, mode): 
            if op == 1:
		self.add(mode)
            elif op == 2:
		self.mult(mode)
            elif op == 3:
		self.input(mode)
            elif op == 4:
		self.output(mode)
	    elif op == 5:
		self.jump_if_true(mode)
	    elif op == 6:
		self.jump_if_false(mode)
	    elif op == 7:
		self.less_than(mode)
	    elif op == 8:
		self.equals(mode)
            elif op == 9:
                self.relative_base(mode)


    def run(self):
        size = len(self.memory)

        while self.pc < size:
            opcode = self.memory[self.pc]
            op = opcode % 100
            mode = opcode / 100
	    # print("op: {}".format(opcode))
            if op == 99:
		break
            self.execute(op, mode)

