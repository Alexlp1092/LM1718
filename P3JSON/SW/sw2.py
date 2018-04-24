import json
from pprint import pprint
with open('swjson.json') as data_file:    
    data = json.load(data_file)

contador=0
print("Ahora listará las naves que aparezcan en el episodio que quieras")
episodio=input("Introduzca el número del episodio: ")


for nave in data["results"]:
	for pelicula in nave["films"]:
		if pelicula["id"]==episodio:
			nombre=pelicula["title"]
			contador=contador+1
			print(nave["name"])
print("El total de naves en",nombre,"son",contador)