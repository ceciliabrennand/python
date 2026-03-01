# Sistema com múltiplas funções

def todas_notas():
    """Uma função para cadastrar notas em uma lista"""
    notas = []
    for i in range(1, 5 + 1):
        nota = float(input('Adicione a nota: '))
        notas.append(nota)
    return notas

def media(notas:float):
    """Uma função para calcular a média"""

def aprovacao(media:float):
    """Uma função para informar se o aluno foi aprovado (média ≥ 7)"""

print(""" MENU PRINCIPAL
1) Cadastrar notas do aluno
2) Calcular a média do aluno
3) Confirmar se o aluno está aprovado.
""")
opcao = int(input('Escolha uma opção (ex: 1): '))
if opcao == 1:
    print(todas_notas())


    