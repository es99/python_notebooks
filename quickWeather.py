"""Consumindo API da Open Weather Map com módulos json do Python"""

import json, requests, sys
import pprint

if len(sys.argv) < 2:
    print('Uso: quickWheater <localizacao>')
    sys.exit()

location = ' '.join(sys.argv[1:])

key_pass = 'f1ad681a228a6de282df71c707d65498'
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key_pass}&lang=pt_br"

response = requests.get(url)

response.raise_for_status()
weatherData = json.loads(response.text)

humidade = weatherData['main']['humidity']
temperatura = weatherData['main']['temp']
condicao = weatherData['weather'][0]['description']
cidade = weatherData['name']

print(f"Cidade: {cidade}")
print(f"temperatura: {celsius}\nhumidade: {humidade}\ncondicao:{condicao}")