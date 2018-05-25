# plot-iq-psd
Simple Python script to plot the PSD of Complex Float I/Q data

### Dependencies
Matplotlib:

python -mpip install -U pip

python -mpip install -U matplotlib

Tested on Python 2.7.12

### Usage
plot_iq_spectrum.py [-h] frequency sample_rate file_name

Example: 

python plot_iq_spectrum.py 103500000 250000 test_data/103.5Mhz250ksps.iq
