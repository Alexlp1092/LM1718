from lxml import etree


licencias=etree.Element("licencias")
doc=etree.ElementTree(licencias)
licencia=etree.Element("licencia")
nombre=etree.Element("nombre")
imagen=etree.Element("imagen")
licencia.append(nombre)
licencia.append(imagen)
licencia[0].text="Creative Commons By - Share Alike"
licencia[1].text="cc_bysa_88x31.png"
licencias.append(licencia)

doc.write('licencias.xml', xml_declaration=True, encoding='UTF-8', pretty_print=True)