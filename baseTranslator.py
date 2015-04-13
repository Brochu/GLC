# baseTranslator.py
# --------------------------
# Abstract class for translators
#   Should contain some settings and some methods
#       - translate(): Should return None if the buffer is not complete, else return the buffer.
#                       This function receives a tuples (Interval, Octave) from the output Generator.
#       - flush(): When the generator stops receiving notes, the buffer must be filled/finished or whatever and returned

BASE_BUFFER_SIZE = 16 # Notes, not bytes
END_CHAR = '\n'

class baseTranslator:
    def __init__(self, bufferMaxSize = BASE_BUFFER_SIZE, endChar = END_CHAR):
        self.bufferMaxSize = bufferMaxSize
        self.endChar = endChar
        self.buffer = ''
        self.bufferSize = 0
    
    def translate(self, notes):
        self._translate(notes)
        
        if self.bufferSize >= self.bufferMaxSize:
            return self.flush()
        else:
            return None
    
    def flush(self):
        self._flush()
        
        self.buffer += self.endChar
        temp = self.buffer
        self.buffer = ''
        self.bufferSize = 0
        return temp
        
    def _translate(self, notes):
        pass
    
    def _flush(self):
        pass