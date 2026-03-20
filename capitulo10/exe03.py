# Fazendo de outra forma

with open('capitulo10/mensagem.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()
    for i in conteudo:
        print(i)