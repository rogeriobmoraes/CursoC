#include <stdio.h>

int main() {
    int numeros[3], temp;

    // Leitura dos três números e armazenamento no array
    for (int i = 0; i < 3; i++) {
        printf("Digite o número %d: ", i + 1);
        scanf("%d", &numeros[i]);
    }

    // Ordenação do array em ordem decrescente usando o algoritmo de bubble sort
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (numeros[i] < numeros[j]) {
                temp = numeros[i];
                numeros[i] = numeros[j];
                numeros[j] = temp;
            }
        }
    }

    // Imprimir os números em ordem decrescente
    printf("Números em ordem decrescente: ");
    for (int i = 0; i < 3; i++) {
        printf("%d ", numeros[i]);
    }
    printf("\n");

    return 0;
}