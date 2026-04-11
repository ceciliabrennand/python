# %%

import requests # para realizar requisições na web
import json # para tratar json de listas/dicionarios para arquivos json
from tqdm import tqdm

import pandas as pd

ceps = [
    "50010010",
    "50010050",
    "52061055",
    "50030030",
    "50030120"
]

url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

print(dados)

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv('capitulo12/ceps.csv', sep=';')

# %%

with open('capitulo12/ceps.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)