
## What I Learned

Mesh analysis is a method used to find the currents flowing through different loops (meshes) of a circuit.

The main idea is to apply Kirchhoff's Voltage Law (KVL) to each mesh:

$$
\sum V = 0
$$

For shared resistors, the voltage depends on the difference between the mesh currents:

$$
V_R = R(I_1 - I_2)
$$

After writing the equations, they can be represented as a linear system and solved using Python and NumPy.

The general form is:

$$
A\vec{I} = \vec{V}
$$

This allows Python to calculate the mesh currents automatically.
