"""coding: utf-8"""

import requests


def dados_viacep(cep):
    return requests.get('https://viacep.com.br/ws/{}/json/'.format(cep)).json()


def dados_pokemon(pokemon):
    return requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon)).json()


def retorna_response(url):
    return requests.get(url).text


if __name__ == '__main__':
    print(dados_viacep('62042210'))
    print(dados_pokemon('pikachu'))
    print(retorna_response('http://www.nuclic.ufc.br'))
