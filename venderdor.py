produtos = [] 
num_produtos = int(input("Quantos produtos deseja adicionar? "))

for _ in range(num_produtos):
    produto = {
        "Preco": float(input("Preço do produto: ")),
        "qnt": int(input("Quantidade do produto: "))
    }
    produtos.append(produto)  

for i in produtos:
    valor_vendas_totais = 0
    valor_vendas_totais = valor_vendas_totais + i['Preco']
    print(f"Valor total das vendas {valor_vendas_totais}")

for p in produtos:
    print(f"Preço: {p['Preco']}, Quantidade: {p['qnt']}")