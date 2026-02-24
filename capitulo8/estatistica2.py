# Média

def soma(valores:list)->float:
    return sum(valores)

def media(valores:list)->float:
    return soma(valores) / len(valores)

valores = []
while True:
    numero = input('Digite um número: ')
    if numero == '':
        break
    else:
        num = float(numero)
        valores.append(num)
    

print('Média:', media(valores))