"""coding: utf-8"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket criado com sucesso")

HOST = 'localhost'
PORT = 5433
mensagem = 'Olá servidor'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (HOST, 5432))

    dados, servdor = s.recvfrom(4096)
    dados = dados.decode()

    print("Cliente: " + dados)
finally:
    print("cliente : fecha a conexão")
    s.close()
