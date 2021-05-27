from thinkdsp import read_wave
from thinkdsp import decorate

wave1 = read_wave('download.wav')
spectrum1 = wave1.make_spectrum()
spectrum1.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

wave2 = read_wave('download2.wav')
start = 1.2
duration = 0.6
segment2 = wave2.segment(start, duration)
spectrum2 = segment2.make_spectrum()
spectrum2.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

