

def main():

    valores = [float(x) for x in input().split()]

    valoresS = valores.copy()

    valoresS.sort()

    if valoresS[2] < valoresS[1] + valoresS[0]:
        print(f"Perimetro = {sum(valores):.1f}")

    else:
        print(f"Area = { ((valoresS[0] + valoresS[1]) * valoresS[2]) / 2 :.1f}")


if __name__ == '__main__':
    main()
