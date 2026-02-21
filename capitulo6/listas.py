# Uma maneira de definir listas

idades = [15, 50, 38, 28, 25, 18, 44]

print('Soma das idades:', sum(idades))

print('Quantidade de itens:', len(idades))

print('Média das idades:', sum(idades)/len(idades))

print('Menor idade:', min(idades))

print('Maior idade:', max(idades))

cec = ['cecília', 26, 'publicitária', 'recife', 1999, ['Kovu', 'Annie', 'Nami']]
print(cec[5][1])

tamanho = len(cec)
ultimo = len(cec) - 1
cachorros = cec[ultimo]
ultimo_cachorro = len(cachorros) - 1
print(cachorros[ultimo_cachorro])

# Isso poderia ser apenas:

ultimo = cec[-1]
print(ultimo)
ultimo_cachorro = ultimo[-1]
print(ultimo_cachorro)

print(cec[0:4])
print(cec[5][-2:])
print(cec[::-1])