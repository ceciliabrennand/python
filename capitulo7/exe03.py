# Solicite frases ao usuário. Para parar, é só apertar enter. O programa deve apresentar cada frase e quantas vezes ela foi repetida.

frases = []
quant = 0

while True:
    frase = input('Digite uma frase: ')
    if frase == '':
        break
    else:
        frases.append(frase)
        quant += 1

print('Frases:', frases)
print('A frase foi repetida', quant, 'vezes.')