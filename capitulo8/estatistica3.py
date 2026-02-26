# Média

def soma(a:float, b:float, *args)->float:
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a, b, *args) / (len(args) + 2)

a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
c = float(input('Digite outro número: '))

print('Média:', media(a, b, c))