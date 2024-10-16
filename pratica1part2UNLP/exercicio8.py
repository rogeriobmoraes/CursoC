passwd = {}

for user in range(3):
    user = input("User: ")
    passwd[user] = input("Password: ")


print(f"{passwd.items()}")


