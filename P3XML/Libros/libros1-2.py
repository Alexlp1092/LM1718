from lxml import etree
doc = etree.parse('books.xml')

libros=doc.findall('book')

libros[0].attrib["category"]='ITALIANI'


print("La nueva categoria =",libros[0].attrib["category"])

doc.write('books2.xml')