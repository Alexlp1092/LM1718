import json
from pprint import pprint
with open('swjson.json') as data_file:    
    data = json.load(data_file)

for nave in data["results"]:
	print(nave["name"])