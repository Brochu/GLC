# outputGenerator.py
# --------------------------
# Translates some notes with a translator (default: simpleTranslator) and outputs them in a stream (default: stdout)
# TODO: Systeme de commandes pour dire au translator que c'est fini et de vider son buffer

from simpleTranslator import simpleTranslator
import sys

class outputGenerator:
    def __init__(self, translator = simpleTranslator(), outputStream = sys.stdout):
        self.translator = translator
        self.outputStream = outputStream
    
    def translate(self, notes):
        """Notes should be tuples (Interval, Octave) in a list"""
        for n in notes:
            if n[0] == None:
                buffer = self.translator.flush()
                break
            else:
                buffer = self.translator.translate(n)
            
            if buffer:
                self.outputStream.write(buffer)
                self.outputStream.flush()
                