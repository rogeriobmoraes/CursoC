alunos = {}
maior_que_oito = 0
igual_a_sete = 0

while True:
    nome = input("Nome: ")
    if nome == "Zidane Zinedine":
        break
    nota = float(input("Nota: "))
    alunos[nome] = nota  # Armazena o nome como chave e a nota como valor

for nome, nota in alunos.items():  # Itera sobre os pares de nome e nota
    if nota >= 8.0:
        maior_que_oito += 1
    elif nota == 7.0:
        igual_a_sete += 1

print(f"Quantidade de alunos aprovados com nota maior que 8: {maior_que_oito}")
print(f"Quantidade de alunos aprovados com nota igual a 7: {igual_a_sete}")