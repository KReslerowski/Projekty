import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def zliczanie_ukonczonych_zadan(tasks):
    ukonczoneZadaniaUzytkownika = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                ukonczoneZadaniaUzytkownika[entry["userId"]] += 1
            except KeyError:
                ukonczoneZadaniaUzytkownika[entry["userId"]] = 1
                
    return ukonczoneZadaniaUzytkownika
            
def users_with_top_completed_tasks(completedTasksFrequencyByUser):
    userIdWithMaxCompletedAmountOfTasks = []
    maxAmountOfCompletedTask = max(completedTasksFrequencyByUser.values())            
    for userId, numberOfCompletedTask in completedTasksFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            userIdWithMaxCompletedAmountOfTasks.append(userId)
    
    return userIdWithMaxCompletedAmountOfTasks
    
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Error decoding")
else:
    iloscSkonczonychZadanPrzezUsera = zliczanie_ukonczonych_zadan(tasks)
    uzytkownicy_z_najwieksza_iloscia_pkt = users_with_top_completed_tasks(iloscSkonczonychZadanPrzezUsera)
    
print(uzytkownicy_z_najwieksza_iloscia_pkt)