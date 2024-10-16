numeros = []

while True:
    numero = int(input("What's n: "))
    if numero == 100:
        numeros.append(numero)
        break
    numeros.append(numero)
   
    
minimo = 0
maximo = 0
soma = 0

for i in range(len(numeros)):
        if numeros[i] < minimo:
            minimo = numeros[i]
        elif numeros[i] > maximo:
            maximo = numeros[i]
        soma += numeros[i]


print(f"Mínimo: {minimo}, Maximo: {maximo}, soma: {soma}") 