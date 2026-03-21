with open('capitulo10/mensagem2.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()

linhas = len(conteudo)

print(f'O arquivo tem {linhas} linhas')