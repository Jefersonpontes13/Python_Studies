"""coding: utf-8"""

from threading import Thread
import time


def carro(identificador, velocidade):
    trajeto = 0
    print(f'\nCarro {identificador} | Posição: {trajeto}\n')

    while trajeto <= 100:

        trajeto += velocidade
        time.sleep(0.5)
        print(f'Carro {identificador} | Posição: {trajeto}\n')


if __name__ == '__main__':
    t_carro1 = Thread(target=carro, args=[1, 1])
    t_carro2 = Thread(target=carro, args=[2, 2])

    t_carro1.start()
    t_carro2.start()
