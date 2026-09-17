import numpy as np
import matplotlib.pyplot as plt

L = 2


t = np.linspace(0, 4, 100)
I = np.linspace(2, 10, 100)


dI_dt = np.gradient(I, t)
V = L * dI_dt

plt.plot(t, V)

plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Inductor Voltage")
plt.grid()
plt.show()
