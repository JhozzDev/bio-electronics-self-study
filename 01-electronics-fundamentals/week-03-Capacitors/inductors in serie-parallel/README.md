# Total Inductance

## Inductors in Series

When inductors are connected in series, their inductances are added together:

$$
L_T = L_1 + L_2 + L_3 + \cdots + L_n
$$

### Example

For:

* \(L_1 = 2H\)
* \(L_2 = 4H\)
* \(L_3 = 6H\)

$$
L_T = 2 + 4 + 6 = 12H
$$

---

## Inductors in Parallel

When inductors are connected in parallel, the reciprocal of the total inductance is equal to the sum of the reciprocals of each inductor:

$$
\frac{1}{L_T} =
\frac{1}{L_1} +
\frac{1}{L_2} +
\frac{1}{L_3} + \cdots
$$

For two inductors, this can also be written as:

$$
L_T = \frac{L_1L_2}{L_1+L_2}
$$

### Example

For:

* \(L_1 = 2H\)
* \(L_2 = 4H\)

$$
L_T = \frac{2(4)}{2+4} = 1.33H
$$

---

## Python Implementation

```python
def inductors_series(inductors):
    return sum(inductors)


def inductors_parallel(inductors):
    return 1 / sum(1 / L for L in inductors)
```

### Key Takeaway

* **Series → add the inductances.**
* **Parallel → add their reciprocals.**
* The result is measured in **Henries (H)**.

> These formulas assume ideal inductors without magnetic coupling between them.
