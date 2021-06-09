
contador_caracteres = lambda lista_palavras: [len(palavra) for palavra in lista_palavras]

calculadora = {
    'adicao': lambda numero_1, numero_2: numero_1 + numero_2,
    'subtracao': lambda numero_1, numero_2: numero_1 - numero_2,
    'multiplicacao': lambda numero_1, numero_2: numero_1 * numero_2,
    'divisao': lambda numero_1, numero_2: numero_1 / numero_2
}

if __name__ == '__main__':
    quantidade_caracteres_ovo = contador_caracteres(['ovo'])
    print(quantidade_caracteres_ovo)

    soma = calculadora['adicao']
    soma_4_4 = soma(4, 4)
    print(soma_4_4)
