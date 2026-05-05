import numpy as np
# Importamos la lógica de generación desde tu archivo previo
from tone_generator import generar_tono_real 

def modular_am(fs, fm, m, N):
   
    # 1. Generación del mensaje (Tono modulante de 10 kHz)
    # Respetamos el lineamiento: Señal modulante = tono de 10 kHz
    mensaje = generar_tono_real(fs, fm, N)
    
    # 2. Ecuación de Modulación AM
    # Implementación directa sin filtros avanzados ni procesamiento en tiempo real.
    # s(t) = [1 + m * cos(wm*t)]
    # La portadora se genera al desplazar esto a fc (915 MHz) en el hardware.
    señal_am = (1.0 + m * mensaje) + 1j*0
    
    # 3. Normalización para el ADALM-Pluto
    # Escalamos la señal para que el valor máximo sea 1.0 (0 dBFS digital).
    señal_am = señal_am / np.max(np.abs(señal_am))
    
    return señal_am.astype(np.complex64)

if __name__ == "__main__":
    # Configuración de prueba según tabla de especificaciones (Sección 3)
    fs = 1e6   # 1 Msps
    fm = 10e3  # 10 kHz
    m = 0.5    # Índice de modulación: 0.5
    N = 8192
    
    señal = modular_am(fs, fm, m, N)
    
    print("--- Modulador AM (Fase C) ---")
    print(f"Mensaje: {fm/1e3} kHz")
    print(f"Índice m: {m}")
    print("Estado: Modulación básica.")