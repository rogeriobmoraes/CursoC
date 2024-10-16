#include <stdio.h>

int main(void)
{
    int tam = 6, aux, vetor1[6] = {1, 2, 3, 4, 5, 6};

    // Imprimir array original
    printf("Array original:\n");
    for (int i = 0; i < 6; i++)
    {
        printf("%d ", vetor1[i]);
    } 
    printf("\n");

    // Inverter os elementos do vetor
    for (int i = 0; i < tam / 2; i++)
    {
        aux = vetor1[i];
        vetor1[i] = vetor1[tam - 1 - i];
        vetor1[tam - 1 - i] = aux;       
    }

    // Imprimir array modificado
    printf("Array modificado:\n");
    for (int i = 0; i < 6; i++)
    {
        printf("%d ", vetor1[i]);
    } 
    printf("\n"); // Para adicionar uma nova linha

    return 0;
}