from lxml import etree
doc = etree.parse('users.xml')
listaaccesos=[]

usuarios=doc.findall('user')
for usuario in usuarios:
	buscaccesos=usuario.find('lastaccess')
	if buscaccesos.text not in listaaccesos:
		listaaccesos.append(buscaccesos.text)
listaaccesos.sort()
for acceso in listaaccesos:
	for usuario in usuarios:
		if acceso==usuario.find('lastaccess').text:
			print(usuario.find('firstname').text, usuario.find('lastname').text)