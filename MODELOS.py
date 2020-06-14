def moeda(txt):
	preço = input(txt)
	if ',' in preço:
		preço = preço.replace(',', '.')
	return preço

		
def fmoeda(valor):
	valor = valor.replace('.', ',')
	return ('R$ {}'.format(valor))
	
	
cores = ['BRANCO','PRETO','AMADEIRADO']
pause = ''
while True:
	texto = str(input('Nome do produto: ')).upper()
	preço = moeda('Preço: ')
	print('-='*10)
	for c, item in enumerate(cores):
		print(f'{c+1} - {item}')
	print('-='*10)
	while pause != True:
		try:
			cor = int(input('COR: '))
			cor-=1
			cor = cores[cor]
			medidaA = int(input('Altura: '))
			medidaL = int(input('Largura: '))
			medidaP = int(input('Profundidade: '))
		except: 
			print('Digite os dados corretamente!')
		else:
			preço = fmoeda(preço)
			with open('Text.txt', 'w+') as file:
				file.write(f'🌻 {texto} 🌻 {preço}\n \n• COR: {cor}\n• MEDIDA: {medidaL}L x {medidaA}A x {medidaP}P\n \nO MÓVEL PERFEITO PARA VOCÊ DECORAR A CASA DO SEU JEITINHO! ✨\n \n• ENTREGA SOMENTE EM IPATINGA.\n• TAXA DE ACORDO COM O BAIRRO, OU RETIRADA NO BAIRRO VENEZA 2.\n \n• ACEITAMOS CARTÃO DE CRÉDITO, COM ACRÉSCIMO.\n \n• PARA MAIS INFORMAÇÕES OU PERGUNTAS, MANDE-NOS UMA MENSAGEM! ✨\n \n• EFEITO COVID • \n -Devido ao covid-19 nós não estamos fazendo entregas de itens pequenos, apenas itens grandes que os cliente não conseguem estarem carregando em seus veículos. Desde já agradeço pela compreensão e colaboração de todos! ✨')
				file.seek(0, 0)
				print(file.read())
				break
	break