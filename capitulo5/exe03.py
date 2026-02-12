saldo_tot = 0

while True:
    valor = input('Digite o saldo em conta: ')
    if valor == "":
        break
    saldo_tot += float(valor)

print('A soma total do saldo em conta foi de: R$', saldo_tot)