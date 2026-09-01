V_source = 12
R1 = 4
R2 = 2

R_total = R1 + R2

I = V_source / R_total

V_R1 = I * R1
V_R2 = I * R2

kvl = V_source - V_R1 - V_R2

print(f"Current: {I} A")
print(f"Voltage R1: {V_R1} V")
print(f"Voltage R2: {V_R2} V")
print(f"KVL: {kvl} V")