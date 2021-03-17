

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
    alunos = sorted(prefs)
    candidatos = prefs.copy()
    escolhidos = []
    for i in alunos:
        for j in candidatos[i]:
            if j not in escolhidos:
                escolhidos.append(j)
                del candidatos[i]
                break
    return sorted(candidatos)


'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    result = sorted(nomes)
    result.sort(key=lambda x : len(x.split()))
    return result


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
    result = {}
    for i in ruas:
        if i[0] not in result:
            result[i[0]] = 1
        else:
            result[i[0]] += 1
        if i[-1] not in result:
            result[i[-1]] = 1
        elif i[0] != i[-1]:
            result[i[-1]] +=1
    result = sorted(result.items())
    result.sort(key=lambda x : x[1])
    return result


'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def factoriza(n):
    result = 0
    for i in range(2, n//2 +1): 
        if n%i == 0:
            result += i
            while (n%i == 0):
                n //= i
        if n < i:
            break
    return result


"""
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
"""

def frequencia(texto):
    result = {}
    palavras = texto.split()
    for i in palavras:
        if i not in result:
            result [i] = 1
        else:
            result[i] +=1
    result = sorted(result.items())
    result.sort(key=lambda x: x[1], reverse=True)
    result = [x[0] for x in result]
    return result


'''
Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.
'''

def tabela(jogos):
    classificacao = dict((e,[0,0]) for (e,g,e,g) in jogos)
    for e in jogos:
        score = e[1] - e[3]
        if score > 0:
            classificacao [e[0]][0] +=3
        elif score < 0:
            classificacao [e[2]][0] +=3
        else:
            classificacao [e[0]][0] +=1
            classificacao [e[2]][0] +=1
        classificacao [e[0]][1] += score
        classificacao [e[2]][1] -= score
    result = sorted(classificacao.items())
    result.sort(key=lambda x : x[1][1], reverse=True)
    result.sort(key=lambda x : x[1][0], reverse=True)
    result = [(r[0],r[1][0]) for r in result]
    return result


"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def hacker(log):
    hack = {}
    troca = lambda x,y : x if y == '*' else y
    intersecta = lambda x,y : "".join(map(troca, x,y))
    for i in log:
        if i[1] not in hack:
            hack[i[1]] = i[0]
        else:
            hack[i[1]] = intersecta(hack[i[1]],i[0])
    result = sorted(hack.items())
    result = [(i[1],i[0]) for i in result]
    result.sort(key=lambda x : sum(map(lambda l : 0 if l == "*" else 1, x[0])), reverse=True)
    return result


'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def valida(isbn):
    soma = 0
    for i in range(len(isbn)):
        if i%2 == 0:
            soma += eval(isbn[i])
        else:
            soma += eval(isbn[i])*3
    return soma % 10 == 0


def isbn(livros):
    result = []
    for i in livros:
        if not valida(livros[i]):
            result.append(i)
    result.sort()
    return result


'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''

def repete(palavra,n):
    repetidos = 0
    sufixo = list(palavra)
    for i in range(1, len(palavra)):
        if palavra[:-i] == palavra[i:]:
            del sufixo[: len(palavra)-i]
            break
    sufixo = "".join(sufixo)
    result = palavra*(n>0)  + sufixo*(n-1)
    return result


'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''

def robot(comandos):
    result = []
    entrada = comandos.split('H')
    if entrada[-1] == '':
        entrada.pop()
    for i in entrada:
        movs = [0,0,0,0]
        aux = [0,0,0,0]
        p = 3
        for j in i:
            if j == 'E':
                p = (p+1)%4
            elif j == 'D':
                p = (p+3)%4
            elif p <2:
                aux[p] -= 1
                aux[(p+2)%4] -=1
                movs[p] = min(movs[p],aux[p])
            else:
                aux[p] += 1
                aux[(p+2)%4] +=1
                movs[p] = max(movs[p], aux[p])
        result.append(tuple(movs))
    return result
