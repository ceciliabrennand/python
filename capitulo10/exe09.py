# Crie um programa que leia um arquivo e crie um novo arquivo contendo apenas as linhas que possuem mais de 10 caracteres.

with open('capitulo10/mensagem4.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()

print(conteudo)

lista = []

for i in range(len(conteudo)):
    conteudo[i] = conteudo[i].strip()
    if len(conteudo[i]) >= 10:
        lista.append(conteudo[i])

print(lista)
