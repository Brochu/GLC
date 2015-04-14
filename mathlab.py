# mathlab.py
#------------------------
# Utility functions ported from Mathlab tests for the better part

import sys
import numpy as num
import pylab
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import math

from scipy import fft, arange

THRESHOLD = 0.75
MIN_THRESHOLD = 25

def nextpow2(n):
    exp2 = num.log2(n)
    nextexp = num.ceil(exp2)
    return nextexp

def getfftinfo(signal, drawGraph):
    Fs = 44100
    T = 1.0/Fs
    L = len(signal)

    nfft = 2 ** nextpow2(L)
    Y = fft(signal, int(nfft))
    numUniquePts = num.ceil((nfft+1)/2)
    Y = Y[1:numUniquePts]
    mx = abs(Y)
    mx = mx / L
    mx = mx ** 2

    if nfft % 2:
	mx[2:len(mx)] = mx[2:len(mx)]*2
    else:
	mx[2:len(mx) - 1] = mx[2:len(mx) - 1]*2

    f = arange(numUniquePts - 1) * Fs / nfft
    if drawGraph:
	plt.plot(f, mx, 'r')
	plt.xlabel('freq')
	plt.ylabel('amp')
	plt.show()
    else:
    	return [f, mx]

def findFreq(x, y):
    threshold = THRESHOLD
    min_threshold = MIN_THRESHOLD
    thresholdVal = num.max(y) * threshold
    idx = num.where(y >= thresholdVal)
    temp = idx[0]
    for crotte in idx[0]:
        #print "=======\ntemp: {0}\ncrotte: {1}\ny[crotte]: {2} <? {3}\ntemp[crotte]: {4}\n=======".format(temp, crotte, y[crotte], min_threshold, num.where(temp != crotte)[0])
        if y[crotte] < min_threshold:
            temp = num.where(temp != crotte)[0]

    if len(temp) <= 0:
        return None
    else:
        return x[temp]

def findNote(freqList):
    a = 2.0 ** (1.0 / 12.0)
    f0 = 440.0
    fn = freqList / f0
    notes = num.log(fn) / num.log(a)
    notes = num.round(notes)
    return notes

def convertToLetterNote(note):
    if note == float("-inf") or note == float("inf") or note == None:
        return None
        
    note = int(note)
    letters = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
    return letters[note % 12]

def fonctionReconnaissance(data):
    x, y = getfftinfo(data, False)
    freqlst = findFreq(x, y)
    if freqlst.any():
        return findNote(freqlst)
    else:
        return None

if __name__ == '__main__':
    # Read sound file
    #sampleRate, signal = wav.read(sys.argv[1])
    # get frequencies in signal
    #x, y = getfftinfo(signal, bool(sys.argv[2]))
    #freq = findFreq(x, y)
    #print freq
    #print findNote(freq)
    print convertToLetterNote(-8)
