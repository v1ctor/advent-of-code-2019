from StringIO import StringIO
from computer import Computer

class Amplifier:
    
    def __init__(self, program, phase):
        self.computer = Computer(program)
        self.computer.readbuf.append(phase)

    def terminated(self):
        return not self.computer.interrupted()

    def amplify(self, signal):
        self.computer.readbuf.append(signal)
        self.computer.run()
        signal = None
        if len(self.computer.writebuf) > 0:
            signal = self.computer.writebuf[0]
            self.computer.output = self.computer.writebuf[1:]

        return signal




