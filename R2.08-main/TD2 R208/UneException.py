def divise1(a, b):
    c = a / b
    return c


if __name__ == '__main__':
    div = False
    while not div:
        try:
            a = float(input("Saisir a : "))
            b = float(input("Saisir b : "))
        except ValueError as e:
            print(f"Erreur {e}")
        else:
            c = divise1(a, b)
            print(f"La division de {a} par {b} donne {c}")
            div = True
