#C to F
C = input("Enter the degrees Celcius you would like to convert to Fahrenheit: \n")
if type(C) == int or type(C) == float:
    C = float(C)
    F = (C * 1.8) + 32
    print(F)
else:        
    inp = input("Enter Fahrenheit Temperature: \n")
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)