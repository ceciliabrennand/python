# SOMA DE ALTURAS

cont = 1
soma = 0
while cont <= 4:
    alt = float(input('Digite uma altura (ex: 1.75): '))
    soma += alt
    cont += 1

print('A soma total das alturas deu:', soma)