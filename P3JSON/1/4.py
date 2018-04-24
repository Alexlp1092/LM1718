import json
from pprint import pprint
with open('books.json') as data_file:    
    data = json.load(data_file)

for libro in data['bookstore']['book']:
	print("Titulo:",libro["title"]["__text"])
	if type(libro['author'])!=list:
		print("Autor:",libro['author'])
		print()
	else:
		for autor in libro["author"]:
			print("Autor:",autor)
		print()