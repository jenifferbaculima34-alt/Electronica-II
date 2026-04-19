import adi
import numpy as np
import matplotlib.pyplot as plt

fs = int(1e6)
N = 2048

sdr = adi.Pluto("usb:1.3.5")

sdr.sample_rate = fs
sdr.rx_lo = int(915e6)
sdr.rx_rf_bandwidth = fs
sdr.rx_hardwaregain_chan0 = 40
sdr.rx_buffer_size = N

print("Recibiendo...")
data = sdr.rx()

# FFT
fft = np.fft.fftshift(np.fft.fft(data))
freqs = np.fft.fftshift(np.fft.fftfreq(len(data), 1/fs))

plt.plot(freqs, np.abs(fft))
plt.title("Espectro recibido (FFT)")
plt.grid()
plt.show()