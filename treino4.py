'''

Implemente uma função que descubra o maior conjunto de pessoas que se conhece 
mutuamente. A função recebe receber uma sequências de pares de pessoas que se 
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos 
conhecem todos os outros.

'''
#8%

    
def complete(dic, num):
    return len(dic) == num

def valid(dic, num):
    s = set(dic.keys())
    for pessoa in dic:
        s = s & dic[pessoa]
        s.add(pessoa)
        if len(s) < num:
            return False
    return True

def extensions(grafo, dic):
    list = [l for l in grafo if l not in dic]
    return list
        

def aux(grafo, dic, num):
    if complete(dic, num):
        return valid(dic, num)

    for x in extensions(grafo, dic):
        dic[x] = grafo[x]
        if aux(grafo, dic, num):
            return True
        dic.pop(x)
    return False
    



def amigos(conhecidos):
    
    grafo =  {}
    
    for grupo in conhecidos:
        for pessoa in grupo:
            if pessoa not in grafo:
                grafo[pessoa] = set(grupo) - set([pessoa])
            else:
                grafo[pessoa] = grafo[pessoa] | (set(grupo) - set([pessoa]))
    dic = {}
    
    for i in range(len(grafo.keys()), 1, -1):
        if aux(grafo, dic, i):
            return i



'''
Um anel de tamanho n (um número par) consiste numa permutação do números de 1 
até n em que a soma de quaisquer dois números adjacentes é um número primo
(considera-se que o primeiro elemento da sequência é adjacente do último).
Implemente uma função que calcule um destes aneis de tamanho n.

'''
#13%

def complete(l,n):
    return len(l) == n


def isPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        if i*i > n:
            return True
    return True



def extensions(list,n):
    if len(list) == 0:
        l = [a for a in range(1,n+1)]
    elif len(list) == n-1:
        l = [a for a in range(1,n+1) if a not in list and isPrime(list[-1]+a) and isPrime(list[0]+a) ]
    else:
        l = [a for a in range(1,n+1) if a not in list and isPrime(list[-1]+a)]
    return l
  
    
def aux(list,n):
    if complete(list,n):
        return list 
    for x in extensions(list,n):
        list.append(x)
        aux(list,n)
        if complete(list,n):
            return list
        list.remove(x)
    return []
    
def anel(n):
    return aux([],n)


'''

Implemente uma função que calcula o número mínimo de nós de um grafo 
não orientado que cobrem todas as arestas, ou seja, o tamanho do menor 
conjunto de nós que contém pelo menos um extremo de cada aresta. 
A função recebe a lista de todas as arestas do grafo, sendo cada aresta um 
par de nós.

'''

def cobertura(arestas):
    extremos = set([a for aresta in arestas for a in aresta])
    for i in range(len(extremos)+1):
        if aux(arestas, len(extremos), i, set()):
            return i

def extensions(arestas,s):
    list = []
    for a in arestas:
        n = set(a) - s
        if len(n) >0:
            list.append(n)
    return list
        


def aux(arestas, numExtremos, tentativas, s):
    if tentativas == 0:
        return len(s) == numExtremos
    for x in extensions(arestas, s):
        s = s | x
        if aux(arestas, numExtremos, tentativas-1, s):
            return True
        s = s - x
    return False



 '''

Um ciclo Hamiltoniano num grafo não orientado é um caminho no grafo que passa
uma e uma só vez por cada nó e termina no nó onde começou.

Implemente uma função que calcula o menor (em ordem lexicográfica) ciclo 
Hamiltoniano de um grafo, caso exista. Se não existir deve devolver None.

'''
#13%

def hamilton(arestas):
    vertices = set([v for a in arestas for v in a])
    arestas.sort()
    for a in vertices:
        list = aux(arestas, vertices, [a])
        if list:
            return list
    return None
    

def complete (arestas, vertices, list):
    if len(list) == len(vertices):
        if (list[-1], list[0]) in arestas or (list[0], list[-1]) in arestas:
            return True
    return False

def extensions(arestas, list):
    l = []
    for a in arestas:
        if a[0] == list[-1] and a[1] not in list:
            l.append(a[1])
        if a[1] == list[-1] and a[0] not in list:
            l.append(a[0])
    return l

def aux(arestas, vertices, list):
    if complete(arestas, vertices, list):
        return list
    for a in extensions (arestas, list):
        list.append(a)
        aux(arestas, vertices, list)
        if complete(arestas, vertices, list):
            return list
        list.remove(a)
    return []