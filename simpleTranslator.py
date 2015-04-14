# simpleTranslator.py
# --------------------------
# Simple implementation of the baseTranslator to test the outputGenerator.
# Uses mathlab.py convertToLetterNote() to translates notes to letter.
# Has a buffer of 1 note

import mathlab

from baseTranslator import baseTranslator

BUFFER_LENGTH = 1
END_CHAR = '\n'

class simpleTranslator(baseTranslator):
    def __init__(self):
        baseTranslator.__init__(self, BUFFER_LENGTH, END_CHAR)
    
    def _translate(self, notes):
        self.buffer += mathlab.convertToLetterNote(notes[0]) + " " + str(notes[1])
        self.bufferSize += 1