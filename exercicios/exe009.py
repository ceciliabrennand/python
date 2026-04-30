# Verificar se alguém é da família brennand

nome = input('Insira seu nome completo: ')
nome = nome.lower()
if 'brennand' in nome and 'soares' in nome:
    print('Você faz parte da família Brennand e da família Soares!')
elif 'brennand' in nome:
    print('Você pertence à família Brennand!')
elif 'soares' in nome:
    print('Você pertence à família Soares!')
else:
    print('Você não é Brennand nem Soares')