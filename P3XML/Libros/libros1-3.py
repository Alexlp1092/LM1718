from lxml import etree
doc = etree.parse('books.xml')
raiz=doc.getroot()

libro=etree.Element("book")
libro.append(etree.Element("title"))
libro.append(etree.Element("author"))
libro.append(etree.Element("year"))
libro.append(etree.Element("price"))
libro[0].text="Aprende Python con Joaquin"
libro[1].text="Joaquin Delhom Viana"
libro[2].text="2018"
libro[3].text="92.97"
raiz.append(libro)


doc.write('books2.xml')