lista = ['laranja', 'cerveja', 'miojo', 'carvão', 'picanha']

compra = input('''Produtos em estoque: laranja, cerveja, miojo, carvão, picanha
O que você vai querer comprar hoje? ''')
compra = compra.lower()

if compra in lista:
    print('Produto adicionado ao carrinho.')
else: 
    print('Não temos esse produto em estoque :( Escolha um produto válido e tente novamente.')