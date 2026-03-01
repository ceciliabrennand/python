txt = 'Meu novo arquivo!'

nome_arquivo = "C:/Users/cisab/Documents/python/capitulo10/historia2.txt"

with open(nome_arquivo, mode='w') as open_file:
    open_file.write(txt)