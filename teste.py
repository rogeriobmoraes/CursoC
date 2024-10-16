for i in range(5):
    for _ in range(5 - i - 1):
        print(" ", end="")

    for _ in range(i + 1):
        print("#", end="")
    print()


