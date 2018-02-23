from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
#print (etree.tostring(doc))
raiz=doc.getroot()

print (len(raiz))

#for i in range (len(raiz)):
#	provincias=raiz[i]
#	print(provincias[0].text)


provincias=doc.findall("provincia")
for provincia in provincias:
	print (provincia[0].text)


#localidades=doc.findall("localidades")
#for localidad in localidades:
#	print(localidades.text)