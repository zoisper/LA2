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





def amigos(conhecidos):
    pessoas = set([c for grupo in conhecidos for c in grupo])
    
    for n in range(len(pessoas)+1, 2 ,-1):
        if aux(conhecidos, pessoas, n, set()):
            return n

def extensions(conhecidos, pessoas, s):
    list = [p for p in pessoas if p not in s]
    for l in list.copy():
        for p in s:
            if (l,p) not in conhecidos and (p,l) not in conhecidos:
                list.remove(l)
                break
    return list
    
def complete(n, s):
    return len(s) == n

def aux(conhecidos, pessoas, n, s):
    if complete(n, s):
        return True
    for x in extensions(conhecidos, pessoas, s):
        s.add(x)
        if aux(conhecidos, pessoas,n , s):
            return True
        s.remove(x)
    return False



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
#9%

def complete(n, s):
    return len(s) == n

def valid(arestas, s):
    for a in arestas:
        if a[0] not in s and a[1] not in s:
            return False
    return True

def extensions(vertices, s):
    return [a for a in vertices if a not in s]

def aux(arestas, vertices, n, s):
    if complete(n,s):
        return valid(arestas, s)
    for x in extensions(vertices, s):
        s.add(x)
        if aux(arestas, vertices, n, s):
            return True
        s.remove(x)
    return False
        


def cobertura(arestas):
    vertices = set([a for aresta in arestas for a in aresta])
    for n in range(len(vertices)+1):
        if aux(arestas, vertices, n, set()):
            return n
    return 0


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


'''

Implemente uma função que determina quantas permutações dos n primeiros digitos 
são múltiplas de um dado número d. Por exemplo se n for 3 temos as seguintes 
permutações: 123, 132, 213, 231, 312, 321. Se neste caso d for 3 então todas 
as 6 permutações são múltiplas.

'''
#13%

def constroi(list):
    r = 0
    for i in range(len(list)):
        r *=10
        r+=list[i]
    return r

def complete(n, list):
    return len(list) == n

def valid(d, list):
    return constroi(list)%d == 0

def extensions(n, list):
    return [a for a in range(1, n+1) if a not in list]

def aux(n, d, list):
    if complete(n, list):
        if valid(d, list):
            return 1
        return 0
    result = 0
    for x in extensions(n, list):
        list.append(x)
        result += aux(n,d, list)
        list.pop()
    return result

def multiplos(n,d):
    return aux(n,d,[])

'''

Os sacos de um supermercado tem um limite de peso que conseguem levar. 
Implemente uma função que o ajude a determinar o número mínimo de sacos que 
necessita para levar todas as compras. A função recebe o peso máximo que os
sacos conseguem levar e uma lista com os pesos de todos os items que pretende 
comprar. Deverá devolver o número mínimo de sacos que necessita para levar 
todas as compras.

'''
#9%

def sacos(peso,compras):
    total = sum(compras)
    minimo = total//peso
    
    for i in range(minimo,len(compras)+1):
        list = [peso for a in range(i)]
        if aux(peso, compras, total, list, []):
            return i
            
def extensions(compras, escolhidos):
    return [a for a in range(len(compras)) if a not in escolhidos]

def escolhe(produto, list):
    for i in range(len(list)):
        if list[i] - produto >=0:
            return i
    return -1

def aux(peso, compras, total, list, escolhidos):
    if total == 0:
        return True
    for indexProduto in extensions(compras, escolhidos):
        escolhidos.append(indexProduto)
        indexSaco = escolhe(compras[indexProduto], list)
        if indexSaco == -1:
            return False
        list[indexSaco] -= compras[indexProduto]
        total -= compras[indexProduto]
        if aux(peso, compras, total, list, escolhidos):
            return True
        escolhidos.pop()
        list[indexSaco] += compras[indexProduto]
        total += compras[indexProduto]
    return False
        