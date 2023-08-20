name = input("Escribe tu nombre: \n")
print("hola,", name)
vueltas = input("Ahora escribe las vueltas que diste hoy en numeros por favor: \n")
vueltas = int(vueltas)
print(vueltas, "vueltas, muy bien!\n")
print("Cada vuelta es de 390 metros.\n")
metros_per = 390
metros_total = metros_per * vueltas 
print("Asi que corriste", metros_total ,"metros!\n")
if metros_total < 5000:
    metros_total = metros_total + (5000%metros_total)

vueltas_5k = metros_total / 390
ritmo_tiempo = 22.3 / vueltas_5k 
print("Y para llegar a completar 5K en 22.3 minutos (un buen promedio) solo tendrias que mantener un ritmo de", ritmo_tiempo,"minutos por vuelta.")



#Chained Conditional:
x = 15
if 25 <= x:
    print("less or equal to 25")
elif 20 <= x:
    print("less or equal to 20")
elif 16 <= x:
    print("less or equal to 15")
else:
    print("Less than 14")

if x%3 == 0 and x < 20:
    print("It's divisable by 3 and less than 20.")
elif x > 20:
    print("Higher than 20.")


#1st nested test
if x <= 5:
    print("Less than 5 or 5")
else:
    if x < 10:
        print("Less than 10.")
    else:
        if x < 15:
            print("less than 15")
        else:
            if x < 20:
                print("Less than 20.")

#2nd nested test
if x >= 1 and x <= 10:
    print("1-10")
else:
    if x >= 10 and x <= 20:
        print("10-20")
    else:
        if x >= 20 and x <= 30:
            print("20-30")

#3rd nested test
x = 15
y = 15
if x == y:
    if x == 15:
        if y <= 15:
            print('idk, mane...')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

#F to C (NOT MINE)
inp = input("Enter Fahrenheit Temperature: \n")
fahr = float(inp)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

#C to F
C = input("Enter the degrees celcius you would like to convert to Fahrenhei: \n")
C = float(C)
F = (C * 1.8) + 32
print(F)













