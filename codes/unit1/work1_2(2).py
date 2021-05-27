from thinkdsp import read_wave
from thinkdsp import decorate
from thinkdsp import play_wave

wave = read_wave('download2.wav')
start = 1.2
duration = 0.6
segment = wave.segment(start, duration)
spectrum = wave.make_spectrum()
# spectrum.low_pass(3000)
#spectrum.high_pass(5000)
spectrum.band_stop(3000,5000)
wave2 = spectrum.make_wave()

wave2.play('temp.wav')


