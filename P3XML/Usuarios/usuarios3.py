from lxml import etree
doc = etree.parse('users.xml')

usuarios=doc.findall('user')

for usuario in usuarios:
	ip=usuario.find('lastip')
	octeto=ip.text.split('.')
	if octeto[0]!="172":
		print(usuario.find('email').text)