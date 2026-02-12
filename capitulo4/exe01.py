print('----- VENDEDOR DE ÁGUA -----')
print('Você deseja água com ou sem gás?')
print('1) Sem gás')
print('2) Com gás')
agua = int(input('Escreva 1 ou 2: '))

if agua == 1:
    print('O total é: R$1,50')
elif agua == 2:
    print('O total é: R$2,50')
else:
    print('Resposta inválida. Escolha 1 ou 2.')