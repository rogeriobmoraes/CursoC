n = float(input("What's n: "))

for i in range(9):
    num = float(input("What's num: "))
    if num == n * 2:
        print("Dobro inserido")
        break
else:
    print("Dobro nao inserido")        
