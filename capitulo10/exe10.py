lista = []

def adicionar_usuario():
    print('Adicione quantos usuários quiser. Se quiser parar, aperte enter sem nada escrito.')
    while True:
        usuario = input('Qual o nome do usuário? ')
        if usuario == '':
            break
        idade = input('Qual a idade do usuário? ')
        lista.append(f'{usuario}; {idade}')
        


with open('capitulo10/lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.readlines()

print(''' 
O que você deseja fazer?
1) Adicionar novos usuários
2) Listar todos os usuários cadastrados
3) Buscar um usuário pelo nome
''')

escolha = input('Escolha uma opção pelo número (ex: 1): ')
try:
    int(escolha)
except ValueError:
    print('Erro. Digite um número.')

if int(escolha) < 1 or int(escolha) > 3:
    print('Escolha um número válido.')
if int(escolha) == 1:
    adicionar_usuario()
    with open('capitulo10/lista_alunos.txt', 'a', encoding='utf-8') as arquivo:
        for i in lista:
            arquivo.write('\n' + i)
elif int(escolha) == 2:
    with open('capitulo10/lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
        for i in range(len(conteudo)):
            conteudo[i] = conteudo[i].strip('\n')
        print(conteudo)
elif int(escolha) == 3: # Refazer
    nome = input('Qual nome você deseja buscar? ')
    with open('capitulo10/lista_alunos.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.readlines()
    for i in range(len(conteudo)):
        conteudo[i] = conteudo[i].strip('\n').split()
        if conteudo[i] == nome:
            print(conteudo[i])