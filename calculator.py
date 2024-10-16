def get_int(s):
    while True:
        try:
            return int(input(s))
        except ValueError:
            pass

def main():
    x = get_int("x: ")
    y = get_int("y: ")

    print(x * y)


main()