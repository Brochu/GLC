import numpy as num
import pylab
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

from scipy import fft, arange

def nextpow2(n):
	exp2 = num.log2(n)
	nextexp = num.ceil(exp2)
	return nextexp

sampleRate, signal = wav.read('accord.wav')

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
plt.plot(f, mx, 'r')
plt.xlabel('freq')
plt.ylabel('amp')
plt.show()
