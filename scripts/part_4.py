import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# =======Visual rep. of sampling:========

t = np.linspace(0, 3, 10000)
f = np.sin(2 * np.pi * t)

t_sampled = np.linspace(0, 3, 75)
f_sampled = np.sin(2 * np.pi * t_sampled)

plt.plot(t, f, label="f(t)", color="black")
plt.axis("off")
plt.savefig("guide_sections/plots/p4_cont.png")
plt.clf()

plt.plot(t, f, label="f(t)", zorder=1, color="black")
plt.scatter(t_sampled, f_sampled, label="f(n)", color="red", zorder=2)
plt.axis("off")
plt.savefig("guide_sections/plots/p4_cont_samp.png")
plt.clf()

plt.scatter(t_sampled, f_sampled, label="f(n)", color="red")
plt.axis("off")
plt.savefig("guide_sections/plots/p4_samp.png")
plt.clf()


# =======Sampling:========

t = np.linspace(0, 10, 1000) 
sinus = np.sin(t)

plt.title("Sinusfunksjon (f(t))")
plt.plot(t, sinus, label="f(t)")
xlabel = plt.xlabel("t")
ylabel = plt.ylabel("Amplitude")
plt.legend()
plt.savefig("guide_sections/plots/p4_sine.png")
plt.clf()


t = np.linspace(0, 10, 3) 
sinus = np.sin(t)

plt.title("Sinusfunksjon (f(t)), undersamplet")
plt.plot(t, sinus, label="f(t)")
xlabel = plt.xlabel("t")
ylabel = plt.ylabel("Amplitude")
plt.legend()
plt.savefig("guide_sections/plots/p4_sine_usamp.png")
plt.clf()

# =======Spectral leakage========

N = 10000
t_full = np.linspace(0, 3, N)
t_leak = np.linspace(0, 2.35, N)

fs_full = N/3
fs_leak = N/2.35

sig_full = np.sin(2*np.pi*t_full) # 1 Hz
sig_leak = np.sin(2*np.pi*t_leak)

fft_full = abs(2*sp.fft.fft(sig_full)/N)
fft_leak = abs(2*sp.fft.fft(sig_leak)/N)

fft_freq_full = sp.fft.fftfreq(N, 1/fs_full)
fft_freq_leak = sp.fft.fftfreq(N, 1/fs_leak)

plt.plot(t_full, sig_full)
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Sinus, 1 Hz, 0 til 3 sekunder")
plt.savefig("guide_sections/plots/p4_sine_full.png")
plt.clf()

plt.plot(t_leak, sig_leak)
plt.xlabel("Tid (s)")
plt.ylabel("Amplitude")
plt.title("Sinus, 1 Hz, 0 til 2.35 sekunder")
plt.savefig("guide_sections/plots/p4_sine_leak.png")
plt.clf()

plt.stem(fft_freq_full, fft_full, basefmt=" ")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.title("Frekvensspekter, sinus, 1 Hz, 0 til 3 sekunder")
plt.xlim(0, 3)
plt.savefig("guide_sections/plots/p4_fft_full.png")
plt.clf()

plt.stem(fft_freq_leak, fft_leak, basefmt=" ")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.title("Frekvensspekter, sinus, 1 Hz, 0 til 2.35 sekunder")
plt.xlim(0, 3)
plt.savefig("guide_sections/plots/p4_fft_leak.png")
plt.clf()
