# What did I learn today?

Kirchhoff's Current Law (KCL) is based on **"Inputs and Outputs"**. The current entering a node must be equal to the current leaving the node.

**Current Input = Current Output**

For instance:

```text
10A = 5A + I
10A = 5A + 5A
I = 5A
```

Because:

```text
Current Input (10A) = Current Output (5A + I)
```

## Node

A **node** is an intersection between two or more branches. It is often represented as a point where the elements of a circuit connect.

## Branch

A **branch** is a path between nodes that contains a circuit element, such as a resistor.

## KCL Formula

The algebraic sum of all currents at a node is equal to zero:

```text
ΣI = 0
```

This means:

```text
Current entering = Current leaving
```

## Finding Current with a Resistor

To find the current through a resistor, we use Ohm's Law as usual:

```text
I = V / R
```

Then, that current can be used in our KCL equation.

## Finding the Node Voltage

When there is **only one unknown node voltage**, we can use KCL to find the node voltage.

For example:

```text
        12V
         |
        2Ω
         |
       Vnode
       /   \
     4Ω     8Ω
     |       |
    GND     GND
```

The KCL equation is:

```text
(12 - Vnode) / 2 = Vnode / 4 + Vnode / 8
```

Multiply everything by 8:

```text
4(12 - Vnode) = 2Vnode + Vnode
```

Distribute:

```text
48 - 4Vnode = 2Vnode + Vnode
```

Move the terms:

```text
48 = 7Vnode
```

Divide:

```text
Vnode = 48 / 7
```

Therefore:

```text
Vnode ≈ 6.86V
```

## Finding the Currents

Once we have the node voltage, we can find the current in each branch.

For the resistor connected to the 12V source:

```text
I = (Vin - Vnode) / R
```

For the resistors connected from the node to ground:

```text
I = Vnode / R
```

So:

```text
I1 = (12 - Vnode) / 2
I2 = Vnode / 4
I3 = Vnode / 8
```

Then we can verify KCL:

```text
I1 = I2 + I3
```

### Important

This method is useful when there is **only one unknown node voltage**.

If a circuit has multiple unknown node voltages, we need to create multiple KCL equations and solve them together.
