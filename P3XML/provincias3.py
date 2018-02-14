from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
#print (etree.tostring(doc))
raiz=doc.getroot()

provincias=doc.findall("provincia")
for provincia in provincias:
	print (provincia[0].text)

localidades=doc.findall("provincia/localidades/localidad")
print (len(localidades))

