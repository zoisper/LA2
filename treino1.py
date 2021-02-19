

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


'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    nomes.sort()
    nomes.sort(key=lambda t: len(t.split()))
    return nomes



'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    dic = {}
    for i in ruas:
        if i[0] not in dic:
            dic[i[0]] = 1
        else:
            dic[i[0]] +=1
        if i[-1] not in dic:
            dic[i[-1]] = 1
        else:
            dic[i[-1]] +=1
    lista = sorted(dic.items())
    lista.sort(key=lambda t : (t[1], t[0]))
    return lista

'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def primo(n):
    for i in range(2, n-1):
        if n%i == 0:
            return False
    return True

def factoriza(n):
    r = 0
    for i in range (2, n):
        if primo(i) and n%i == 0:
            r += i
            while n%i == 0:
                n /= i
    return r

"""
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
"""
def frequencia(texto):
    dic ={}
    lista = texto.split()
    for i in lista:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    lista = sorted(dic.items())
    lista.sort(key=lambda t : t[1], reverse=True)
    lista = [l[0] for l in lista]
    return lista


# outra versao

from collections import Counter

def frequencia2(texto):
    lista = texto.split()
    lista.sort(key=Counter(lista).get, reverse=True)
    lista = list(dict.fromkeys(lista))
    return lista



