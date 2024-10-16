empresas = []
emp_maior = 0
emp_maior_50 = 0

qnt_empresas = int(input("Quantas empresas deseja analisar? "))

for _ in range(qnt_empresas):
    cod_emp = int(input("Código da empresa: "))
    quant_invest = int(input("Quantidade de investimentos: "))
    
    total_invest = 0  # Reiniciar o total de investimentos para cada empresa

    for _ in range(quant_invest):
        var_cada_invest = float(input("Qual o valor do investimento: "))
        total_invest += var_cada_invest  # Somar o valor de cada investimento

    if total_invest > emp_maior:
        emp_maior = cod_emp  # Armazenar o código da empresa com maior investimento

    if total_invest > 50:
        emp_maior_50 += 1  # Contar quantas empresas têm investimento acima de 50

    promedio = total_invest / quant_invest  # Calcular a média dos investimentos
    empresa = { 'codigo': cod_emp, 'promedio': promedio }
    empresas.append(empresa)  # Adicionar a empresa à lista

# Imprimir o promedio de cada empresa
for i in range(len(empresas)):
    print(f"Promedio de investimento da empresa {[i + 1]} : codigo: {empresas[i]['codigo']}: valor: {empresas[i]['promedio']}")

# Imprimir resultados finais
print(f"Empresa com maior montante de investimento: {emp_maior}")
print(f"Quantidade de empresas com investimento superior a 50: {emp_maior_50}")