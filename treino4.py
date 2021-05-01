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



