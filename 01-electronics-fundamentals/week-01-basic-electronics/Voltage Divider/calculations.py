# Two Resistances circuit divider
r2 = 20
r1 = 10
voltage_in_1 = 12
resistances_cal = r2 / (r1+r2)
output_voltage = voltage_in_1 * resistances_cal 
print("Voltage Output: ", output_voltage, "V")

# When there's no resistance value
amperes = 0.05
voltage_in_2 = 20
r1 = 0
r2 = 0 
resistances_total = voltage_in_2 / amperes

output_voltage_formula = voltage_in_2 * (r2/resistances_total)
print("Output_Voltage_2: ", output_voltage_formula)

