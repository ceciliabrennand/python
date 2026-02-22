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
