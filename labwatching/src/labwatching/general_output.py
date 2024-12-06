import nidaqmx
from nidaqmx.constants import AcquisitionType
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def sine_model(t, A, f, phi, C):
    return A * np.sin(2 * np.pi * f * t + phi) + C

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
            total_data += (data)
            total_read += read
            print(f"Acquired data: {read} samples. Total {total_read}.", end="\r")
    except KeyboardInterrupt:
        pass
    finally:
        task.stop()
        print(total_data)
        print("")
        print("")
        print(len(total_data))
        print(len(data))
        print(f"\nAcquired {total_read} total samples.")

        # Create an array of time points corresponding to the data (assuming uniform sampling)
        t = np.arange(0, 1, 0.001)

        # Fit the sine model to the data
        params, covariance = curve_fit(sine_model, t, data, p0=[np.max(data)-np.min(data), 0.1, 0, np.mean(data)])

        # Extract the fitted parameters
        A_fit, f_fit, phi_fit, C_fit = params

        # Generate the fitted sine wave using the fitted parameters
        fitted_data = sine_model(t, A_fit, f_fit, phi_fit, C_fit)

        # Plot the original data and the fitted sine wave
        plt.figure(figsize=(10, 6))
        plt.plot(t, data, label='Original Data', marker='o', markersize=4)
        plt.plot(t, fitted_data, label='Fitted Sine Wave', linestyle='-', color='r')
        plt.legend()
        plt.xlabel('Sample Index')
        plt.ylabel('Voltage')
        plt.title('Sine Wave Fit to Data')
        plt.show()

        # Print the fitted parameters
        print(f"Amplitude (A): {A_fit}")
        print(f"Frequency (f): {f_fit} Hz")
        print(f"Phase (phi): {phi_fit} radians")
        print(f"Vertical offset (C): {C_fit}")



