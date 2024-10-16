#soma = 0
#cont = 0
maior = 0
posicao = 0
numeros = []

for i in range(10):
    numeros.append(int(input("What's n: ")))
    #soma += numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
        posicao = i + 1

#print(f"Soma dos numeros: {soma}")
print(f"Maior entre os números: {maior}, e esta na posicao {posicao}")
#print(f"Quantidade de números maiores que 5: {cont}")
