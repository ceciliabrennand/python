lista = [120, 'python', 120.01, 'asw', False, [10, 20]]

# Faça um programa que retorne o elemento na posição -1, elemento na primeira posição da lista e o último caractere do segundo elemento da lista

print(lista)
print('Último elemento:', lista[-1])
print('Primeiro elemento:', lista[0])

for i in lista[1]:
    if i == 'n':
        print('Último caractere do segundo elemento:', i)
