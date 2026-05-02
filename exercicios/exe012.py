# somar 4 alturas recebidas

total = 0

for i in range(1,5):
    altura = float(input(f'Altura da {i}ª pessoa (ex: 1.67): '))
    total += altura
    
print('Soma das alturas: ', total)