import Funcoes
from Funcoes import faz_nada
from Funcoes import contador_caracteres
from Classes import Televisao

if __name__ == '__main__':
    faz_nada()
    resultado_adicao = Funcoes.adicao(1, 2)
    televisao = Televisao()
    televisao.power()
    lista_palavras = ['Gato', 'Cachorro', 'Papagaio']
    quantidade_caracteres_palavras = contador_caracteres(lista_palavras)
    print(quantidade_caracteres_palavras)
