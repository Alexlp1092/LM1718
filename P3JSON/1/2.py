import json
from pprint import pprint
with open('books.json') as data_file:    
    data = json.load(data_file)

preciomin=float(input("Introduzca el precio minimo: "))
preciomax=float(input("Introduzca el precio maximo: "))

for libro in data['bookstore']['book']:
	if float(libro["price"])>preciomin and float(libro["price"])>preciomax:
		print (libro["title"]["__text"])