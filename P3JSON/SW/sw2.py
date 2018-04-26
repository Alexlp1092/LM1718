import json
from pprint import pprint
with open('swjson.json') as data_file:    
    data = json.load(data_file)


listapelis=[]

for pelicula in data ["results"]:
	for titulo in pelicula["films"]:
		if titulo["id"] not in listapelis:
			listapelis.append(titulo["id"])


for nave in data["results"]:
	contador=0
	for pelicula in nave["films"]:
		contador=contador+1
	if contador==1:
		print(nave["name"], contador, "vez")
	else:
		print(nave["name"], contador, "veces")
	