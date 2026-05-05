import adi

def iniciar_pluto(uri="usb:1.5.5"):
    """
    Configura el ADALM-Pluto con los parámetros de los lineamientos.
    """
    try:
        sdr = adi.Pluto(uri)
        
        # Parámetros básicos (Sección 3 de los lineamientos)
        fs = int(1e6)          # 1 Msps
        fc = int(915e6)        # 915 MHz
        
        sdr.sample_rate = fs
        
        # Configuración TX
        sdr.tx_lo = fc
        sdr.tx_rf_bandwidth = fs
        sdr.tx_hardwaregain_chan0 = -10  # Especificación técnica: -10 dBm
        
        # Configuración RX
        sdr.rx_lo = fc
        sdr.rx_rf_bandwidth = fs
        # Usamos AGC slow_attack para cumplir con la ganancia de 50dB sin saturar
        sdr.gain_control_mode_chan0 = "slow_attack" 
        
        print(f"ADALM-Pluto configurado en {fc/1e6} MHz a {fs/1e6} Msps.")
        return sdr, fs, fc
    
    except Exception as e:
        print(f"Error al conectar con el Pluto: {e}")
        return None, None, None

if __name__ == "__main__":
    # Prueba rápida de conexión
    sdr, fs, fc = iniciar_pluto()
    if sdr:
        print("Prueba de configuración exitosa.")