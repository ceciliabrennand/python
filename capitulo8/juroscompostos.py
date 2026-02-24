# %%

def juros_compostos(aporte, taxa, anos):
    resultado = aporte * (1 + taxa) ** anos
    return resultado

print(juros_compostos(1000, 0.13, 4))
# %%
