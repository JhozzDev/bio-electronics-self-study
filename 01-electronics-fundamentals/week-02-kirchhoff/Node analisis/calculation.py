import numpy as np

R1 = 10
R2 = 10
R3 = 10

Vs = 20


A = np.array([
    [1/R1 + 1/R2, -1/R2],
    [-1/R2, 1/R2 + 1/R3]
])


B = np.array([
    Vs/R1,
    0
])

V = np.linalg.solve(A, B)

V1 = V[0]
V2 = V[1]

print(f"V1 = {V1:.2f} V")
print(f"V2 = {V2:.2f} V")