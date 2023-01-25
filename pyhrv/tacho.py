# Import
import pyhrv.tools as tools
import numpy as np

# Load sample ECG signal
signal = np.loadtxt('./files/SampleECG.txt')[:, -1]

# Plot Tachogram
tools.tachogram(signal)