def soma(*numeros):
    total = sum(numeros)
    return total
    
def media(*numeros):
    if len(numeros) == 0 or len(numeros) == 1:
        erro = 'Não podemos fazer a média sem no mínimo 2 números.'
        return erro
    else:
        m = soma(*numeros) / len(numeros)
        return m

lista = []

while True:
    num = input('Digite um número:')
    if num == '':
        break
    else:
        numero = int(num)
        lista.append(numero)

print(media(*lista))

# %% código mais limpo 

def soma(*numeros):
    total = sum(numeros)
    return total
    
def media(*numeros):
    if len(numeros) < 2:
        erro = 'Não podemos fazer a média sem no mínimo 2 números.'
        return erro
    
    m = soma(*numeros) / len(numeros)
    return m

lista = []

while True:
    num = input('Digite um número:')
    if num == '':
        break
    else:
        numero = int(num)
        lista.append(numero)

print(media(*lista))