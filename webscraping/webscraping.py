"""coding: utf-8"""

from bs4 import BeautifulSoup
import requests

site = requests.get("https://tabuademares.com/br/ceara/fortaleza").content

soup = BeautifulSoup(site, 'html.parser')

#print(soup.prettify())

#temperatura = soup.find("div", class_="grafico_estado_actual_texto_size grafico_estado_actual_texto1")

print(soup.title.string)
