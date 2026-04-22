x = []

for i in range(1, 101):
    x.append(i)
print(x)

# Isso é a mesma coisa que o código abaixo

y = [i for i in range(1, 101)]
print(y)

# Dá pra ficar bem mais complexo

def eh_par(x):
    return x % 2 == 0

z = [eh_par(i) for i in range(1,101)]
print(z)

# Só mostrar os números pares

w = [i for i in range(1, 101) if eh_par(i)]
print(w)