import adi

sdr = adi.Pluto("usb:1.3.5")

sdr.sample_rate = int(1e6)
sdr.tx_lo = int(915e6)
sdr.rx_lo = int(915e6)

sdr.tx_rf_bandwidth = int(1e6)
sdr.rx_rf_bandwidth = int(1e6)

sdr.tx_hardwaregain_chan0 = -10
sdr.rx_hardwaregain_chan0 = 40

print("Pluto configurado correctamente")