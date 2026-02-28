def maior_numero(lista):
    lista.sort()
    return lista[-1]

lista = [3, 3, 4, 5, 6, 1, 7, 8, 9, 3, 4, 5, 6, 7, 5]

print(lista)
print('O maior número da lista é:', maior_numero(lista))