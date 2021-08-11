"""coding: utf-8"""

from datetime import date, time, datetime, timedelta


def data_atual_numerica():
    data_atual = date.today()
    return data_atual.strftime('%d/%m/%Y')


def data_atual_texto():
    data_atual = date.today()
    return data_atual.strftime('%A %B %Y')


def time_especifico(h, m, s):
    horario = time(hour=h, minute=m, second=s)
    return horario.strftime('%H:%M:%S')


def obter_date_time():
    data_time_atual = datetime.now()
    return data_time_atual.strftime('%d/%m/%Y %H:%M:%S')


def obter_date_time_all_simple():
    data_time_atual = datetime.now()
    return data_time_atual.strftime('%c')


def obter_dia_atual():
    return datetime.now().day


def obter_ano_atual():
    return datetime.now().year


def obter_mes_atual():
    return datetime.now().month


def obter_dia_semana_atual():
    tupla_dias_semana = (
        'Segunda',
        'Terça',
        'Quarta',
        'Quinta',
        'Sexta',
        'Sábado',
        'Domingo',
    )
    return tupla_dias_semana[datetime.now().weekday()]


if __name__ == '__main__':
    print(data_atual_numerica())
    print(data_atual_texto())
    print(time_especifico(15, 23, 52))
    print(obter_date_time())
    print(obter_date_time_all_simple())
    print(obter_dia_semana_atual())

    data_string = '01/01/2019'
    data_string_datetime = datetime.strptime(data_string, '%d/%m/%Y')

    data_resultado = data_string_datetime - timedelta(days=30, hours=3, minutes=45)

    sete_de_setembro = datetime.strptime('07/09/2001', '%d/%m/%Y') - datetime.now()

    print(data_resultado)
