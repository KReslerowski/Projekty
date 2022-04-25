import requests
import json
import pprint
import webbrowser
from datetime import *

"""

API - Application Programming Interface

Inter - pomiędzy
face - twarz

bankomat

minimum 15 pkt
posegregowane malejąco
z ostatniego tygodnia
kategoria python

"""

czas = datetime.today() - timedelta(days = 14)


parametry = {
        "site" : "stackoverflow",
        "sort" : "votes",
        "order" : "desc",
        "fromdate" : int(czas.timestamp()),
        "tagged" : "python",
        "min" : 15
}

r = requests.get("https://api.stackexchange.com/2.2/questions/", parametry)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for questions in questions["items"]:
        pprint.pprint(questions["link"])
        webbrowser.open(questions["link"])
