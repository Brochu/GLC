# streamHandler.py
#------------------------
# Handles audio inputs. Right now it only handles live input, but we should add a file input.
# THAT would be cool!

import pyaudio
import time
import numpy
import struct

from mathlab import *

#CUTOFF_THRESHOLD = 0.001

#DEFAULT_WIDTH = 4 # Nombre de byte par sample
DEFAULT_CHANNELS = 1
DEFAULT_RATE = 44100
DEFAULT_DEVICE_INDEX = 0
DEFAULT_FRAMES_PER_BUFFER = 2048

class streamInfo:
    def __init__(self, width = 4, channels = DEFAULT_CHANNELS, rate = DEFAULT_RATE, deviceIndex = DEFAULT_DEVICE_INDEX, framesPerBuffer = DEFAULT_FRAMES_PER_BUFFER):
        self.width = width
        self.channels = channels
        self.rate = rate
        self.deviceIndex = deviceIndex
        self.framesPerBuffer = framesPerBuffer

class streamHandler:
    def __init__(self, func = None, outputGen = None, streaminfo = None):
        if streaminfo == None:
            self.streaminfo = streamInfo()
        else:
            self.streaminfo = streaminfo

        self.func = func
        self.outputGen = outputGen
        self._maxPrint = 100
        self._currentPrint = 0
        self.kkfini = False

    def _getCallback(self):
        def _streamCallback(in_data, frame_count, time_info, status):
            if self._currentPrint < self._maxPrint:
                self._currentPrint += 1
                data = []

                data = numpy.fromstring(in_data, dtype=numpy.int16).tolist()
                """
                for i in range(frame_count):
                    width = self.streaminfo.width
                    temp = struct.unpack('h', '\x00' * (2 - width) + in_data[i*width : i*width + width])
                    data.append(temp[0] if temp[0] > CUTOFF_THRESHOLD else temp[0])"""

                #print "{0}: {1} frames using {2} bytes".format(time_info, frame_count, len(in_data))
                #print data
                #print ""

                x, y = getfftinfo(data, False)
                freqlst = findFreq(x, y)
                if freqlst != None:
                    notelst = findNote(freqlst)
                    for note in notelst:
                        print convertToLetterNote(note)
                #if freqlst != None:
                #    a = findNote(freqlst)
                #    print a
                #    for c in a:
                #       print convertToLetterNote(int(c))
            else:
                self.kkfini = True
            return (None, pyaudio.paContinue)
        return _streamCallback

    def start(self):
        self._pa = pyaudio.PyAudio()
        self.stream = self._pa.open(format = pyaudio.paInt16,
                                    channels = self.streaminfo.channels,
                                    rate = self.streaminfo.rate,
                                    input = True,
                                    input_device_index = self.streaminfo.deviceIndex,
                                    frames_per_buffer = self.streaminfo.framesPerBuffer,
                                    stream_callback = self._getCallback())

    def stop(self):
        self.stream.stop_stream()
        self.stream.close()
        self._pa.terminate()

if __name__ == "__main__":
    sh = streamHandler(None, None)
    sh.start()
    while not sh.kkfini:
        pass
    sh.stop()
