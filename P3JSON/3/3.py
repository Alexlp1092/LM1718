import json, time
from pprint import pprint
with open('ej3.json') as data_file:    
    data = json.load(data_file)

for provincia in data["lista"]["provincia"]:
	print(provincia["nombre"]["__cdata"])
	print("-------")
	time.sleep(2.0)
	contador=0
	if type(provincia["localidades"]["localidad"])==list:
		for municipio in provincia["localidades"]["localidad"]:
			contador=contador+1
	else:
		contador=contador+1
	print(contador,"municipios")
	print()