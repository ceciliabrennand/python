idade = int(input('Qual é a sua idade?'))

if idade >= 18 and idade < 70:
    print('Você está liberado para beber!')
elif idade >= 70:
    print('Sua idade é avançada. Cuidado com a bebida.')
else:
    print('Você não é maior de idade. Não pode beber.')