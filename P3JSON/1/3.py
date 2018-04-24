import json
from pprint import pprint
with open('books.json') as data_file:    
    data = json.load(data_file)

cadena=input("Introduzca la cadena por la que quiere buscar el titulo: ")

for libro in data['bookstore']['book']:
	if libro["title"]["__text"].startswith(cadena):
		print("Titulo:",libro["title"]["__text"],'\n'
		 	"Año:",libro["year"])