import matplotlib.pyplot as plt
import numpy as np
import psutil
import time

# Fixing random state for reproducibility
np.random.seed(19680801)


# create some data to use for the plot


t = np.arange(0.0, 100.0, 1)

r = np.exp(-t[:1000] / 0.05)  # impulse response

x = np.random.randn(len(t))

s = np.convolve(x, r)[:len(x)] * dt  # colored noise

plt.plot(t,s)

plt.show()
