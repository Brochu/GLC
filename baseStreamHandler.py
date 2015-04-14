# baseStreamHandler.py
#------------------------
# Abstract class representing stream handlers.

import numpy

from mathlab import fonctionReconnaissance
from outputGenerator import outputGenerator

DEFAULT_DATA_TYPE = numpy.int16
DEFAULT_CHUNK_SIZE = 1024

class baseStreamHandler:
    def __init__(self, func = fonctionReconnaissance, outputGen = outputGenerator(), dataType = DEFAULT_DATA_TYPE, chunkSize = DEFAULT_CHUNK_SIZE):
        self.func = func
        self.outputGen = outputGen
        self.dataType = dataType
        self.chunkSize = chunkSize

    def _getCallback(self):
        def _streamCallback(in_data):
            data = []
            data = numpy.fromstring(in_data, dtype=self.dataType).tolist()
            noteData = self.func(data)
            
            return _callBackProcessing(noteData)
        return _streamCallback
    
    def _callBackProcessing(self, data):
        self.outputGen.translate(data)
        return None

    def start(self):
        pass

    def stop(self):
        pass
