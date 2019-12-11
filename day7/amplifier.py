
import StringIO
import sys
from computer import Computer

class Amplifier:
    
    def __init__(self, phase, signal, amplifier = None):
        self.phase = phase
        self.signal = signal
        self.amplifier = amplifier

    def execute(self):
        oldstdin = sys.stdin




