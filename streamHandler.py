import pyaudio
import time
import struct

CUTOFF_THRESHOLD = 0.001

DEFAULT_WIDTH = 4 # Nombre de byte par sample
DEFAULT_CHANNELS = 1
DEFAULT_RATE = 44100
DEFAULT_DEVICE_INDEX = 0
DEFAULT_FRAMES_PER_BUFFER = 128

class streamInfo:
    def __init__(self, width = DEFAULT_WIDTH, channels = DEFAULT_CHANNELS, rate = DEFAULT_RATE, deviceIndex = DEFAULT_DEVICE_INDEX, framesPerBuffer = DEFAULT_FRAMES_PER_BUFFER):
        self.width = width
        self.channels = channels
        self.rate = rate
        self.deviceIndex = deviceIndex
        self.framesPerBuffer = framesPerBuffer

class streamHandler:
    def __init__(self, func, outputGen, streaminfo = None):
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
                
                for i in range(frame_count):
                    temp = struct.unpack('f', in_data[0 : 4])
                    data.append(temp[0] if temp[0] > CUTOFF_THRESHOLD else 0.0)
                    
                print "{0}: {1} frames using {2} bytes".format(time_info, frame_count, len(in_data))
                print data
                print ""
            else:
                self.kkfini = True
            return (None, pyaudio.paContinue)
        return _streamCallback
    
    def start(self):
        self._pa = pyaudio.PyAudio()
        self.stream = self._pa.open(format = self._pa.get_format_from_width(self.streaminfo.width),
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
        
sh = streamHandler(None, None)
sh.start()
while not sh.kkfini:
    pass
sh.stop()