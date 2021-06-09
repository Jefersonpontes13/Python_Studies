
class Calculadora:
    def __init__(self, operando_1, operando_2):
        self.operando_1 = operando_1
        self.operando_2 = operando_2

    def adicao_self(self):
        return self.operando_1 + self.operando_2

    def subtracao_self(self):
        return self.operando_1 - self.operando_2

    def multiplicacao_self(self):
        return self.operando_1 * self.operando_2

    def divisao_self(self):
        return self.operando_1 / self.operando_2

    def soma(self, operando_1, operando_2):
        return operando_1 + operando_2


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 1

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal += 1

    def diminui_canal(self):
        self.canal -= 1
