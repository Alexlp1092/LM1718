import json
from pprint import pprint
with open('swjson.json') as data_file:    
    data = json.load(data_file)

contador=0
print("Ahora listará las naves que aparezcan en el episodio que quieras")
episodio=input("Introduzca el número del episodio: ")
listapelis=[]

for pelicula in data ["results"]:
	for titulo in pelicula["films"]:
		if titulo["id"] not in listapelis:
			listapelis.append(titulo["id"])

if episodio not in listapelis:
	print("Pelicula inexistente")
else:
	for nave in data["results"]:
		for pelicula in nave["films"]:
			if pelicula["id"]==episodio:
				nombre=pelicula["title"]
				contador=contador+1
				print(nave["name"])
	print("El total de naves en",nombre,"son",contador)