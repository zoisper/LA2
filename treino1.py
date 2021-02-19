

# https://codeboard.io/projects/148692


"""
Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.
"""

def aloca(prefs):
    colocados = []
    l = 0;
    while (l < len(prefs)):
        x = min(prefs)
        j = 0
        while (x in prefs) and (j < len(prefs[x])):
            if prefs[x][j] not in colocados:
                colocados.append(prefs[x][j])
                del prefs[x]
            else:
                j = j + 1
        l = l + 1
    return list(prefs)

"""
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
"""

from collections import Counter

def frequencia(texto):
    lista = texto.split(' ')
    lista.sort(key=Counter(lista).get, reverse=True)
    lista = list(dict.fromkeys(lista))
    return lista



