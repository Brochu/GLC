from streamHandler import *
import pyaudio
import itertools
import sys

def hacklol(kk):
    if ord(kk) >= 128:
        return 'e'
    else:
        return kk

pa = pyaudio.PyAudio()
deviceCount = pa.get_device_count()
validDevices = []

for i in range(deviceCount):
    device = pa.get_device_info_by_index(i)
    if device['maxInputChannels'] <= 0L:
        continue
        
    validDevices.append(i)
    deviceName = device['name']
    deviceName = ''.join(map(hacklol, deviceName))
    print "Device {0}: {1}".format(i, deviceName)
    
pa.terminate()

sys.stdout.write('\nCHOOSE YOUR DESTINY: ')
chosenDeviceIndex = raw_input()

if chosenDeviceIndex.upper() == "EXIT":
    exit()
    
chosenDeviceIndex = int(chosenDeviceIndex)

if not chosenDeviceIndex in validDevices:
    raise IOError("Invalid input device")

si = streamInfo(deviceIndex = chosenDeviceIndex)
sh = streamHandler(streaminfo = si)
sh.start()

while not sh.kkfini:
    pass