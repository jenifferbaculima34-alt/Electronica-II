# Proyecto: Sistema de Comunicación y Procesamiento de Señales con ADALM-Pluto

Este proyecto implementa y valida un sistema de comunicación utilizando Radio Definida por Software (SDR) con el ADALM-Pluto y Python. Incluye la generación de señales, transmisión/recepción, análisis espectral y modulación/demodulación AM.

## Estructura del Repositorio

El proyecto está organizado de la siguiente manera:

* **PHYTON/** - Scripts de Python
  * `config_pluto.py` - Configuración y conexión del hardware
  * `tone_generator.py` - Generador de tonos puros
  * `am_modulator.py` - Modulación de amplitud (AM)
  * `am_demodulator.py` - Demodulación por envolvente
  * `fft_analyzer.py` - Análisis y visualización de la FFT
  * `loopback_test.py` - Script principal de validación (Loopback TX/RX)
* **data/** - Datos experimentales en formato .csv
* **figures/** - Gráficos y diagramas de los resultados
* **docs/** - Informes y documentación en LaTeX (Overleaf)
* **vhdl/** - Archivos de configuración del hardware (plantilla)

## Requisitos Previos

Antes de ejecutar los scripts, asegúrate de tener instaladas las librerías necesarias. Puedes instalarlas ejecutando en tu terminal:

```bash
pip install pyadi-iio numpy matplotlib
