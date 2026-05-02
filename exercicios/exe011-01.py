# Quantas vezes a letra 'a' aparece numa palavra

total = 0

palavra = input('Escreva uma palavra: ') # Poderia ser input('Escreva uma palavra: ').lower()

for i in palavra:
    if i == 'a' or i == 'A':
        total += 1

print(f'A letra "a" aparece em {palavra} um total de {total} vezes.')