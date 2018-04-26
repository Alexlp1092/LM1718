import json
from pprint import pprint
with open('swjson.json') as data_file:    
    data = json.load(data_file)


pasmin=input("Introduzca un minimo de pasajeros: ")
pasmax=input("Introduzca un máximo de pasajeros: ")
print()
print("Las naves con dicha capacidad de pasejeros son: ")
print("------------------------------------------------")
for nave in data["results"]:
	if nave["passengers"]>pasmin and nave["passengers"]<pasmax:
		print(nave["name"])