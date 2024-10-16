def insertion_sort(lista):
    # Percorre a lista do segundo elemento até o último
    for i in range(1, len(lista)):
        chave = lista[i]  # O elemento a ser inserido na posição correta
        j = i - 1 # j e inicializado com um indice anterior ao primeiro indice

        # Move os elementos da lista que são maiores que a chave para uma posição à frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]  # Desloca o elemento para a direita
            j -= 1
        
        # Insere a chave na posição correta
        lista[j + 1] = chave

# Exemplo de uso
lista = [5, 2, 4, 6, 1, 3]
insertion_sort(lista)
print("Lista ordenada:", lista)






