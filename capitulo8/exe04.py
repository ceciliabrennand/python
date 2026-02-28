# Função com retorno

def soma(a:int, b:int)->int:
    return a + b

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

total = soma(n1, n2)

print(n1, '+', n2, '=', total)