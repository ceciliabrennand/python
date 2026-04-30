print('''Bem-vindo ao Galego da Água.
    Escolha qual água você quer:
    1) Natural: R$1,50
    2) Com gás: R$2,50  ''')

opcao = int(input('Escolha a opção que deseja (ex: 1): '))
qtde = int(input('Quantas garrafas deseja? '))

if opcao == 1:
    total = 1.50 * qtde
    print('Valor total: R$', total)
elif opcao == 2:
    total = 2.50 * qtde
    print('Valor total: R$', total)
else:
    print('Opção inválida. Tente novamente.')

