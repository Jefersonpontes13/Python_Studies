"""coding: utf-8"""

import random
import string

TAMANHO = 16

CHARS = string.ascii_letters + string.digits + '!@#$%&*()-=+_'

rnd = random.SystemRandom()


def gerar_senha():
    return ''.join(rnd.choice(CHARS) for i in range(TAMANHO))


if __name__ == '__main__':
    gerar_senha()
