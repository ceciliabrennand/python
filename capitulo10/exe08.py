# Copiar um arquivo e fazer a cópia do conteúdo

with open('capitulo10/mensagem3.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()

with open('capitulo10/mensagem3_copia.txt', 'w', encoding='utf-8') as copia:
    copia = copia.write(conteudo)