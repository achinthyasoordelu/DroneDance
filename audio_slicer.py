import wave

source = wave.open('C:\\Users\\Achinthya\\Desktop\\b2u.wav', 'rb')
frameRate = source.getframerate()
channels = source.getnchannels()
sampleWidth = source.getsampwidth()

frameIndex = 0
while frameIndex <= source.getnframes():
    source.setpos(frameIndex*frameRate)
    sampleData = source.readframes(int((end - frameIndex) * frameRate))
    frameIndex += 88200
