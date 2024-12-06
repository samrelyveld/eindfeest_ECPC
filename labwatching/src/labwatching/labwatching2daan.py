import nidaqmx
from nidaqmx.constants import AcquisitionType

# Create a task to handle the device
with nidaqmx.Task() as task:
    # Add an analog input channel (e.g., ai0)
    task.ai_channels.add_ai_voltage_chan("Dev1/ai0", 
                                         min_val=-10.0, 
                                         max_val=10.0)

    # Configure the task for continuous sampling
    task.timing.cfg_samp_clk_timing(rate=1000, 
                                    sample_mode=AcquisitionType.CONTINUOUS)

    print("Starting data acquisition... Press Ctrl+C to stop.")

    try:
        while True:
            # Read 100 samples from the channel
            data = task.read(number_of_samples_per_channel=100)
            print(data)  # Process or analyze data here

    except KeyboardInterrupt:
        print("\nStopping acquisition.")