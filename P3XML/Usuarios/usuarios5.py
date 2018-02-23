from lxml import etree
doc = etree.parse('users.xml')
listaciudades=[]

usuarios=doc.findall('user')
for usuario in usuarios:
	buscaciudad=usuario.find('city')
	if buscaciudad.text not in listaciudades:
		listaciudades.append(buscaciudad.text)
for ciudad in listaciudades:
	print (ciudad)
	print ("-----")
	for usuario in usuarios:
		if ciudad==usuario.find('city').text:
			print(usuario.find('firstname').text)
	print()
			