
class Computer:

    def __init__(self, memory):
        self.memory = list(memory)
        self.pc = 0


    def read(self, mode, addr):
        value = self.memory[addr]
	if mode == 0:
	    return self.memory[value]
	else:
	    return value


    def add(self, mode):
	val1 = self.read(mode % 10, self.pc + 1)
	val2 = self.read((mode / 10) % 10, self.pc + 2)
        addr = self.memory[self.pc + 3]
        self.memory[addr] = val1 + val2
        self.pc += 4


    def mult(self, mode):
	val1 = self.read(mode % 10, self.pc + 1)
	val2 = self.read((mode / 10) % 10, self.pc + 2)
        addr = self.memory[self.pc + 3]
        self.memory[addr] = val1 * val2
        self.pc += 4


    def input(self, mode):
	val = input()
        addr = self.memory[self.pc + 1]
        self.memory[addr] = val
        self.pc += 2


    def output(self, mode):
        val = self.read(mode % 10, self.pc + 1)
	print(val)
        self.pc += 2


    def execute(self, opcode): 
            op = opcode % 100
            if op == 99:
                return
	    mode = opcode / 100
            if op == 1:
		self.add(mode)
            elif op == 2:
		self.mult(mode)
            elif op == 3:
		self.input(mode)
            elif op == 4:
		self.output(mode)


    def run(self):
        size = len(self.memory)

        while self.pc < size:
            opcode = self.memory[self.pc]
            self.execute(opcode)

