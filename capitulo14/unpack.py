# %%
a = 1
b = 5

print(a)
print(b)

# %%

c = a
a = b
b = c

print(a)
print(b)

# %%

a, b = b, a

print(a)
print(b)

# %%

a, b, *resto = 1, 2, 3, 4, 5, 6, 7, 8
print(a,b, resto)

# %%

*resto, a, b = 1, 2, 3, 4, 5, 6, 7, 8
print(resto, a,b)

# %%

a, *resto, b = 1, 2, 3, 4, 5, 6, 7, 8
print(a, resto, b)

# %%

def soma(a, *args):
    total = a + sum(args)
    return total

soma(1, 2, 3, 4, 5)

# %%

def soma_quatro(a, b, c, d):
    return a+b+c+d
values = [1, 2, 3, 4]

soma_quatro(*values)

# %%

dados = {'nome': 'cec', 'sobrenome':'brennand'}
for i, j in dados.items():
    print(i, j)