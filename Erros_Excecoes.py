"""coding: utf-8"""


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


def divisao(dividendo, divisor):
    arquivo_txt = None
    try:
        arquivo_txt = open('Arquivos_txt/notas.txt', 'r')
        texto = arquivo_txt.read()
        print(texto)
        resultado = [dividendo[indice] / divisor[indice] for indice in range(len(dividendo))]
    except BaseException as ex:
        print('Erro encontrado:\n{}'.format(ex))
    except ZeroDivisionError:
        print("Não é possível realizar divisão por zero - 0")
    except IndexError:
        print("Não é possível acessar um índice inválido")
    else:
        print('Executa quando não ocorre axeção')
        return resultado
    finally:
        print('Sempre executa')
        arquivo_txt.close()


def execao_personalizada():
    while True:
        try:
            x = int(input(' Nota [0, 10] : '))
            print(x)
            if 10 < x:
                raise InputError("Nota não pode ser maior que 10")

            elif x < 0:
                raise InputError("Nota não pode ser menor que 0")
            break
        except ValueError:
            print("A nota deve ser um número.")
        except InputError as excecao_message:
            print(excecao_message)


if __name__ == '__main__':
    lista_dividendos = [12, 4, 7, 9, 28]
    lista_divisores = [3, 9, 1, 3, 1]
    divisao(lista_dividendos, lista_divisores)
    execao_personalizada()
