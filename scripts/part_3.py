import matplotlib.pyplot as plt

plt.stem(1, 1, "black", label="Sinus med frekvens 1 i frekvensdomenet", basefmt=" ")
plt.xlim(0, 5)
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.savefig("guide_sections/plots/p3_signal_1_FFTfake.png")
plt.clf()


plt.stem([-1, 1], [0.5, 0.5], "black", label="Sinus med frekvens 1 i frekvensdomenet, faktisk", basefmt=" ")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.xlim(-2.5,  2.5)
plt.ylim(0, 1)

plt.savefig("guide_sections/plots/p3_signal_1_FFTactual.png")
plt.clf()
