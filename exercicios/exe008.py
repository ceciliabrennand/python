print('Sorveteria GG')
print('''Tipos:
        1) Casquinha: R$1,00
        2) Cascão: R$2,50
        3) Cestinha: R$4,00
''')

tipo = int(input('Escolha o tipo: '))
# poderia tirar o int e botar pra escrever a opção, depois tipo = tipo.lower() pra ficar tudo minúsculo 

print('''Sabores:
      1) Morango
      2) Creme
      3) Chocolate''')

sabor = int(input('Escolha o sabor: '))

print('''Coberturas: 
      1) Caramelo: R$1.50
      2) Morango: R$1.50
      3) Sem cobertura''')

cobertura = int(input('Escolha a cobertura: '))

if tipo == 1:
    valor = 1
elif tipo == 2:
    valor = 2.50
elif tipo == 3:
    valor = 4
else:
    print('Opção inválida. Recomece.')

if cobertura == 1 or cobertura == 2:
    valor += 1.50

# Aqui, poderia ser if cobertura in ['caramelo', 'morango']:
# valor += 1.50

print(f'O valor total ficou: R$ {valor}')