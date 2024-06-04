# Importerer nødvendige biblioteker

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

t_start = 0 # Starttid, sekunder
t_slutt = 50 # Slutttid, sekunder 

fs = 1000 # Samplingsfrekvens, Hz
Ts = 1/fs # Samplingsintervall, sekunder 

N = fs * t_slutt # Antall samplepunkter

t = np.linspace(t_start, t_slutt, N) # tidsakse

# én sinus med amplitude 1 og frekvens 1 Hz og én cosinus med amplitude 3 og frekvens 100 Hz:
data = np.sin(2*np.pi*50*t) + 3*np.cos(2*np.pi*100*t) 

# Ta FFT-en:

fouriertransformert_data = sp.fft.fft(data) # Utfører fouriertransformasjonen
fouriertransformert_data = fouriertransformert_data / N # Normaliserer fouriertransformasjonen

amplituder = np.abs(fouriertransformert_data) # Finner amplitudene
faser = np.angle(fouriertransformert_data) # Finner fasene

# Plotting 

frekvenser = sp.fft.fftfreq(len(data), Ts) # Lager en array med frekvenser
plt.plot(frekvenser, amplituder) # Plotter amplituden mot frekvensene
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.savefig("guide_sections/plots/p5_full.png")

plt.clf()

# Om dataen er reell og vi vil kun plotte amplituden for positive frekvenser:
plt.plot(frekvenser, 2*amplituder)
plt.xlim(0, fs/2) # Setter x-aksen til å gå fra 0 til halvparten av samplingsfrekvensen
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.savefig("guide_sections/plots/p5_pos.png")