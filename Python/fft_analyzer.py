import numpy as np
import matplotlib.pyplot as plt

def calcular_fft(data, fs):
    
    N = len(data)
    
    # Aplicar ventana de Hamming para reducir el "leakage" (fuga espectral)
    # Recomendado en la Metodología Fase B
    window = np.hamming(N)
    data_windowed = data * window
    
    # Calcular FFT y centrar con fftshift
    fft_raw = np.fft.fft(data_windowed)
    fft_shifted = np.fft.fftshift(fft_raw)
    
    # Convertir a magnitud en dB (escala logarítmica para el informe IEEE)
    # Se añade 1e-12 para evitar log(0)
    mag_db = 20 * np.log10(np.abs(fft_shifted) / N + 1e-12)
    
    # Generar el eje de frecuencias
    freqs = np.fft.fftshift(np.fft.fftfreq(N, 1/fs))
    
    return freqs, mag_db

def graficar_espectro(freqs, mag_db, titulo="Espectro FFT"):
    """
    Función auxiliar para visualizar el espectro de forma estandarizada.
    """
    plt.plot(freqs / 1e3, mag_db) # Frecuencia en kHz
    plt.title(titulo)
    plt.xlabel("Frecuencia [kHz]")
    plt.ylabel("Magnitud [dB]")
    plt.grid(True)