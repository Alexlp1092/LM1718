from lxml import etree
doc = etree.parse('users.xml')

usuarios=doc.findall('user')

for usuario in usuarios:
	nombre=usuario.find('firstname')
	apellido=usuario.find('lastname')
	print(nombre.text, apellido.text)