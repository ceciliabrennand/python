# %%

nome_arquivo = "C:/Users/cisab/Documents/python/capitulo10/historia.txt"

open_file = open(nome_arquivo)

with open(nome_arquivo, "r", encoding="utf-8") as open_file:
    conteudo = open_file.read()
    print(conteudo)