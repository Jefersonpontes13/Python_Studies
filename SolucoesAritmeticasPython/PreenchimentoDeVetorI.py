

def main():

    valor = int(input())

    for indice in range(10):
        if indice == 0:
            print("N[" + str(indice) + "] = " + str(valor))
        else:
            valor *= 2
            print("N[" + str(indice) + "] = " + str(valor))


if __name__ == '__main__':
    main()
