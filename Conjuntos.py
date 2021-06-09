# type[set] Conjunto: Sequencia de elementos unicos
conjunto_Inteiros = {1, 2, 3, 4, 5, 6, 7}
conjunto_Inteiros_2 = {1, 2, 3, 8, 9}

# Adicionar elemento ao conjunto
conjunto_Inteiros.add(8)

# Remover elemento do conjunto
conjunto_Inteiros.discard(8)
conjunto_Inteiros.add(8)
conjunto_Inteiros.remove(8)

# Unir conjuntos - União Aritmética
conjunto_Inteiros_Uniao = conjunto_Inteiros.union(conjunto_Inteiros_2)

# Intersecção de conjuntos - Intersecção Aritmética
conjunto_Inteiros_Interseccao = conjunto_Inteiros.intersection(conjunto_Inteiros_2)

# Diferença de conjuntos - Diferença Aritmética
conjunto_Inteiros_Diferenca = conjunto_Inteiros.difference(conjunto_Inteiros_2)

# Diferença Simétrica de conjuntos - Diferença Simétrica Aritmética
conjunto_Inteiros_Diferenca_Simetrica = conjunto_Inteiros.symmetric_difference(conjunto_Inteiros_2)

# Conjunto está contido em outro
conjunto_Esta_Contido = conjunto_Inteiros.issubset(conjunto_Inteiros_2)

# Conjunto Contém outro
conjunto_Contem = conjunto_Inteiros.issuperset(conjunto_Inteiros_2)

# Converter lista em Conjunto - Remove redundância de elementos
lista_Animais = ['Galo', 'Pato', 'Gato', 'Cachorro', 'gato']
conjunto_Animais = set(lista_Animais)

# Converter conjunto em lista
lista_Animais_Unicos = list(conjunto_Animais)
