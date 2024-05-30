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
sig_1 = A_1 * np.cos(2 * np.pi * f_1 * t)

# =======Plotting=======:

# Frequency domain, signal 1:

# fft_1 = 2 * abs(sp.fft.fft(sig_1)) / N
fft_1_freqs = sp.fft.fftfreq(N, 1 / fs)

# plt.stem(fft_1_freqs, fft_1, label="Sinus med frekvens 1 i frekvensdomenet", basefmt=" ")
# plt.xlim(0, 5)
# plt.grid()
# plt.title("f(t), frekvensdomene")
# plt.xlabel("Frekvens (Hz)")
# plt.ylabel("Amplitude")

# plt.savefig("guide_sections/plots/p3_signal_1_FFTfake.png")
# plt.clf()

# fft_1 = abs(sp.fft.fft(sig_1)) / N

# plt.stem(fft_1_freqs, fft_1, label="Sinus med frekvens 1 i frekvensdomenet, faktisk", basefmt=" ")
# plt.grid()
# plt.title("f(t), frekvensdomene")
# plt.xlabel("Frekvens (Hz)")
# plt.ylabel("Amplitude")
# plt.xlim(-2.5, 2.5)

# plt.savefig("guide_sections/plots/p3_signal_1_FFTactual.png")
# plt.clf()


plt.plot(fft_1_freqs, np.angle(sp.fft.fft(A_1 * np.cos(2 * np.pi * f_1 * t))))
plt.plot(fft_1_freqs, np.angle(sp.fft.fft(A_1 * np.sin(2 * np.pi * f_1 * t))))
# plt.xlim(-2.5, 2.5)

plt.show()