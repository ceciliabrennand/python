tot = 0

print('----- SORVETERIA -----')
print("""Qual sorvete você deseja?
1) Casquinha - R$1,00
2) Cascão - R$2,50
3) Cestinha - R$4,00""")

sorv = int(input('Escolha um número: '))

if sorv == 1:
    tot += 1
elif sorv == 2:
    tot += 2.50
elif sorv == 3:
    tot += 4
else:
    print('Escolha um número válido.')

print("""Qual sabor você deseja?
1) Morango
2) Creme
3) Chocolate""")
sab = int(input('Escolha um número: '))

print("""Deseja cobertura?
1) Caramelo - R$1,50
2) Morango - R$1,50
3) Chocolate - R$1,50
4) Sem cobertura""")
cob = int(input('Escolha um número: '))

if cob == 1 or cob == 2 or cob == 3:
    tot += 1.50
    print('O total deu: R$', tot)
elif cob == 4:
    print('O total deu: R$', tot)
else: 
    print('Escolha um número válido.')