arquivo= "C:/Users/cisab/Documents/python/capitulo10/data.csv"

open_file = open(arquivo)

with open(arquivo, "r", encoding="utf-8") as open_file:
    data = open_file.readlines()

print(data)

for linha in data:
    print(linha)