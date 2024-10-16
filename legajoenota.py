def main():
    cont = 0
    contP = 0
    contAD = 0
    while True:
        legajo = int(input("Ingresse o legajo: "))
        if legajo == -1:
            break 
        
        promedio = float(input("Promedio: "))

        if promedio > 6.5:
            contP += 1
        if promedio > 8.5:
            contAD = promedio

        cont += 1
    print_result(cont, contP, contAD)


def print_result(c1, c2, c3):   
    print(f"Total de alunos lidos = {c1}")
    print(f"Alunos que superam 6.5 = {c2}")
    print(f"Alunos destacados = {c3}")


main()