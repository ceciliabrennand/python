# %%
arquivo= "C:/Users/cisab/Documents/python/capitulo10/data.csv"

open_file = open(arquivo)

with open(arquivo, "r", encoding="utf-8") as open_file:
    data = open_file.readlines()

print(data)

for linha in data:
    print(linha)

# %%

dados = {}

chaves = data[0].strip('\n').split(';')
print(chaves)
for c in chaves:
    dados[c] = []
print(dados)

# %%
