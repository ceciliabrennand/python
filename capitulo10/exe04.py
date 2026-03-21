with open('capitulo10/mensagem.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()
    print(conteudo)
    tamanho = len(conteudo)

# Conteúdo é uma lista, então precisa adicionar uma nova linha à uma lista
for i in range(tamanho): #Tem que botar range porque tamanho é um número
    conteudo[i] = conteudo[i].strip()

print(conteudo)

conteudo.append('Linha 5')

print(conteudo)
