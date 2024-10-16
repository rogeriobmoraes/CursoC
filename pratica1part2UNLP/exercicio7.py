def main():
    corrida_ordenada = input_piloto()
    extrair_orden(corrida_ordenada)

def input_piloto():
    corrida = []
    for i in range(4):
        nome = input("Nome do piloto: ")
        tempo = float(input("Tempo do piloto: "))

        piloto = {"nome": nome, "tempo": tempo}
        corrida.append(piloto)

    corrida_ordenada = sorted(corrida, key=lambda item: item['tempo'])
    
    return corrida_ordenada


def extrair_orden(corrida_ordenada):
    primeiro = corrida_ordenada[0]
    segundo = corrida_ordenada[1]
    penultimo = corrida_ordenada[len(corrida_ordenada) - 2]
    ultima = corrida_ordenada[len(corrida_ordenada) - 1]

    print(f"Primeiro: {primeiro['nome']}, Tempo: {primeiro['tempo']}")
    print(f"Segundo: {segundo['nome']}, Tempo: {segundo['tempo']}")
    print(f"Penultimo: {penultimo['nome']}, Tempo: {penultimo['tempo']}")
    print(f"Ultimo: {ultima['nome']}, Tempo: {ultima['tempo']}")


main()

