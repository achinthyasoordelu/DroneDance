#!/bin/sh
#import pyglet
import wave
from subprocess import call
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfilex          
import numpy

low = 0
high = 0
cut = 0
def processWav():
    global high
    global low
    global cut
    #song = pyglet.media.load('tempfile.wav')
    fs, data = wavfile.read('tempfile.wav') # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    command = ''
    if len(b) != 0:
        c = fft(b) # calculate fourier transform (complex numbers list)
        #d = len(c)/2  # you only need half of the fft list (real signal symmetry)
        if numpy.average(c) < 0 and numpy.average(c) > -50:
            command = 'left'
        elif numpy.average(c) <= -50:
            commdand = 'down'
        elif numpy.average(c) > 0 and numpy.average(c) < 50:
            command = 'right'
        elif numpy.average(c) > 175:
            command = 'spin'
        else:
            command = 'up'
        if numpy.average(c) < low:
            low = numpy.average(c)
        elif numpy.average(c) > high:
            high = numpy.average(c)
	print command
        call(["./client", command])
    else:
        cut = 1
	call(["./client", "stop"])
    #song.play()
    #plt.plot(abs(c[:(d-1)]),'r') 
    #plt.show()

def sliceWav():
    source = wave.open('/home/linaro/Desktop/piano2.wav', 'rb')
    frameRate = source.getframerate()
    channels = source.getnchannels()
    sampleWidth = source.getsampwidth()
    source.setpos(0)
    while source.tell() <= source.getnframes() and cut != 1:
        sampleData = source.readframes(int((frameRate)))
        newAudio = wave.open('tempfile.wav', 'w')
        newAudio.setnchannels(channels)
        newAudio.setsampwidth(sampleWidth)
        newAudio.setframerate(frameRate)
        newAudio.writeframes(sampleData)
        newAudio.close()
        processWav()
sliceWav()
print(low)
print(high)
