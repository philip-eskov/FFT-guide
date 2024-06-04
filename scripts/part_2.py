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
plt.title("f(t)")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_1.png")
plt.clf()


# Frequency domain, signal 1:

plt.stem(f_1, A_1, "black", basefmt=" ")
plt.xlim(0, 5)
plt.title("f(t), frekvensspekter")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_1_FFT.png")
plt.clf()

# Signal 2:

plt.plot(t, sig_2, "black")
plt.title("g(t)")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_2.png")
plt.clf()

plt.stem(f_2, A_2, "black", basefmt=" ")
plt.xlim(0, 5)
plt.title("g(t), frekvensspekter")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_2_FFT.png")
plt.clf()

# Signal 1 + 2:

plt.plot(t, sig_1a2, "black")
plt.title("h(t)")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_1a2.png")
plt.clf()


# Frequency domain, signal 1 + 2:

fft_1a2 = 2 * abs(sp.fft.fft(sig_1a2)) / N
fft_1a2_freqs = sp.fft.fftfreq(N, 1 / fs)

plt.stem([f_1, f_2], [A_1, A_2], "black", basefmt=" ")
plt.xlim(0, 5)
plt.title("h(t), frekvensspekter")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_1a2_FFT.png")
plt.clf()
