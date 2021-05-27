from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate
cos_sig = CosSignal(freq=220, amp=1.0, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)
oadd = SinSignal(freq=500, amp=0.7, offset=0)
# mix = sin_sig + cos_sig
mix = sin_sig + cos_sig + oadd
# mix.plot()
# decorate(xlabel='Time (s)')
wave = mix.make_wave(duration=2, start=0, framerate=11025)
wave.play('temp.wav')
spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')


