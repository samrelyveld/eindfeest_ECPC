import nidaqmx
from nidaqmx.constants import AcquisitionType
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.fft import fft, fftfreq
from lmfit import models

fit_list = []

datasets = {
    "Prom 1.5% PEO": fit_list
}

colors = {
    "Prom 1.5% PEO": "black"
}



def snelheid_functie(x, a, b, x0):
    return a * (x - x0) ** 2 + b

def fit_sec(data_input):
    # Data van de fotodetector
    data = np.array(data_input)  # Vul hier de fotodetectordata in
    sampling_rate = 1e3  # Voorbeeld sampling rate in Hz (pas aan naar jouw systeem)

    # Bereken de FFT
    n = len(data)
    print ("n= ", n)
    fft_result = fft(data)
    frequencies = fftfreq(n, d=1/sampling_rate)  # Frequenties bij FFT

    # Behoud alleen de positieve frequenties
    positive_frequencies = frequencies[:n // 2]
    positive_fft = np.abs(fft_result[:n // 2])

    # Vind de dominante frequentie
    dominant_frequency_index = np.argmax(positive_fft)
    dominant_frequency = positive_frequencies[dominant_frequency_index]

    # Visualiseer de frequentiespectrum

    # Snelheid berekening
    wavelength = 632.8e-9 
    theta = np.radians(4.5) 
    velocity = (wavelength / 2) * dominant_frequency / np.sin(theta)

    print(f"Dominante frequentie: {dominant_frequency:.2f} Hz")
    print(f"Geschatte snelheid: {velocity:.2f} m/s")
    return int(dominant_frequency)


def measure():
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        task.start()
        print("Running task. Press Ctrl+C to stop.")

        try:
            total_read = 0

            while True:
                data = task.read(number_of_samples_per_channel=1000)
                read = len(data)
                total_read += read
                print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
                print("fit sec =",(fit_sec(data)))
                fit_list.append(fit_sec(data))
                print(fit_list)
        except KeyboardInterrupt:
            pass
        finally:
            task.stop()
            print(f"\nAcquired {total_read} total samples.")
            plt.figure(figsize=(10, 6))
            plt.hist(fit_list, bins=20, color='blue', edgecolor='black', alpha=0.7)
            plt.xlabel('Dominant Frequency (Hz)')
            plt.ylabel('Count')
            plt.title('Histogram of Dominant Frequencies')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
                    
            

measure()

    # Main execution for shifting and plotting











