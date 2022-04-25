"""
pip - pip installs packages - instalator pakunktów

PyPi - Python Package index - indeks (spis) pakunktów do Pythona


"""

import requests

response = requests.get("http://videokurs.pl")

print(response.status_code)