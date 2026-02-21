lista = []
cont = 0

while True:
   numero = input('Digite um número:')
   if numero == '':
      break
   else:
      num = int(numero)
      lista.append(num)

num_esc = int(input('Agora escolha um número dos que você digitou: '))
for i in (lista):
   if i == num_esc:
      cont += 1

print(lista)
print('O número', num_esc, 'apareceu', cont, 'vezes na lista.')