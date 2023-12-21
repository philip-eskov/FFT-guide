import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Time domain:

start = 0
end = 5
N = 100000
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

plt.plot(t, sig_1, label="Signal 1")
plt.grid()
plt.title("f(t)")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.savefig("guide_sections/plots/p2_signal_1.png")
plt.clf()


# Frequency domain, signal 1:

fft_1 = 2 * abs(sp.fft.fft(sig_1)) / N
fft_1_freqs = sp.fft.fftfreq(N, 1 / fs)

plt.plot(fft_1_freqs, fft_1, label="Signal 1, Frekvensdomene")
plt.xlim(0, 5)
plt.grid()
plt.title("f(t), frekvensdomene")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_1_FFT.png")
plt.clf()


# Signal 2:

plt.plot(t, sig_2, label="Signal 2")
plt.grid()
plt.title("g(t)")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.savefig("guide_sections/plots/p2_signal_2.png")
plt.clf()

fft_2 = 2 * abs(sp.fft.fft(sig_2)) / N
fft_2_freqs = sp.fft.fftfreq(N, 1 / fs)

plt.plot(fft_2_freqs, fft_2, label="Signal 2, Frekvensdomene")
plt.xlim(0, 5)
plt.grid()
plt.title("g(t), frekvensdomene")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_2_FFT.png")
plt.clf()


# Signal 1 + 2:

plt.plot(t, sig_1a2, label="Signal 1 and 2")
plt.grid()
plt.title("h(t)")
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.grid()

plt.savefig("guide_sections/plots/p2_signal_1a2.png")
plt.clf()


# Frequency domain, signal 1 + 2:

fft_1a2 = 2 * abs(sp.fft.fft(sig_1a2)) / N
fft_1a2_freqs = sp.fft.fftfreq(N, 1 / fs)

plt.plot(fft_1a2_freqs, fft_1a2, label="Signal 1 + 2, Frekvensdomene")
plt.xlim(0, 5)
plt.grid()
plt.title("h(t), frekvensdomene")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")

plt.savefig("guide_sections/plots/p2_signal_1a2_FFT.png")
plt.clf()
