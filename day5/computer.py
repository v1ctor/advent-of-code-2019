
class Computer:

    def __init__(self, memory):
        self.memory = list(memory)
        self.pc = 0

    def mode(self, mode, pos):
        for i in range(1, pos):
            mode = mode / 10
        return mode % 10


    def read(self, pos, mode = -1):
        value = self.memory[self.pc + pos]
        if mode == -1:
            return value
        if self.mode(mode, pos) == 0:
            return self.memory[value]
        else:
            return value

    # op 1
    def add(self, mode):
        val1 = self.read(1, mode)
        val2 = self.read(2, mode)
        addr = self.read(3)
        self.memory[addr] = val1 + val2
        self.pc += 4

    # op 2
    def mult(self, mode):
        val1 = self.read(1, mode)
        val2 = self.read(2, mode)
        addr = self.read(3)
        self.memory[addr] = val1 * val2
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
        addr = self.read(3)
        if first < second:
            self.memory[addr] = 1
        else:
            self.memory[addr] = 0
        self.pc += 4

    # op 8
    def equals(self, mode):
        first = self.read(1, mode)
        second = self.read(2, mode)
        addr = self.read(3)
        if first == second:
            self.memory[addr] = 1
        else:
            self.memory[addr] = 0
        self.pc += 4

    # op 3
    def input(self, mode):
        val = input()
        addr = self.read(1)
        self.memory[addr] = val
        self.pc += 2

    # op 4
    def output(self, mode):
        val = self.read(1, mode)
        print(val)
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

