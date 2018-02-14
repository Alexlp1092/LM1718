from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
#print (etree.tostring(doc))
raiz=doc.getroot()



localidades=doc.findall("provincia/localidades/localidad")
print (len(localidades))

provincias=doc.findall("provincia")
for provincia in provincias:
	print (provincia[0].text)