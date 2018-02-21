from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
raiz=doc.getroot()
provincias=doc.findall("provincia")

lista=["02", "25", "07", "85"]

for provincia in provincias:
	nombre=provincia.find('nombre')
	if provincia.attrib["id"] in lista:
		print("Provincia",nombre.text)
		localidades=provincia.findall('localidades/localidad')
		for localidad in localidades:
			print("Localidad",localidad.text)