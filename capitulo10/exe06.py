def soma(conteudo):
    total_palavras = 0
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].strip('\n')
        palavras = conteudo[i].split() #Tem que usar split porque o computador não entende que 1 string tem palavras separadas

        for palavra in palavras:
            total_palavras += 1
    return total_palavras

with open ('capitulo10/mensagem3.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()

print(conteudo)

total = soma(conteudo)

print('O total de palavras é: ', total)
