from lxml import etree
doc = etree.parse('books.xml')

libros=doc.findall('book')

libros[1].find('year').text='2018'


print("Año =",libros[1].find('year').text)

doc.write('books2.xml')