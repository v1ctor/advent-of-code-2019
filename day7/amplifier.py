from computer import Computer
from io import StringIO

class Amplifier:
    
    def __init__(self, name, program, phase):
        self.name = name
        self.computer = Computer(program)
        self.computer.readbuf.append(phase)

    def terminated(self):
        return self.computer.terminated()

    def amplify(self, signal):
        self.computer.readbuf.append(signal)
        self.computer.run()
        signal = None
        if len(self.computer.writebuf) > 0:
            signal = self.computer.writebuf[0]
            self.computer.writebuf = self.computer.writebuf[1:]

        return signal




