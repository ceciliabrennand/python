def busca(nome_arquivo, palavra):
    total = 0

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()

    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].strip('\n').split()
        for i in conteudo[i]:
            if i == palavra:
                total += 1
    return total

nome_arquivo = input('Qual arquivo você quer procurar? (Ex: mensagem3.txt): ')
palavra = input('Qual palavra você quer procurar no arquivo? (Ex: radio): ')


total = busca(nome_arquivo, palavra)

print(f'O total de vezes que a palavra {palavra} apareceu foi de: {total}')