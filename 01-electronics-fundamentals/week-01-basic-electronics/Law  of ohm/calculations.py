ops = int(input("What options will you choose: \n1. Volts \n2. Resistance\n3. Watts\n4.Amps \n5. Convertion ma -> a\n6. Convertion a -> ma\n"))

match ops:
    case 1:
        R = int(input("R:\n"))
        I = int(input("I:\n"))
        print("Volts:", R*I)
    case 2:
        I = int(input("I:\n"))
        V = int(input("V:\n"))
        print("Resistance:", V/I)
    case 3:
        V = int(input("V:\n"))
        I = int(input("I:\n"))
        print("Watts:", V*I)
    case 4:
        V = int(input("V:\n"))
        R = int(input("R:\n"))
        print("Amps:", V/R)
    case 5:
        ma = float(input("ma:\n"))
        print(f"{ma}mA->{ma*1000}a")
    case 6:
        a = float(input("aa:\n"))
        print(f"{a}A->{a/1000}mA")


    



