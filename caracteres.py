caracteres = []

for i in range(3):
    caracteres.append(input("Caractere: "))

if all(c in 'aeiou' for c in caracteres):
    print("Os três são vogais!")

# Verifica se pelo menos um caractere é vogal
elif any(c in 'aeiou' for c in caracteres):
    print("Pelo menos 1 caractere é vogal")

# Caso contrário, todos são consoantes
else:
    print("São consoantes")