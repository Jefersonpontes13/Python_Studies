"""coding: utf-8"""

import hashlib

stringEntrada = input("Digite o texto: ")

menu = int(input('''
Menu - Tpo de Hash

1 - MD5
2 - SHA1
3 - SHA256
4 - SHA521

Número do  Hash a ser gerado :  
'''))

if menu == 1:
    resultado = hashlib.md5(stringEntrada.encode('utf-8'))
    print('Hash MD5: ', resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(stringEntrada.encode('utf-8'))
    print('Hash SH1: ', resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(stringEntrada.encode('utf-8'))
    print('Hash SHA256: ', resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(stringEntrada.encode('utf-8'))
    print('Hash SHA512: ', resultado.hexdigest())

else:
    print('Deu ruim')
