# Inductor Voltage


<img width="778" height="676" alt="image" src="https://github.com/user-attachments/assets/120551fe-8b76-4d39-8625-41ef1027af8f" />


## What I Learned

The voltage across an inductor is determined by how quickly the current changes over time.

The main equation is:

$$
V_L = L\frac{dI}{dt}
$$

Where:

* **\(V_L\)** = Inductor voltage in volts (V)
* **\(L\)** = Inductance in henries (H)
* **\(I\)** = Current in amperes (A)
* **\(t\)** = Time in seconds (s)

### Change in Current

For a constant rate of change, we can use:

$$
\frac{\Delta I}{\Delta t}
$$

For example, if the current changes from 2 A to 10 A in 4 seconds:

$$
\frac{\Delta I}{\Delta t} = \frac{10-2}{4} = 2\ A/s
$$

For a 4 H inductor:

$$
V_L = 4(2) = 8V
$$

### Coding part xd

In Python, `np.gradient()` (Basically divides all the values and then find the shared number) can approximate the rate of change of the current:

```python
dI_dt = np.gradient(I, t)
V = L * dI_dt
```


I really love this one becauses it generates numbers between the first value and the second, the third is the amount of numbers you want to place in.
```python
t = np.linspace(0, 4, 100)
I = np.linspace(2, 10, 100)
```





`np.gradient()` is useful when working with many current and time data points because it calculates the approximate rate of change at each point.

### Key Idea

> The formula in a nutshell is just: The Starting current minus the ending current divided by the time and then multiply by the
> An inductor produces a larger voltage when the current changes more rapidly.
