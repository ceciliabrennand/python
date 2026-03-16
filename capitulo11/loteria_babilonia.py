import random

def loteria(numero:int):
    if numero < num_sorteado:
        resposta = print('Errou. Seu chute foi menor que o número sorteado.')
        return resposta
    elif numero > num_sorteado:
        resposta = print('Errou. Seu chute foi maior que o número sorteado.')
        return resposta                 
   
num_sorteado = random.randint(1, 100)
i = 1

print('------LOTERIA DA BABILÔNIA------')
print('Você tem 3 tentativas para acertar o número sorteado.')

while i < 4:
    print(f'Tentativa número {i}: ')
    num_escolhido = int(input('Escolha um número de 1 a 100: '))
    if num_escolhido != num_sorteado:
        loteria(num_escolhido) 
        i += 1
    else:
        print('Parabéns! Você acertou o número sorteado.')
        break

print(f'''Que pena, você não conseguiu. 
O número sorteado era {num_sorteado}.
Tente novamente!''')