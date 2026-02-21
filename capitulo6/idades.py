idades = []

num = (input('Quantas pessoas tem na sua sala? '))
numero = int(num)
cont = 1

while cont <= numero:
    idade = input('Digite as idades: ')
    idades.append(int(idade))
    cont += 1

print(idades)

media = sum(idades) / len(idades)
menor_idade = min(idades)
maior_idade = max(idades)

print('MÉDIA:', media)
print('Menor idade:', menor_idade)
print('Maior idade:', maior_idade)