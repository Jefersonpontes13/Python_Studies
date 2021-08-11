"""coding: utf-8"""

import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou !!!")
        print("Erro {}".format(e))
        sys.exit()
    print("socket criado com sucesso")

    host_alvo = input("HOST: ")
    port_alvo = input("PORT: ")

    try:
        s.connect((host_alvo, int(port_alvo)))
        print("cliente TCP conectado - HOST: {} PORT: {}".format(host_alvo, port_alvo))
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar - HOST: {} PORT: {}".format(host_alvo, port_alvo))
        print("Erro {}".format(e))
        sys.exit()


if __name__ == '__main__':
    main()
