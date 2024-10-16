def main():
        char = input("Enter + or - to make the operation: ")

        if char == "+":
            retorno = ler_numeros()
            resultado = sum_numbers(retorno)
            print(f"The of sum is {resultado}")
 
        elif char == "-":
            retorno = ler_numeros()
            resultado = sub_numbers(retorno)
            print(f"The of sub is {resultado}")
        
        else:
            print("Invalid operator")


def ler_numeros():
    numeros = []
    while True:
        numero = int(input("What's n: "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def sum_numbers(numeros):
    aux = 0
    for i in range(len(numeros)):
            aux += numeros[i]
    return aux

def sub_numbers(numeros):
    aux = numeros[0]
    for i in range(1, len(numeros)):
            aux -= numeros[i]
    return aux


main()
