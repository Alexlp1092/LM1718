from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
#print (etree.tostring(doc))
raiz=doc.getroot()

provincias=doc.findall("provincia")
buscaprovincia=str(input("Introduzca una provincia: "))
for provincia in provincias:
	nombre=provincia.find('nombre')
	if nombre.text==buscaprovincia:
		for localidades in provincia.findall('localidades/localidad'):
			print (localidades.text)