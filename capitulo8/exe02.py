#num = int(input('Digite um número: '))

def piramide(n):
    for i in range(1, n + 1): #precisa do +1 se não vai só até o num anterior
        print((str(i) + '  ') * i)

piramide(5)