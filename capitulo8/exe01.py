# Programa que recebe um número e vê se é par ou ímpar

def par_impar(x:int):
    if x % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
    
numero = int(input('Digite um número: '))
(par_impar(numero))