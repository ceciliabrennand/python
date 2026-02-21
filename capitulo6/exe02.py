# Pedir ao usuário que escolha um número e mostrar quantas vezes aparece na lista

lista = [1,2,3,4,4,4,4,5,6,7,5,7,9,9,8,4,7,5,3,2,0,8,9,1]
cont = 0

num_esc = int(input('Escolha um número entre 0 e 9: '))
if num_esc > 9:
    print('Número inválido. Tente novamente.')
else:
    for i in (lista):
        if i == num_esc:
            cont += 1
    print(lista)
    print('O número', num_esc, 'apareceu', cont, 'vezes na lista.')
