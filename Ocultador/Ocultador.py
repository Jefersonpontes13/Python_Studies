"""coding: utf-8"""

import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('tst.txt', atributo_ocultar)

if retorno:
    print('deu certo')
else:
    print('deu ruim')
