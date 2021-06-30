from thinkdsp import decorate
from thinkdsp import read_wave
wave = read_wave('72475__rockwehrmann__glissup02.wav')
wave.play()
wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')