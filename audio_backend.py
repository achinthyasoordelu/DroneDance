import pyaudio
import wave
import numpy
import pyfftw
import math
import matplotlib.pyplot as plt
from scipy.fftpack import fft

frames = 1024
source = wave.open('C:\\Users\\Achinthya\\Desktop\\b2u.wav', 'rb')
sourcePA = pyaudio.PyAudio()
sourceStream = sourcePA.open(format=sourcePA.get_format_from_width(source.getsampwidth()),
                             channels = source.getnchannels(),
                             rate = source.getframerate(),
                             input=True,
                             frames_per_buffer=frames)
print('here')
data = source.readframes(source.getnframes())
print('there')
freqBuffer = numpy.arange(frames)/source.getframerate()
freq = numpy.arange(.1 * frames)
fileTime = int(math.floor(source.getnframes() / source. getframerate()))
sampleCount = int(math.floor(fileTime * source.getframerate() / frames))
inputArray = numpy.empty([sampleCount], dtype = float)
frameArray = numpy.empty([frames], dtype = float)
inputIndex = 0
numSamples = 0
dataIndex = 0
print('here')
while numSamples != sampleCount:
    while inputIndex != frames:
        frameArray[inputIndex] = (sum(data[dataIndex:dataIndex + 3]))
        inputIndex += 1
        dataIndex += 4
    inputArray[numSamples] = numpy.average(frameArray)
    numSamples += 1
    inputIndex = 0
print('there')
'''
print(inputArray)
print(len(inputArray))
print(freqBuffer)
print(len(freqBuffer))

inputArray = numpy.asarray(inputArray)
freqBuffer = numpy.asarray(freqBuffer)
inputArray = inputArray.astype(numpy.complex64)
freqBuffer = freqBuffer.astype(numpy.complex64)

left,right=numpy.split(numpy.abs(numpy.fft.fft(freqBuffer)),2)
tot = numpy.add(left,right)'''
secArray = numpy.empty([fileTime])
inputIndex = 0
dataIndex = 0
print('here')
while inputIndex != fileTime:
    secArray[inputIndex] = numpy.average(inputArray[dataIndex:(int(source.getframerate() / frames) + dataIndex)])
    inputIndex += 1
    dataIndex += int(source.getframerate() / frames)
print('there')
fftSec = fft(data)
plt.plot(fftSec)
plt.show()

