from StringIO import StringIO
from computer import Computer

class Amplifier:
    
    def __init__(self, program, phase, amplifier = None):
        self.phase = phase
        self.program = program
        self.amplifier = amplifier

    def amplify(self, signal):
        stdin = StringIO("{}\n{}\n".format(self.phase, signal))
        stdout = StringIO()
        c = Computer(self.program, stdin, stdout)
        c.run()
        signal = int(stdout.getvalue())
        stdin.close()
        stdout.close()
        return signal




