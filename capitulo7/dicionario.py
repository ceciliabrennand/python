# %%
dados_cec = {
    'nome':'cecília',
    'sobrenome':'brennand',
    'idade':'26',
    'filhos':False,
    'cachorros':['kovu', 'annie', 'nami'],
    'cargos':[
        {'nome':'ds jr', 'empresa':'tapps'},
        {'nome':'ds pl', 'empresa':'sas'},
        {'nome':'ds sr', 'empresa':'boticario'},
        {'nome':'ds espec.', 'empresa':'via varejo'}
    ]
}

print(dados_cec['idade'])
print(dados_cec['cachorros'][-1])
print(dados_cec['cargos'][-1]['empresa'])

dados_cec['série'] = 'arcane'
print(dados_cec)
print('Chaves:', dados_cec.keys())
print('Valores:', dados_cec.values())
print('Itens:', dados_cec.items())

for i in dados_cec:
    print(i, '-->', dados_cec[i])

for i in dados_cec.items():
    print(i)

for chave, valor in dados_cec.items():
    print(chave, '-->', valor)

    