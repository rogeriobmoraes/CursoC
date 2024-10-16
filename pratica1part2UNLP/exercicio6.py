codigo = []
preco = []
maisbarato = []
contpares = 0


for i in range(3):
    cod = int(input("Digite o Codigo do produto: "))
    preco_produto = float(input("Digite o preço do produto: "))
    codigo.append(cod)
    preco.append(preco_produto)

for j in range(len(preco)-1):
    if preco[j] < preco[j + 1]: 
        maisbarato.append(codigo[j]) 

strmaisbarato = ', '.join(map(str, maisbarato))
print(f"Códigos dos produtos mais baratos: {strmaisbarato}")

for l in range(len(preco)):
    if codigo[l] % 2 == 0 and preco[l] < 16.00:
        contpares += 1

print(f"Produtos com código par e preço inferior a 16: {contpares}")

    