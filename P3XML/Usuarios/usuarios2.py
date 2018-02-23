from lxml import etree
doc = etree.parse('users.xml')

usuarios=doc.findall('user')

for usuario in usuarios:
	if usuario.find('picture').text=="1":
		print(usuario.find('username').text)