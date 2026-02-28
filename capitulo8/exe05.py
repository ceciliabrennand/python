def potencia(base, expoente=2):
    return base ** expoente

num = int(input('Digite um número: '))
total = potencia(num)
print(num, 'elevado a', 2, 'é igual a:', total)