import pyaudio
import time

DEFAULT_WIDTH = 2 # Nombre de byte par sample
DEFAULT_CHANNELS = 2
DEFAULT_RATE = 44100
DEFAULT_DEVICE_INDEX = 0

class streamInfo:
    def __init__(self, width = DEFAULT_WIDTH, channels = DEFAULT_CHANNELS, rate = DEFAULT_RATE, deviceIndex = DEFAULT_DEVICE_INDEX):
        self.width = width
        self.channels = channels
        self.rate = rate
        self.deviceIndex = deviceIndex

class streamHandler:
    def __init__(_self, func, outputGen, streaminfo = None):
        if streaminfo == None:
            self.streaminfo = streamInfo()
        else:
            self.streaminfo = streaminfo
            
        self.func = func
        self.outputGen = outputGen
        self._maxPrint = 100
        self._currentPrint = 0
    
    def _getCallback(self):
        def _streamCallback(in_data, frame_count, time_info, status):
            if self._currentPrint < self._maxPrint:
                self._currentPrint += 1
                print in_data
            return (None, pyaudio.paContinue)
        return _streamCallback
    
    def start(self):
        self._pa = pyaudio.PyAudio()
        self.stream = self._pa.open(format = p.get_format_from_width(self.streaminfo.width),
                                    channels = self.streaminfo.channels,
                                    rate = self.streaminfo.rate,
                                    input = True,
                                    input_device_index = self.streaminfo.deviceIndex,
                                    stream_callback = _getCallback())
    
    def stop(self):
        self.stream.stop_stream()
        stream.close()
        self._pa.terminate()