import numpy as np
import matplotlib.pyplot as plt

# =======Visual rep. of sampling:========

t = np.linspace(0, 3, 10000)
f = np.sin(2 * np.pi * t)

t_sampled = np.linspace(0, 3, 25)
f_sampled = np.sin(2 * np.pi * t_sampled)

plt.title("Kontinuerlig funksjon (f(t))")
plt.plot(t, f, label="f(t)")
xlabel = plt.xlabel("t")
ylabel = plt.ylabel("Amplitude")
plt.legend()
plt.savefig("guide_sections/plots/p4_cont.png")
plt.clf()

plt.title("Kontinuerlig funksjon (f(t)) og sampler (f(n))")
plt.plot(t, f, label="f(t)", zorder=1)
plt.scatter(t_sampled, f_sampled, label="f(n)", color="orange", zorder=2)
xlabel = plt.xlabel("t")
ylabel = plt.ylabel("Amplitude")
plt.legend()
plt.savefig("guide_sections/plots/p4_cont_samp.png")
plt.clf()

plt.title("Sampler (f(n))")
plt.scatter(t_sampled, f_sampled, label="f(n)", color="orange")
xlabel = plt.xlabel("t")
ylabel = plt.ylabel("Amplitude")
plt.legend()
plt.savefig("guide_sections/plots/p4_samp.png")
plt.clf()
