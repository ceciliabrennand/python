import random  

def get_input():
    while True:  
        print(f'Tentativa número {i}: ')  
        try:
            num_escolhido = int(input('Escolha um número de 1 a 100: '))
        except ValueError:
            print('Isso não é um número. Tente novamente.')
            continue
        if 1 <= num_escolhido <= 100:
            return num_escolhido
        print('Número invalido. Por favor, escolha um número de 1 a 100.')    
   
num_sorteado = random.randint(1, 100)

print('------LOTERIA DA BABILÔNIA------')
print('Você tem 3 tentativas para acertar o número sorteado.')

for i in range(1, 4):
    num_escolhido = get_input()
        
    if num_escolhido > num_sorteado:
        print('Errou. O número sorteado é menor.')
    elif num_escolhido < num_sorteado:
        print('Errou. O número sorteado é maior.')
    else:
        print('Parabéns! Você acertou o número sorteado.')
        break

else:
    print(f'''Que pena, você não conseguiu. 
O número sorteado era {num_sorteado}.
Tente novamente!''')