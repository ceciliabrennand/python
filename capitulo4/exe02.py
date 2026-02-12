print('----- VENDEDOR DE ÁGUA -----')
print('Você deseja água com ou sem gás?')
print('1) Sem gás')
print('2) Com gás')
agua = int(input('Escreva 1 ou 2: '))
num = int(input('Quantas águas você quer? '))

if agua == 1:
    print('O total é: R$', 1.50 * num)
elif agua == 2:
    print('O total é: R$', 2.50 * num)
else:
    print('Resposta inválida. Escolha 1 ou 2.')