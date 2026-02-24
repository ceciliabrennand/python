dados = {}

while True:
    frase = input('Digite uma frase: ')
    if frase == '':
        break
    if frase not in dados:
        dados[frase] = 1
    else:
        dados[frase] += 1

# Se a frase não estiver em frases, então o valor é 1. Senão, é adicionado mais 1 ao valor. 

for i, j in dados.items():
    print(i, '-->', j)

    