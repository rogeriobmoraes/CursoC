altura = 5

for i in range(altura):
    # Pirâmide da esquerda (alinhada à direita)
    for _ in range(altura - i - 1):
        print(" ", end="")
    for _ in range(i + 1):
        print("#", end="")
    
    # Espaço entre as pirâmides
    print("  ", end="")
    
    # Pirâmide da direita (alinhada à esquerda)
    for _ in range(i + 1):
        print("#", end="")
    
    # Pula para a próxima linha
    print()