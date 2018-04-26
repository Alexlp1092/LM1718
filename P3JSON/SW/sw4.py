import json
from pprint import pprint
with open('swjson.json') as data_file:    
    data = json.load(data_file)


nombrenave=input("Introduzca la palabra por la que quiere buscar la nave ")

for nave in data["results"]:
	if nave["name"].startswith(nombrenave) or nave["name"].endswith(nombrenave):
		print(nave["name"])