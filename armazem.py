while True:
    cod = int(input("Codigo do produto: "))
    precoA = float(input("Preco atual: "))
    NovoP = float(input("Novo preco: "))
    if NovoP > (precoA + precoA * 10/100):
        print(f"Novo preco {NovoP} supera 10%")
    else:
        print(f"Novo preco {NovoP.02f}, nao supera 10%")

    if cod == 32767:
        break
