import requests
import json
import webbrowser
import credentials

from pprint import pprint

r = requests.get('https://api.thecatapi.com/vl/favorites/', headers = 'c81be0eb-028a-495c-b33b-b76ebc41756a')

try:
    content = r.json()
except:
    print("Niepoprawny format", r.text)
else:
    print(content)


print("hej, zaloguj się - podaj login i haslo ")