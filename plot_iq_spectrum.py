import matplotlib.pyplot as plt
import numpy as np
import argparse


def plot_iq(iq, np_data_type, frequency, sample_rate):
    """Plots the power spectrum of the given I/Q data.

    Args:
        iq: String containing alternating I/Q pairs (e.g. IQIQIQIQIQ..etc)
        dtype: numpy dtype to interpret the data as. Rather than dealing
            with a complex type, just treat each I and Q as same type 
            (e.g 32 bit complex float is just 32 bit float)
    """

    #Convert to Numpy array
    iq_array = np.fromstring(iq, dtype = np_data_type)
    #Get Power (Power = I^2 + Q^2)
    all_i = iq_array[::2] ** 2
    all_q = iq_array[1::2] ** 2
    pwr_array = np.add(all_i, all_q)
    #Take FFT
    fft_bins = 1024
    fft_array = np.fft.fft(pwr_array, fft_bins)
    #Shift FFT
    fft_array = np.fft.fftshift(fft_array)
    db_array = 20*np.log10(abs(fft_array))
    #Fill the x axis with correct frequency values
    x_vals = np.linspace(frequency - sample_rate/2.0, frequency + sample_rate /2.0, num=fft_bins)
    #Plot dB values
    plt.plot(x_vals, db_array)
    #Label axes
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("dB")
    #plt.ylim(min(db_array), max(db_array))

    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("frequency", help="Center frequency of the data"
        ,type=int)
    parser.add_argument("sample_rate", help="Sample rate of the data"
        ,type=int)
    parser.add_argument("file_name", help="File that contains the data")
    args = parser.parse_args()
    parser = argparse.ArgumentParser()
    with open(args.file_name, 'r') as data_file:
        iq_data = data_file.read()
        plot_iq(iq_data, np.float32, args.frequency, args.sample_rate)