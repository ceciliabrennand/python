# %%
arquivo= "C:/Users/cisab/Documents/python/capitulo10/data.csv"

open_file = open(arquivo)

with open(arquivo, "r", encoding="utf-8") as open_file:
    lines = open_file.readlines()

print(lines)

for l in lines:
    print(l)

# %%

dados = {}

chaves = lines[0].strip('\n').split(';')
print(chaves)
for c in chaves:
    dados[c] = []
print(dados)

# %%

for l in lines[1:]: # percorrer todas as linhas a partir da segunda

    valores = l.strip('\n').split(';') # para remover o \n e quebra em ;, fazendo cada um virar uma lista. exemplo: Teo;32;streamer --> ['Teo', '32', 'streamer']

    for i in range(0, len(valores)): # passa por todas as chaves do dicionário e adiciona esses valores que foram recebidos. percorre 0, 1, 2, que seria teo, 32 e streamer, na ordem

        dados[chaves[i]].append(valores[i]) # valores[i] na posição 0 é teo, na posição 2 é 32 e na 3 é streamer. e aí bota na posição 0 que é nome, na posição 2 que é idade e na posição 3 que é profissão, aí adiciona na lista

print(dados)
# %%

# Média de idades

idades = []
for i in dados['idade']:
    idades.append(int(i))

media = sum(idades) / len(idades)
print(media)
# %%
