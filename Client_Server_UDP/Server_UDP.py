"""coding: utf-8"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("socket criado")

HOST = 'localhost'
PORT = 5432

s.bind((HOST, PORT))

mensagem = 'Olá cliente'

while 1:
    dados, endereco = s.recvfrom(4096)

    if dados:
        print('servidor enviando mensagem')
        s.sendto(dados + mensagem.encode(), endereco)
