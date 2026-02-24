# Média

def soma(a:float, b:float, *args):
    valores = [a, b] + list(args)
    return sum(valores)

def media(a:float, b:float, c=0)->float:
    return soma(a, b) / 2

x = float(input('Digite um número: '))
y = float(input('Digite outro número: '))

print('Média:', media(x, y))