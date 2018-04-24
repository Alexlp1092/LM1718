import json
from pprint import pprint
with open('ej2.json') as data_file:    
    data = json.load(data_file)

codigo=input("Introduzca un id: ")

for pruebas in data:
	if pruebas["ID"]==codigo:
		print(pruebas["Titulo"])
		for profesores in pruebas["Profesorado"]:
			print(profesores["NombreCompleto"])