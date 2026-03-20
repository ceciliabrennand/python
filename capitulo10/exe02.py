arquivo = "capitulo10/mensagem.txt"

with open(arquivo, 'r', encoding='utf-8') as open_file:
    print(open_file.read())