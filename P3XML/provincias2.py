from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
#print (etree.tostring(doc))
raiz=doc.getroot()

localidades=doc.findall("provincia/localidades/localidad")
for localidad in localidades:
	print(localidad.text)