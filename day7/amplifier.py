from StringIO import StringIO
from computer import Computer

class Amplifier:
    
    def __init__(self, program, phase, signal, amplifier = None):
        self.phase = phase
        self.program = program
        self.signal = signal
        self.amplifier = amplifier

    def execute(self):
        stdin = StringIO("{}\n{}\n".format(self.phase, self.signal))
        stdout = StringIO()
        c = Computer(self.program, stdin, stdout)
        c.run()
        signal = int(stdout.getvalue())
        stdin.close()
        stdout.close()
        return signal




