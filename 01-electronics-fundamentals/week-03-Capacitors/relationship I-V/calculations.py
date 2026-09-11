import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

C = 1
T = sp.symbols("t")
V = 5 * T ** 2


dv_dv = sp.diff(V, T)
I = C * dv_dv

time = np.linspace(0, 1, 1000)
V_function = sp.lambdify(T, V, "numpy")
I_function = sp.lambdify(T, I, "numpy")

current = I_function(time)
voltages = V_function(time)

plt.figure() 
plt.plot(time, voltages) 
plt.xlabel("Time (s)") 
plt.ylabel("Voltage (V)") 
plt.title("Voltage vs Time") 
plt.grid() 
plt.show()

plt.figure() 
plt.plot(voltages, current) 
plt.xlabel("Voltage (V)") 
plt.ylabel("Current (A)") 
plt.title("Capacitor I-V Relationship") 
plt.grid() 
plt.show()