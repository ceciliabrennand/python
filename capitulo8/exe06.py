def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

numero = input('Digite um número: ')
num = int(numero)
print(num, 'é par?')
print(par_impar(num))

