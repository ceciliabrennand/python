# Quantas vezes a letra 'a' aparece numa palavra

total = 0

palavra = input('Escreva uma palavra: ').lower()

for i in palavra:
    total += i == 'a' # Isso é possível porque false = 0 e true = 1, então quando for true, vai somar 1 em total

print(f'A letra "a" aparece em {palavra} um total de {total} vezes.')