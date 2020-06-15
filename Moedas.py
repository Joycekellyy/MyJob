precos = []


def moeda(txt):
	preço = input(txt)
	if ',' in preço:
		preço = preço.replace(',', '.')
	precos.append(preço)
	return preço

		
def fmoeda(valor):
	if '.' in valor: 
		return ('R$ {}'.format(valor))
	else:
		return ('R$ {},00'.format(valor))
	

preco = ''	
while preco != '0':	
	preco = moeda('preco: ')
	print(fmoeda(preco))
print(precos)
total = 0
for c, item in enumerate(precos):
	if item == '0':
		a = ''
	else:
		if '.' in item:
			item = float(item)
			total += item
		else:
			item = int(item)
			total += item
total = str(total)
print(fmoeda(total))
