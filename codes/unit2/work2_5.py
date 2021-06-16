from thinkdsp import TriangleSignal
from thinkdsp import decorate
def filter_spectrum(spectrum):
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave = TriangleSignal(freq=440).make_wave(duration=0.5)
spectrum = wave.make_spectrum()
# spectrum.plot(high=10000)
# decorate(xlabel='Frequency (Hz)')
filter_spectrum(spectrum)
# spectrum.plot(high=10000)
# decorate(xlabel='Frequency (Hz)')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')

