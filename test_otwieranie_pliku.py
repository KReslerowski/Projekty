namesandsurnames = []

with open("strony_do_sprawdzenia.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesandsurnames.append(tuple(line.replace("\n","").split(" ")))
        
for i in range(len(namesandsurnames)):        
    print(namesandsurnames[i])