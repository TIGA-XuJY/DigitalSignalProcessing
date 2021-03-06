import numpy as np
from thinkdsp import TriangleSignal
from thinkdsp import decorate

triangle = TriangleSignal(440).make_wave(duration=0.01)
triangle.plot()
# decorate(xlabel='Time (s)')
spectrum = triangle.make_spectrum()
print(spectrum.hs[0])
spectrum.hs[0] = 100
triangle.plot(color='gray')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')