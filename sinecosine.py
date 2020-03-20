import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-1, 1.0, 0.01)

fig, (ax1) = plt.subplots(1)

ax1.plot(t, np.sin(2*np.pi * t), label="sine")
ax1.grid(True)
ax1.set_ylim((-2, 2))

ax1.plot(t, np.cos(2*np.pi * t), label="cosine")
ax1.grid(True)
ax1.set_ylim((-2, 2))

plt.legend()

plt.show()