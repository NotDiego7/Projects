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
print("Y para llegar a completar 5K en 22.3 minutos (un buen promedio) solo tendrias que mantener un ritmo de", ritmo_tiempo,"minutos por vuelta.\n")
tiempo_total = input("Ingresa el tiempo total que corriste:\n")
tiempo_total = int(tiempo_total)
tiempo_per_vuelta = tiempo_total / vueltas
print(f"Tu tiempo por cada vuelta fue de {tiempo_per_vuelta}.")
print("¡Buen trabajo!")