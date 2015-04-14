# WavStreamHandler.py
#------------------------
# Specific stream handler that will read input from a wav file, read it by chunks, process and send it to output generator
# DEFAULT_CHUNK_SIZE a ete teste de facon empirique
import sys
import numpy
import wave

from mathlab import fonctionReconnaissance
from outputGenerator import outputGenerator

from baseStreamHandler import baseStreamHandler

DEFAULT_DATA_TYPE = numpy.int16
DEFAULT_CHUNK_SIZE = 4096

class WavStreamHandler(baseStreamHandler):
    def __init__(self, fileName, func = fonctionReconnaissance, outputGen = outputGenerator(), dataType = DEFAULT_DATA_TYPE, chunkSize = DEFAULT_CHUNK_SIZE):
        baseStreamHandler.__init__(self, func, outputGen, dataType, chunkSize)
        self.fileName = fileName
        self.wav = None

    def start(self):
        self.wav = wave.open(self.fileName, "rb")

        # read chucks until end
        readchunk = self.wav.readframes(self.chunkSize)
        while(readchunk != ""):
            # print numpy.fromstring(readchunk, dtype=self.dataType).tolist()
            self._getCallback()(readchunk)
            readchunk = self.wav.readframes(self.chunkSize)

        self.stop()

    def stop(self):
        self.wav.close()

if __name__ == "__main__":
    test = WavStreamHandler(sys.argv[1])
    test.start()
