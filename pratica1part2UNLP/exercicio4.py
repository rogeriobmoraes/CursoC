numeros = []

for i in range(3):
    numero = int(input("What's n: "))
    if numero == 0:
        break
    numeros.append(numero)
    
minimo1 = float("inf")
minimo2 = float("inf")

for numero in numeros:
    if numero < minimo1:
        minimo2 = minimo1
        minimo1 = numero
    elif numero < minimo2:
        minimo2 = numero

    print(f"Mínimo 1: {minimo1}, Mínimo 2: {minimo2}") # ou min(minimo1, minimo2)