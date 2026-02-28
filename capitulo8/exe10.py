def contador(inicio:int, fim:int):
    def contar():
        if inicio < fim:
            for i in range(inicio, fim + 1):
                print(i)
        else:
            for i in range(inicio, fim - 1, -1):
                print(i)
    contar()


inicio = int(input('Digite um número: '))
fim = int(input('Digite outro número: '))

contador(inicio, fim)