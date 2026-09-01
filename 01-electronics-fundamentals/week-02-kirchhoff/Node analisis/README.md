
## What I Learned

Nodal analysis is a method used to find the voltage at different nodes in a circui

It is based on Kirchhoff's Current Law (KCL):

$$
\sum I_{in} = \sum I_{out}
$$

Using Ohm's Law:

$$
I = \frac{V}{R}
$$

## Nodal Analysis Formula

$$
\boxed{\sum \frac{V_{node}-V_{other}}{R}=0}
$$

For a node \(V_1\):

$$
\frac{V_1-V_2}{R_1}+\frac{V_1-V_3}{R_2}+\frac{V_1}{R_3}=0
$$

The reference node is usually **GND**, so:

$$
V_{GND}=0
$$

## Key Points

* Choose a reference node (GND).
* Identify the unknown node voltages.
* Apply KCL to each node.
* Use Ohm's Law to express the currents.
* Solve the equations to find the node voltages.
