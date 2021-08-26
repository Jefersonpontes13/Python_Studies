"""coding: utf-8"""


def media_notas(x, y):
    mean = (x + y) / 2
    print(f"media = {mean:.2f}")


def valida_notas():
    x = float(input())

    if 0 <= x <= 10:
        return x
    else:
        print("nota invalida")
        return valida_notas()


def main():
    choice = 1
    while choice == 1:
        i = -1
        j = -1

        while i == -1:
            i = valida_notas()

        while j == -1:
            j = valida_notas()

        media_notas(i, j)
        choice = 3

        while choice != 1 and choice != 2:
            choice = eval(input('novo calculo (1-sim 2-nao)\n'))


if __name__ == '__main__':
    main()
