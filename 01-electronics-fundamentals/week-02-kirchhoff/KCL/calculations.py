
Vin = 12
R1 = 2
R2 = 4
R3 = 8


Vnode = Vin / (1 + R1/R2 + R1/R3)

I1 = (Vin - Vnode) / R1
I2 = Vnode / R2
I3 = Vnode / R3


print(f"Node Voltage: {Vnode:.2f} V")

print(f"I1: {I1:.2f} A")
print(f"I2: {I2:.2f} A")
print(f"I3: {I3:.2f} A")


print("\nKCL Verification:")

print(f"Current entering: {I1:.2f} A")
print(f"Current leaving: {I2 + I3:.2f} A")

if abs(I1 - (I2 + I3)) < 0.0001:
    print("satisfied")
else:
    print("not satisfied")
