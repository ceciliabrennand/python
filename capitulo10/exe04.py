with open('capitulo10/mensagem.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)

# Conteúdo é uma lista, então precisa adicionar uma nova linha à uma lista
for i in range(len(conteudo)):
    conteudo[i] = conteudo[i].strip()

print(conteudo)
