import json
from pprint import pprint
with open('ej2.json') as data_file:    
    data = json.load(data_file)


for pruebas in data:
	if pruebas["Horas"]>2:
		print(pruebas["Titulo"])