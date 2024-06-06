import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Time domain:

start = 0
end = 5
N = 1000000
t = np.linspace(start, end, N)
fs = N / (end - start)

# =======Signals========:

# Signal 1:

A_1 = 1
f_1 = 1  # Hz
sig_1 = A_1 * np.sin(2 * np.pi * f_1 * t)

# Signal 2:

A_2 = 3
f_2 = 4  # Hz
sig_2 = A_2 * np.sin(2 * np.pi * f_2 * t)

# Signal 1 + 2:

sig_1a2 = sig_1 + sig_2


# =======Plotting=======:

# Signal 1:

plt.plot(t, sig_1, "black")
plt.axis("off")

plt.savefig("guide_sections/plots/p2_signal_1.png")
plt.clf()

# Signal 2:

plt.plot(t, sig_2, "black")
plt.axis("off")


plt.savefig("guide_sections/plots/p2_signal_2.png")
plt.clf()

# Signal 1 + 2:

plt.plot(t, sig_1a2, "black")
plt.axis("off")


plt.savefig("guide_sections/plots/p2_signal_1a2.png")
plt.clf()