import json, time
from pprint import pprint
with open('ej3.json') as data_file:    
    data = json.load(data_file)

nombremun=input("Introduzca un municipio: ")

for provincia in data["lista"]["provincia"]:
	nombreprov=provincia["nombre"]["__cdata"]
	if type(provincia["localidades"]["localidad"])==list:
		for municipio in provincia["localidades"]["localidad"]:
			if nombremun==municipio["__cdata"]:
				print(nombremun, "pertenece a la provincia de",nombreprov)
				break
	else:
		if nombremun==municipio["__cdata"]:
			print(nombremun, "pertenece a la provincia de",nombreprov)
			break