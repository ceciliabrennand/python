txt = 'Mas ja lembrei, tudo certo '

nome_arquivo = "C:/Users/cisab/Documents/python/capitulo10/historia2.txt"

with open(nome_arquivo, mode='a') as open_file:
    open_file.write(txt)