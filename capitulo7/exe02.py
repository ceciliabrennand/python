# Solicite o nome de uma fruta e exiba o preço correspondente

maça = 1.50
banana = 2.75
uva = 1.90
pera = 1.25
laranja = 0.65
limao = 1.25
goiaba = 2.15
abacaxi = 3.20
jaca = 5.80

fruta = input('Qual fruta você deseja?')
if fruta == 'Maçã' or fruta == 'maçã':
    print('Valor total: R$', maça)
elif fruta == 'Banana' or fruta == 'banana':
    print('Valor total: R$', banana)
elif fruta == 'Uva' or fruta == 'uva':
    print('Valor total: R$', uva)    
elif fruta == 'Pêra' or fruta == 'pêra':
    print('Valor total: R$', pera)
elif fruta == 'Laranja' or fruta == 'laranja':
    print('Valor total: R$', laranja)
elif fruta == 'Limão' or fruta == 'limão':
    print('Valor total: R$', limao)
elif fruta == 'Goiaba' or fruta == 'goiaba':
    print('Valor total: R$', goiaba)
elif fruta == 'Abacaxi' or fruta == 'abacaxi':
    print('Valor total: R$', abacaxi)
elif fruta == 'Jaca' or fruta == 'jaca':
    print('Valor total: R$', jaca)
else: 
    print('Não temos essa fruta disponível. Escolha outra.')