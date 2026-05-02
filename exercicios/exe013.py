# Saldo em conta com valores digitados 

soma = 0

print('SALDO EM CONTA')

while True:
    valor = input('Digite o valor que você vai adicionar (ex: 50.50): ')
    if valor == '':
        break
    else: 
        soma += float(valor)
    

print('SALDO TOTAL: R$', soma)