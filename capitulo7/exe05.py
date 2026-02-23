dicionario = {'name':'alice', 'age':35, 'city':'recife', 'profession':'doctor'}

print(dicionario)

dicionario.pop('profession')

print(dicionario)

print('Itens:', dicionario.items())

if 'age' in dicionario:
    print('Verdadeiro')