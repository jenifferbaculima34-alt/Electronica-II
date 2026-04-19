import adi
import numpy as np
import time

fs = int(1e6)
N = 1024

sdr = adi.Pluto("usb:1.3.5")
sdr.sample_rate = fs
sdr.tx_lo = int(915e6)
sdr.tx_rf_bandwidth = fs
sdr.tx_hardwaregain_chan0 = -10
sdr.tx_cyclic_buffer = True

t = np.arange(N) / fs

# tono de prueba (10 kHz como dice tu guía)
tone = np.cos(2*np.pi*10e3*t)

tone = tone / np.max(np.abs(tone))
tx = tone.astype(np.complex64)

print("Transmitiendo tono...")
sdr.tx(tx)

time.sleep(5)