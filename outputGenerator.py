# outputGenerator.py
# --------------------------
# Translates some notes with a translator (default: simpleTranslator) and outputs them in a stream (default: stdout)

import sys

from simpleTranslator import simpleTranslator

class outputGenerator:
    def __init__(self, translator = simpleTranslator(), outputStream = sys.stdout):
        self.translator = translator
        self.outputStream = outputStream
        self._lastNote = None

    def translate(self, notes):
        """Notes should be tuples (Interval, Octave) in a list"""
        for n in notes:
            if n[0] == None:
                buffer = self.translator.flush()
                self.outputStream.write(unicode(buffer))
                self.outputStream.flush()
                break
            elif self._lastNote == n:
                break
            else:
                self._lastNote = n
                buffer = self.translator.translate(n)

            if buffer:
                self.outputStream.write(unicode(buffer))
                self.outputStream.flush()

