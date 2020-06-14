import os
days = ['SEGUNDA', 'QUARTA', 'QUINTA']
daysentrega = ['TERÇA', 'QUINTA', 'SEXTA']
precos = []

def moeda(txt):
	preço = input(txt)
	if ',' in preço:
		preço = preço.replace(',', '.')
	precos.append(preço)
	return preço

		
def fmoeda(valor):
	if '.' in valor: 
		valor = valor.replace('.',',')
		return ('R$ {}'.format(valor))
	else:
		return ('R$ {},00'.format(valor))

def ftot(valor):
	if '.' in valor:
		valor = ('R$ {}'.format(valor))
		valor = valor.replace('.',',')
		return valor
	else:
		return ('R$ {},00'.format(valor))

while True:
#DADOS DO CLIENTE

	name = str(input('Nome do cliente: ')). title()
	number = input('Número: ')
	
#ENTREGA

	while True:
		entrega = str(input('Entrega? [S/N]')).upper()
		if entrega == 'N' or entrega == 'S':
			break
	print(' ')
	if entrega == 'S':
		endereço = input('Endereço: ')
		print (' ')
#DIA DA FABRICAÇÃO
	print('-=' * 10)
	for c, items in enumerate(days):
		print('{} - {}'.format(c+1, items))
	print('-=' * 10)
	fabrication = int(input('Dia da fabricação: ')) 
	
	while fabrication > len(days):
		fabrication = int(input('Dia da fabricação: '))
		if fabrication <= len(days):
			break
	datef = str(input('Data: '))
	
	print(' ')

#DIA DA ENTREGA

	print('-=' * 10)
	for c, items in enumerate(daysentrega):
		print('{} - {}'.format(c+1, items))
	print('-=' * 10)
	diaentrega = int(input('Dia do recebimento: '))

	while diaentrega > len(daysentrega):
		diaentrega = int(input('Dia da recebimento: '))
		if diaentrega <= len(daysentrega):
			break
	dateentrega = str(input('Data: '))
	break
	
print(' ')

#FORMATAÇÃO

print(' ')
	
qproducts = int(input('Quantos produtos? '))

print(' ')
	
if entrega == 'S':
	with open('Pedidos.txt', 'w+') as file:
		file.write(f'{name} {days[fabrication-1]} ({datef})\n• ENTREGA:  *{daysentrega[diaentrega-1]} {dateentrega}*\n• ENDEREÇO: {endereço}\n• NÚMERO: {number}')
		print('-=' * 10)
		for c in range(0, qproducts):
			nameProduct = str(input('Nome do produto: ')).upper()
			try:
				medidaA = int(input('A - Altura: '))
				medidaL = int(input('L - Largura: '))
				medidaP = int(input('P - Profundidade: '))
				preço = moeda('Preço: ')
				print('-=' * 10)
				print(' ')
			except: 
				print('Digite os dados corretamente!')
			else:
				taxa = moeda('Taxa: ')
				taxa = fmoeda(taxa)
				file.write(f'\n \n~ {nameProduct} ~ \n• MEDIDA: {medidaL}L x {medidaA}A x {medidaP}P \n• VALOR: {fmoeda(preço)}')
				file.write(f'\n \n• TAXA: {taxa}')
		file.seek(0, 0)

else:
	with open('Pedidos.txt', 'w+') as file:
		file.write(f'{name} {days[fabrication-1]} ({datef})\n• RETIRADA:  *{daysentrega[diaentrega-1]} {dateentrega}*\n• NÚMERO: {number}')
		print('-=' * 10)
		for c in range(0, qproducts):
			nameProduct = str(input('Nome do produto: ')).upper()
			try:
				medidaA = int(input('A - Altura: '))
				medidaL = int(input('L - Largura: '))
				medidaP = int(input('P - Profundidade: '))
				preço = moeda('Preço: ')
				print('-=' * 10)
				print(' ')
			except: 
				print('Digite os dados corretamente!')
			else:
				file.write(f'\n \n~ {nameProduct} ~ \n• MEDIDA: {medidaL}L x {medidaA}A x {medidaP}P \n• VALOR: {fmoeda(preço)}')
#CALCULANDO O TOTAL
total = 0		
for c, item in enumerate(precos):
	if item != '0':
		if '.' in item:
			item = float(item)
			total += item
		else:
			item = int(item)
			total += item
total = str(total)
total = ftot(total)

if entrega == 'N':
	with open('Pedidos.txt', 'a+') as file:
		file.write(f'\n \n• VALOR TOTAL: {total}')
		file.seek(0, 0)
		print(file.read())
else:	
	with open('Pedidos.txt', 'a+') as file:
		file.write(f'\n• VALOR TOTAL: {total}')
		file.seek(0, 0)
		print(file.read())
os.startfile(r'C:\Users\Convidado\Documents\WhitArt\Pedidos.txt')