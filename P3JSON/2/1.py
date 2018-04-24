import json
from pprint import pprint
with open('ej2.json') as data_file:    
    data = json.load(data_file)

listapruebas=[]
for pruebas in data:
	listapruebas.append(pruebas["Titulo"])

print("El numero total de pruebas es: ",len(listapruebas))