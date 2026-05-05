import numpy as np

def generar_tono_complejo(fs, frecuencia_tono, N):
   
    # Generación del vector de tiempo
    t = np.arange(N) / fs
    
    # Generación de la señal compleja: exp(j * 2 * pi * f * t)
    # Esto genera un tono que se desplaza respecto a la portadora fc
    tono = np.exp(1j * 2 * np.pi * frecuencia_tono * t)
    
    # Normalización para asegurar el máximo rango dinámico sin saturar
    tono = tono / np.max(np.abs(tono))
    
    # Convertir a complex64 (formato requerido por pyadi-iio)
    return tono.astype(np.complex64)

def generar_tono_real(fs, frecuencia_tono, N):
    """
    Genera una senoidal real, útil para la modulante en AM.
    """
    t = np.arange(N) / fs
    return np.cos(2 * np.pi * frecuencia_tono * t)

if __name__ == "__main__":
    # Ejemplo de uso según especificaciones técnicas
    fs_test = 1e6      # 1 Msps
    f_test = 100e3     # 100 kHz
    N_test = 8192
    
    señal = generar_tono_complejo(fs_test, f_test, N_test)
    print(f"Tono de {f_test/1e3} kHz generado exitosamente.")
    print(f"Muestras generadas: {len(señal)}")