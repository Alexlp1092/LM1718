import json
from pprint import pprint
with open('ej3.json') as data_file:    
    data = json.load(data_file)

for provincias in data["lista"]["provincia"]:
	print(provincias["nombre"]["__cdata"])