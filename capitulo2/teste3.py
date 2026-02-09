# brinquedo

height = int(input('Qual é a sua altura em cm? '))
credits = int(input('Quantos créditos você tem? '))

if height >= 137 and credits >= 10:
  print('Aproveite!')
elif height < 137 and credits >= 10:
  print('Você não é alto o suficiente.')
elif height >= 137 and credits < 10:
  print('Você não tem créditos suficientes.')
else:
  print('Você não tem altura nem créditos suficientes.')