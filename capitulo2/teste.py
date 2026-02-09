# testando ph

ph = int(input('Escolha um número de 0 a 14: '))

if ph > 7:
    print('pH básico')
elif ph < 7:
    print('pH ácido')
else:
    print('pH neutro')