import nidaqmx
from nidaqmx.constants import AcquisitionType
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.fft import fft, fftfreq
from lmfit import models

data = []
fit_list = []

datasets = {
    "Prom 1.5% PEO": fit_list,
}

colors = {
    "Prom 1.5% PEO": "black",
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
    wavelength = 632.8e-9  # Voorbeeld golflengte in meters (532 nm voor groen licht)
    theta = np.radians(4.5)  # Voorbeeld hoek tussen de bundels in graden
    velocity = (wavelength / 2) * dominant_frequency / np.sin(theta)

    print(f"Dominante frequentie: {dominant_frequency:.2f} Hz")
    print(f"Geschatte snelheid: {velocity:.2f} m/s")


def process_and_fit_shifted(dataset, label, color):
    metingen = dataset[0]
    r = dataset[1]

    # Fit the model
    model = models.Model(snelheid_functie)
    result = model.fit(metingen, x=r, a=0, b=np.mean(metingen), x0=0)

    # Extract fitting parameters
    a = result.params['a'].value
    b = result.params['b'].value
    x0 = result.params['x0'].value

    # Calculate the shift to align the peak (x0) to zero
    shift = -x0
    r_shifted = [val + shift for val in r]

    # Generate the shifted fit
    r_fine_shifted = np.linspace(min(r_shifted), max(r_shifted), 200)
    y_fit_shifted = snelheid_functie(r_fine_shifted, a, b, 0)  # x0 is zero after shifting

    # Plot shifted data and fit
    plt.plot(r_shifted, metingen, 'o', label=f"{label} Data (Shifted)", color=color, alpha=0.6)
    plt.plot(r_fine_shifted, y_fit_shifted, '-', label=f"{label} Fit (Shifted)", color=color)



def measure():
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
        task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)
        task.start()
        print("Running task. Press Ctrl+C to stop.")

        try:
            total_read = 0
            total_data = []
            while True:
                data = task.read(number_of_samples_per_channel=1000)
                read = len(data)
                total_read += read
                print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
                fit_list.append(fit_sec(data))
        except KeyboardInterrupt:
            pass
        finally:
            task.stop()
            print(f"\nAcquired {total_read} total samples.")
            process_and_fit_shifted(fit_list)

measure()

    # Main execution for shifting and plotting
plt.figure(figsize=(12, 8))
for label, dataset in datasets.items():
    process_and_fit_shifted(dataset, label, colors[label])
plt.xlabel('r (shifted)')
plt.ylabel('metingen')
plt.title('Quadratic Fits with Peaks Aligned at r=0')
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid()
plt.tight_layout()
plt.show()









