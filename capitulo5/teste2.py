# NÚMEROS DIVISÍVEIS POR 4 ATÉ 100

cont = 1
while cont <= 100:
    if cont % 4 == 0:
        print(cont)
    cont += 1

#FORMA DO TÉO ME WHY

# count = 4
# while count <= 100:
#     resto = count % 4
#     if resto == 0:
#         print(count)
#     count += 1

# %% USANDO FOR
max_num = 100

for i in range(1, max_num + 1):
    if i % 4 == 0:
        print(i)