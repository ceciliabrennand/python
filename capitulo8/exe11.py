# Sistema com múltiplas funções

def todas_notas():
    """Uma função para cadastrar notas em uma lista"""
    notas = []
    for i in range(1, 5 + 1):
        nota = float(input('Adicione a nota: '))
        notas.append(nota)
    return notas

def media(notas):
    """Uma função para calcular a média"""
    m = sum(notas) / len(notas)
    return m

def aprovacao(media:float):
    """Uma função para informar se o aluno foi aprovado (média ≥ 7)"""
    if media >= 7:
        return 'O aluno está aprovado.'
    elif media < 5:
        return 'O aluno está reprovado.'
    else: 
        return 'O aluno está em recuperação.'

print(""" MENU PRINCIPAL
1) Cadastrar notas do aluno
2) Calcular a média do aluno
3) Confirmar se o aluno está aprovado.
""")
opcao = int(input('Escolha uma opção (ex: 1): '))
if opcao == 1:
    print('Notas do aluno:', todas_notas())
if opcao == 2:
    notas = todas_notas()
    print('Notas do aluno:', notas)
    print('Média do aluno:', media(notas))
if opcao == 3:
    notas = todas_notas()
    m = media(notas)
    print('Notas do aluno:', notas)
    print('Média do aluno:', m)
    print(aprovacao(m))
else:
    print('Número inválido. Escolha uma opção válida.')