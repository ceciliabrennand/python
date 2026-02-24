# %%

def juros_compostos(aporte:int, taxa:float, anos:int)->float:
    """juros_compostos serve para calcular o retorno financeiro de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos) para cálculo do valor a ser retornado. 
    
    aporte: um número inteiro em R$
    
    taxa: um número float entre 0 e 1
    
    anos: um número inteiro >= 1"""
    resultado = aporte * (1 + taxa) ** anos
    return resultado

print(juros_compostos(1000, 0.13, 4))
# ou print(juros_compostos(taxa=0.13, anos=4, aporte=1000))
