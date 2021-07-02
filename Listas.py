# type[list] Lista: Sequencia de valores - Passíveis de mudança.
lista_Interiros = [1, 2, 3, 4, 5, 6, 7]

# Seleciana valores da lista por indexação
print(lista_Interiros[:3])

# Seleciona elementos por meio de um step
print(lista_Interiros[::2]) # Nesse caso retorna os impares
# Somar valores da lista
sum(lista_Interiros)

# Maior valor da lsita
max(lista_Interiros)

# Menor valor da lsita
min(lista_Interiros)

# Se elemento está contido na lista
esta_Contido = 1 in lista_Interiros

# Percorrer elementos da lista]
for elemento_Inteiro in lista_Interiros:
    print(elemento_Inteiro)

# Operar todos os valores da lista
lista_Interiros *= 1

# Incluir elemento em uma lista
lista_Interiros.append(8)

# Retirar ultimo elemento da lista
lista_Interiros.pop()

# Retirar elemento de uma posição específica da lista
lista_Interiros.pop(0)

# Remover um elemento específico de uma lista
lista_Interiros.remove(2)

# Ordenar uma lista - Ascendente
lista_Interiros.sort()

# Inverte a ordem dos elementos
lista_Interiros.reverse()

# Python - List Comprehension
lista_Interiros_Ao_Quadrado = [elemento_Inteiro ** 2 for elemento_Inteiro in lista_Interiros]


