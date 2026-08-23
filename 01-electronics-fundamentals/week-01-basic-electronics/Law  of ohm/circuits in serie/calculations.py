Voltage = 12
Resistance1 = 2000
Resistance2 = 4000
Resistance3 = 6000
Total_resistance = Resistance1 + Resistance2 + Resistance3

Ampers = Voltage / Total_resistance

Voltage_drop_1 = Ampers * Resistance1
Voltage_drop_2 = Ampers * Resistance2
Voltage_drop_3 = Ampers * Resistance3
Voltage_1 = Voltage - Voltage_drop_1
Voltage_2 = Voltage_1 - Voltage_drop_2
Voltage_3 = Voltage_2 - Voltage_drop_3


print(
    "Rt:", Total_resistance
)

print(
    "Ampers:", Ampers
)


print(
    "Drops: ", Voltage_drop_1, Voltage_drop_2, Voltage_drop_3
)


print(
    "Voltages:", Voltage, Voltage_1, Voltage_2, Voltage_3
)