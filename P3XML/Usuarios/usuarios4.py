from lxml import etree
doc = etree.parse('users.xml')

usuarios=doc.findall('user')
comienzo=input("Introduzca una cadena: ")
numeroletras=len(comienzo)

for usuario in usuarios:
	nombre=usuario.find('firstname')
	apellido=usuario.find('lastname')
	if nombre.text[:numeroletras]==comienzo:
		print(nombre.text, apellido.text)