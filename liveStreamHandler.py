# liveStreamHandler.py
#------------------------
# Handles audio inputs. Right now it only handles live input, but we should add a file input.
# THAT would be cool!
# Note: I read about wave file stream and I'm thinking about having multiple streamHandlers. baseStreamHandler would be an abstract class
#       with: _callBackProcessing(), start() and stop()

import pyaudio
import numpy
import io

from baseStreamHandler import baseStreamHandler
from mathlab import fonctionReconnaissance
from outputGenerator import outputGenerator

DEFAULT_CHANNELS = 1
DEFAULT_RATE = 44100
DEFAULT_DEVICE_INDEX = 0
DEFAULT_STREAM_DATA_TYPE = pyaudio.paInt16

DEFAULT_DATA_TYPE = numpy.int16
DEFAULT_CHUNK_SIZE = 1024

class liveStreamInfo:
    def __init__(self, channels = DEFAULT_CHANNELS, rate = DEFAULT_RATE, deviceIndex = DEFAULT_DEVICE_INDEX, streamDataType = DEFAULT_STREAM_DATA_TYPE):
        self.channels = channels
        self.rate = rate
        self.deviceIndex = deviceIndex
        self.streamDataType = streamDataType

class liveStreamHandler(baseStreamHandler):
    def __init__(self, func = fonctionReconnaissance, outputGen = outputGenerator(), dataType = DEFAULT_DATA_TYPE, chunkSize = DEFAULT_CHUNK_SIZE, streamInfo = liveStreamInfo()):
        baseStreamHandler.__init__(self, func, outputGen, dataType, chunkSize)
        self.streamInfo = streamInfo

    def _getCallback(self):
        def _streamCallback(in_data, frame_count, time_info, status):
            data = []
            data = numpy.fromstring(in_data, dtype=numpy.int16).tolist()
            noteData = self.func(data)
            
            self._callBackProcessing(noteData)
            
            return (None, pyaudio.paContinue)
        return _streamCallback

    def start(self):
        self._pa = pyaudio.PyAudio()
        self.stream = self._pa.open(format = self.streamInfo.streamDataType,
                                    channels = self.streamInfo.channels,
                                    rate = self.streamInfo.rate,
                                    input = True,
                                    input_device_index = self.streamInfo.deviceIndex,
                                    frames_per_buffer = self.chunkSize,
                                    stream_callback = self._getCallback())

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self._pa.terminate()

if __name__ == "__main__":
    #sh = liveStreamHandler(outputGen = outputGenerator(outputStream = io.open("yotest.txt", 'w')))
    sh = liveStreamHandler()
    sh.start()
    print('Press ENTER to stop recording... '),
    nothing = raw_input()
    sh.stop()
