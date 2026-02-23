# Solicite o nome de uma fruta e exiba o preço correspondente

frutas = {
'Maça':'R$1.50',
'Banana':'R$2.75',
'Uva':'R$1.90',
'Pera':'R$1.25',
'Laranja':'R$0.65',
'Limao':'R$1.25',
'Goiaba':'R$2.15',
'Abacaxi':'R$3.20',
'Jaca':'R$5.80'
}

fruta = input('Escolha uma fruta: ')

if fruta in frutas:
    print('Valor total:', frutas[fruta])
else:
    print('Fruta inválida. Coloque outra.')