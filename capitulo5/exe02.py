# SOMA DE ALTURAS

cont = 1
soma = 0
while cont <= 4:
    alt = float(input('Digite uma altura (ex: 1.75): '))
    soma += alt
    cont += 1

print('A soma total das alturas deu:', soma)

# %% SOMA DE ALTURAS COM FOR

soma = 0

for i in range (1, 5):
    alt = float(input('Digite uma altura (ex: 1.75): '))
    soma += alt

print('A soma total das alturas é:', soma)