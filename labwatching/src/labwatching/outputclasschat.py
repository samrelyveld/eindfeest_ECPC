import nidaqmx
from nidaqmx.constants import AcquisitionType
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


class FrequencyMeasurement:
    def __init__(self):
        self.fit_list = []
        self.datasets = {"Prom 1.5% PEO": self.fit_list}
        self.colors = {"Prom 1.5% PEO": "black"}

    @staticmethod
    def snelheid_functie(x, a, b, x0):
        """
        Example function for curve fitting (not used here).
        """
        return a * (x - x0) ** 2 + b

    def fit_sec(self, data_input):
        """
        Perform FFT analysis on the input data to find the dominant frequency and estimate velocity.
        """
        data = np.array(data_input)
        sampling_rate = 1e3  # Example sampling rate in Hz

        # Perform FFT
        n = len(data)
        fft_result = fft(data)
        frequencies = fftfreq(n, d=1 / sampling_rate)

        # Retain positive frequencies
        positive_frequencies = frequencies[:n // 2]
        positive_fft = np.abs(fft_result[:n // 2])

        # Find the dominant frequency
        dominant_frequency_index = np.argmax(positive_fft)
        dominant_frequency = positive_frequencies[dominant_frequency_index]

        # Velocity calculation (based on laser Doppler principle)
        wavelength = 632.8e-9  # Wavelength in meters
        theta = np.radians(4.5)  # Angle in radians
        velocity = (wavelength / 2) * dominant_frequency / np.sin(theta)

        print(f"Dominant Frequency: {dominant_frequency:.2f} Hz")
        print(f"Estimated Velocity: {velocity:.2f} m/s")
        return int(dominant_frequency)

    def measure(self):
        """
        Perform continuous data acquisition and analyze the data using FFT.
        """
        with nidaqmx.Task() as task:
            # Configure the DAQ task
            task.ai_channels.add_ai_voltage_chan("Dev1/ai0")
            task.timing.cfg_samp_clk_timing(1000.0, sample_mode=AcquisitionType.CONTINUOUS)

            print("Running task. Press Ctrl+C to stop.")

            try:
                total_read = 0

                while True:
                    # Read data from the DAQ device
                    data = task.read(number_of_samples_per_channel=1000)
                    read = len(data)
                    total_read += read

                    print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
                    dominant_frequency = self.fit_sec(data)
                    self.fit_list.append(dominant_frequency)
                    print(f"Current Dominant Frequency: {dominant_frequency} Hz")
                    print(f"Fit List: {self.fit_list}")

            except KeyboardInterrupt:
                print("\nMeasurement stopped by user.")
            finally:
                task.stop()
                print(f"\nAcquired {total_read} total samples.")

                # Plot the histogram of dominant frequencies
                self.plot_histogram()

    def plot_histogram(self):
        """
        Plot a histogram of the dominant frequencies recorded during the measurement.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(self.fit_list, bins=20, color='blue', edgecolor='black', alpha=0.7)
        plt.xlabel('Dominant Frequency (Hz)')
        plt.ylabel('Count')
        plt.title('Histogram of Dominant Frequencies')
        plt.grid(True)
        plt.tight_layout()
        plt.show()


# Instantiate and run the class
if __name__ == "__main__":
    frequency_measurement = FrequencyMeasurement()
    frequency_measurement.measure()
