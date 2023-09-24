import json

with open("bd.json", "r", encoding="utf-8") as f:
    data = json.load(f)

numbers = len(data)

summa = 0
for man in data:
    summa += man["оцінка"]

print(summa/numbers)