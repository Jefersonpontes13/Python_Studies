"""coding: utf-8"""

import phonenumbers
from phonenumbers import geocoder

phone = input('Telefone : +5588994933633 : ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
