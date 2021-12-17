import wave
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import numpy
import pyaudio

low = 0
high = 0
cut = 0
def processWav():
    global high
    global low
    global cut
    fs, data = wavfile.read('tempfile.wav') # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    if len(b) != 0:
        c = fft(b) # calculate fourier transform (complex numbers list)
        d = len(c)/2  # you only need half of the fft list (real signal symmetry)
        if numpy.average(c) < 0 and numpy.average(c) > -50:
            print('left')
        elif numpy.average(c) <= -50:
            print('down')
        elif numpy.average(c) > 0 and numpy.average(c) < 50:
            print('right')
        elif numpy.average(c) > 175:
            print('spin')
        else:
            print('up')
        if numpy.average(c) < low:
            low = numpy.average(c)
        elif numpy.average(c) > high:
            high = numpy.average(c)
    else:
        cut = 1
    #plt.plot(abs(c[:(d-1)]),'r') 
    #plt.show()

def sliceWav(filePath):
    source = wave.open(filePath, 'rb')
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
def realTime():
    frame = 1024
    wf = wave.open(sys.argv[1], 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()
#sliceWav()
print(low)
print(high)
