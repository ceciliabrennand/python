# QUANTAS VEZES "A" APARECE EM UMA PALAVRA

cont = 0
palavra = input('Digite uma palavra qualquer: ')

for i in palavra:
    if i == 'a' or i == 'á' or i == 'ã' or i == 'à' or i == 'â':
        cont += 1

print('A letra "A" aparece', cont, 'vezes na palavra', palavra)