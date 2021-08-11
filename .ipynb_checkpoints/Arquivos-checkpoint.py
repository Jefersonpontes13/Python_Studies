import shutil


def escrever_arquivo(arquivo_texto, texto_escrita):
    arquivo_texto = open(arquivo_texto, 'w')
    arquivo_texto.write('{}\n'.format(texto_escrita))
    arquivo_texto.close()


def atualizar_arquivo(arquivo_texto, texto_escrita):
    arquivo_texto = open(arquivo_texto, 'a')
    arquivo_texto.write('{}\n'.format(texto_escrita))
    arquivo_texto.close()


def ler_arquivo(arquivo_texto):
    arquivo_texto = open(arquivo_texto, 'r')
    texto = arquivo_texto.read()
    arquivo_texto.close()
    return texto


def media(notas):
    # Python - List Comprehension
    return sum([float(nota) for nota in notas]) / len(notas)


def media_notas(arquivo_texto_notas, arquivo_texto_medias):
    alunos_notas = ler_arquivo(arquivo_texto_notas)

    alunos_notas = [aluno_notas.split(',') for aluno_notas in alunos_notas.split()[1:]]

    # Python - List Comprehension and lambda
    # media = lambda notas: sum([float(nota) for nota in notas]) / len(notas)

    for aluno in alunos_notas:
        atualizar_arquivo(arquivo_texto_medias, '{},{}'.format(aluno[0], media(aluno[1:])))


def copiar_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/Jeffe/PycharmProjects/Estudos_Python/Arquivos_txt/')


def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/Jeffe/PycharmProjects/Estudos_Python/Arquivos_txt/')


if __name__ == '__main__':

    arquivo_notas_txt = 'notas.txt'
    arquivo_medias_txt = 'medias.txt'
    escrever_arquivo(arquivo_notas_txt, 'Aluno,AP1,AP2,AP3')
    atualizar_arquivo(arquivo_notas_txt, 'Jorge,7,8,9')
    atualizar_arquivo(arquivo_notas_txt, 'Jeferson,7,7,7')
    atualizar_arquivo(arquivo_notas_txt, 'Lucas,6,7,9')
    atualizar_arquivo(arquivo_notas_txt, 'Samuel,9,6,9')

    media_notas(arquivo_notas_txt, arquivo_medias_txt)

    # copiar_arquivo(arquivo_notas_txt)
    mover_arquivo(arquivo_notas_txt)
    mover_arquivo(arquivo_medias_txt)
