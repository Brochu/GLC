import numpy as num
import pylab
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import math

from scipy import fft, arange

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
	threshold = 0.85 # Verifier si il y a un meilleur threashold
	thresholdVal = num.max(y) * threshold
	idx = num.where(y >= thresholdVal)
	return x[idx]

def findNote(freqList):
    a = 2 ** (1.0 / 12.0)
    f0 = 440.0
    fn = freqList / f0
    notes = num.log(fn) / num.log(a)
    notes = num.round(notes)
    print notes

# Read sound file
sampleRate, signal = wav.read('test392.wav')
# get frequencies in signal
x, y = getfftinfo(signal, False)
freq = findFreq(x, y)
findNote(freq)
