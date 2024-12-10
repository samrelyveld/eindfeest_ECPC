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

def gaussian(x, amp, mean, stddev):
    """Gaussian function to fit to the histogram."""
    return amp * np.exp(-(x - mean)**2 / (2 * stddev**2))

def fit_sec(data_input):
    # Data van de fotodetector
    data = np.array(data_input)  # Vul hier de fotodetectordata in
    sampling_rate = 1e3  # Voorbeeld sampling rate in Hz (pas aan naar jouw systeem)

    # Bereken de FFT
    n = len(data)
    fft_result = fft(data)
    frequencies = fftfreq(n, d=1/sampling_rate)  # Frequenties bij FFT

    # Behoud alleen de positieve frequenties
    positive_frequencies = frequencies[:n // 2]
    positive_fft = np.abs(fft_result[:n // 2])

    # Vind de dominante frequentie
    dominant_frequency_index = np.argmax(positive_fft)
    dominant_frequency = positive_frequencies[dominant_frequency_index]
    
    plt.figure(figsize=(10, 6))
    plt.plot(positive_frequencies, positive_fft)
    plt.title("FFT van de fotodetectordata")
    plt.xlabel("Frequentie (Hz)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()
    
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
            
            # Perform Gaussian fit on the histogram
            data_hist, bins_hist = np.histogram(fit_list, bins=20, density=True)
            bin_centers = (bins_hist[:-1] + bins_hist[1:]) / 2
            
            # Fit a Gaussian to the histogram data
            popt, _ = curve_fit(gaussian, bin_centers, data_hist, p0=[1, np.mean(fit_list), np.std(fit_list)])

            # Plot the Gaussian fit
            plt.plot(bin_centers, gaussian(bin_centers, *popt), 'r-', label='Gaussian fit')
            plt.legend()
            plt.show()
                    
            

measure()

    # Main execution for shifting and plotting











