print('TABUADA')
num = int(input('Escolha um número: '))

cont = 1
print('Tabuada do', num)

while cont <= 10:
    print(num, 'x', cont, '=', num * cont)
    cont += 1