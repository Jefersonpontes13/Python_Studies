"""coding: utf-8"""


import hashlib


def main():
    arquivo1 = 'a.txt'
    arquivo2 = 'b.txt'

    hash1 = hashlib.new('ripemd160')
    hash1.update(open(arquivo1, 'rb').read())

    hash2 = hashlib.new('ripemd160')
    hash2.update(open(arquivo2, 'rb').read())

    print(f'Hash 1: {hash1.hexdigest()}')
    print(f'Hash 2: {hash2.hexdigest()}')

    if hash1.digest() != hash2.digest():
        print(f'Aruivos {arquivo1} e {arquivo2}, são diferentes')
    else:
        print(f'Aruivos {arquivo1} e {arquivo2}, são iguais')


if __name__ == '__main__':
    main()
