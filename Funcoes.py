
def adicao(operando_1, operando_2):
    return operando_1 + operando_2


def subtracao(operando_1, operando_2):
    return operando_1 - operando_2


def multiplicacao(operando_1, operando_2):
    return operando_1 * operando_2


def divisao(dividendo, divisor):
    return dividendo / divisor


def faz_nada():
    pass


def contador_caracteres(lista_palavras):
    if len(lista_palavras) == 1:
        return len(lista_palavras[0])
    else:
        quantidade_caracteres = []
        for palavra in lista_palavras:
            quantidade_caracteres.append(len(palavra))
        return quantidade_caracteres
