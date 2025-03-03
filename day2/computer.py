
class Computer:
    def __init__(self, memory, noun, verb):
        self.memory = list(memory)
        self.noun = noun
        self.verb = verb

    def execute(self):
        size = len(self.memory)
        pc = 0

        self.memory[1] = self.noun
        self.memory[2] = self.verb

        while pc < size:
            op = self.memory[pc]
            if op == 99:
                break
            addr1 = self.memory[pc + 1]
            addr2 = self.memory[pc + 2]
            arg1 = self.memory[addr1]
            arg2 = self.memory[addr2]
            addr = self.memory[pc + 3]
            if op == 1:
                self.memory[addr] = arg1 + arg2
            elif op == 2:
                self.memory[addr] = arg1 * arg2
            pc += 4

    def read(self, addr):
        return self.memory[addr]
