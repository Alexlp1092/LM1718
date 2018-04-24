import json
from pprint import pprint
with open('ej2.json') as data_file:    
    data = json.load(data_file)

for pruebas in data:
	print(pruebas["Titulo"])
	print("--------")
	for profesores in pruebas["Profesorado"]:
		print(profesores["NombreCompleto"])
	print()