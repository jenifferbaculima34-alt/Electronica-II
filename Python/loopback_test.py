import numpy as np
import matplotlib.pyplot as plt
import time

# Importación de la Arquitectura de Software definida
from config_pluto import iniciar_pluto
from tone_generator import generar_tono_complejo, generar_tono_real
from am_modulator import modular_am
from am_demodulator import demodular_envolvente
from fft_analyzer import calcular_fft

# ==========================================
# 1. INICIALIZACIÓN Y CONFIGURACIÓN
# ==========================================
# Fase A: Configuración del hardware (915 MHz, 1 Msps)
sdr, fs, fc = iniciar_pluto()
if not sdr:
    print("Error: No se pudo inicializar el Adalm-Pluto.")
    exit()

N = 8192
t = np.arange(N) / fs

# ==========================================
# 2. PROCESAMIENTO DE SEÑALES
# ==========================================

# --- Gráfica 1: Tono puro de 100 kHz ---
tono_puro = generar_tono_complejo(fs, 100e3, N)
f_puro, mag_puro = calcular_fft(tono_puro, fs)

# --- Gráfica 2 y 3: Modulación AM ---
fm = 10e3  # Mensaje de 10 kHz
m = 0.5    # Índice de modulación 0.5
señal_am = modular_am(fs, fm, m, N)
f_am, mag_am = calcular_fft(señal_am, fs)

# --- Gráfica 4: Demodulación (Loopback Real con Pluto) ---
sdr.tx_cyclic_buffer = True
sdr.tx(señal_am * (2**14)) # Escalamiento para el DAC
time.sleep(0.5)

# Limpieza de buffer para mejorar la precisión de la captura
for _ in range(5):
    _ = sdr.rx()

data_rx = sdr.rx() / (2**14) # Captura real del Pluto

mensaje_recuperado = demodular_envolvente(data_rx)
mensaje_original = generar_tono_real(fs, fm, N)

# --- AJUSTES DE SINCRONIZACIÓN (Para corregir image_2b4a7f.png) ---
# 1. Normalización de amplitud para que coincidan las alturas
mensaje_rec_norm = mensaje_recuperado / np.max(np.abs(mensaje_recuperado))

# 2. Corrección de desfase temporal (Shift)
# Buscamos la diferencia entre el primer pico de ambas señales
offset = np.argmax(mensaje_rec_norm[:100]) - np.argmax(mensaje_original[:100])
mensaje_rec_fase = np.roll(mensaje_rec_norm, -offset)

# ==========================================
# 3. GENERACIÓN DE GRÁFICAS (ENTREGABLE)
# ==========================================
plt.figure(figsize=(14, 10))
plt.suptitle(" Modulación AM", fontsize=16)

# 1. Espectro del tono puro (100 kHz)
plt.subplot(2, 2, 1)
plt.plot(f_puro / 1e3, mag_puro, color='blue')
plt.title("1. Espectro del Tono Puro (Pico en 100 kHz)")
plt.xlabel("Frecuencia [kHz]"); plt.ylabel("Magnitud [dB]"); plt.grid(True)
plt.xlim([-150, 150])

# 2. Señal modulada AM en tiempo
plt.subplot(2, 2, 2)
plt.plot(t[:400] * 1e3, np.real(señal_am[:400]), color='green')
plt.title("2. Señal Modulada AM en el Tiempo")
plt.xlabel("Tiempo [ms]"); plt.ylabel("Amplitud"); plt.grid(True)

# 3. Espectro de señal AM (Portadora + Bandas)
plt.subplot(2, 2, 3)
plt.plot(f_am / 1e3, mag_am, color='red')
plt.title("3. Espectro AM (Portadora y Bandas Laterales)")
plt.xlabel("Frecuencia [kHz]"); plt.ylabel("Magnitud [dB]"); plt.grid(True)
plt.xlim([-30, 30]) 

# 4. Señal demodulada vs original (Sincronizada)
plt.subplot(2, 2, 4)
plt.plot(t[:400] * 1e3, mensaje_original[:400], label="Original (10 kHz)", alpha=0.6, lw=2)
plt.plot(t[:400] * 1e3, mensaje_rec_fase[:400], '--', label="Demodulada (Sincronizada)", color='black')
plt.title("4. Señal Demodulada vs Original (Fase Corregida)")
plt.xlabel("Tiempo [ms]"); plt.ylabel("Amplitud Normalizada"); plt.legend(); plt.grid(True)

# --- AJUSTE DE ESPACIADO ---
# h_pad evita que las letras de los ejes choquen con los títulos de abajo
plt.tight_layout(pad=3.5, h_pad=4.5, rect=[0, 0.03, 1, 0.95])

# Mostrar resultados finales
print(f"Validación: Tono detectado en {f_am[np.argmax(mag_am)]/1e3} kHz")
plt.show() 

# Limpiar hardware al cerrar
sdr.tx_destroy_buffer()