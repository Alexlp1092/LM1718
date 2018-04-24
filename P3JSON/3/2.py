import json
from pprint import pprint
with open('ej3.json') as data_file:    
    data = json.load(data_file)

for provincia in data["lista"]["provincia"]:
	if type(provincia["localidades"]["localidad"])==list:
		for municipio in provincia["localidades"]["localidad"]:
			print(municipio["__cdata"])
	else:
		print(provincia["localidades"]["localidad"]["__cdata"])