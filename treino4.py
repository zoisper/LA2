'''

Implemente uma função que descubra o maior conjunto de pessoas que se conhece 
mutuamente. A função recebe receber uma sequências de pares de pessoas que se 
conhecem e deverá devolver o tamanho do maior conjunto de pessoas em que todos 
conhecem todos os outros.

'''
#11%

    
def constroi(lista):
    dic = {}
    for grupo in lista:
        for pessoa in grupo:
            if pessoa not in dic:
                dic[pessoa] = set(grupo) - {pessoa}
            else:
                dic[pessoa] = dic[pessoa] | set(grupo) - {pessoa}
    return dic


def complete(n,s):
    return len(s) == n

def extensions(pessoas,s, dic, impossiveis):
    r = [pessoa for pessoa in pessoas if pessoa not in s and pessoa not in impossiveis]
    errados = []
    for i in range(len(r)):
        for d in s:
            if r[i] not in dic[d]:
                errados.append(r[i])         
                break
    for i in errados:
        r.remove(i)
    return r
    
def aux(pessoas, dic, n, s, impossiveis):
    if complete(n, s):
        return True
    for x in extensions(pessoas, s, dic, impossiveis):
        s.add(x)
        if aux(pessoas, dic, n, s, impossiveis):
            return True
        impossiveis.add(x)
        s.remove(x)
    return False
        


def amigos(conhecidos):
    
    dic = constroi(conhecidos)
    pessoas = list(dic.keys())
    if not pessoas:
        return 0
    for n in range(len(pessoas)+1,1,-1):
        if aux(pessoas, dic, n, set(), set()):
            return n




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
#13%

def complete(n, s):
    return len(s) == n

def valid(arestas, s):
    for a in arestas:
        if a[0] not in s and a[1] not in s:
            return False
    return True

def extensions(vertices, ultimo):
    return [a for a in vertices if vertices.index(a) > ultimo]

def aux(arestas, vertices, n, ultimo, s):
    if complete(n,s):
        return valid(arestas, s)
    for x in extensions(vertices, ultimo):
        s.add(x)
        if aux(arestas, vertices, n, vertices.index(x), s):
            return True
        s.remove(x)
    return False
        

def cobertura(arestas):
    vertices = set([a for aresta in arestas for a in aresta])
    vertices = list(vertices)
    for n in range(len(vertices)+1):
        if aux(arestas, vertices, n, -1, set()):
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
#11%

def sacos(peso,compras):
    if len(compras) == 0:
        return 0
    minimo = sum(compras)//peso
    for i in range(minimo,len(compras)+1):
        if aux(peso, compras, [peso]*i):
            return i
            

def extensions(produto, list):
    return [i for i in range(len(list)) if list[i]-produto >=0]
    

def aux(peso, compras, list):
    if not compras:
        return True
    produto = compras.pop()
    for indexSaco in extensions(produto, list):
        list[indexSaco] -= produto
        if aux(peso, compras, list):
            return True
        list[indexSaco] += produto
    compras.append(produto)
    return False


'''

Implemente uma função que dada uma lista de conjuntos de inteiros determine qual
o menor número desses conjuntos cuja união é idêntica à união de todos os 
conjuntos recebidos.

'''
#10%

def complete(n, s):
    return n == len(s)

def valid (total, s):
    r = set()
    for a in s:
        r = r | a
    return total == len(r)

def extensions(sets, ultimo):
    return [a for a in sets if sets.index(a) > ultimo ]
    
def aux(sets, total, n, ultimo, s ):
    if complete(n, s):
        return valid(total, s)
    for x in extensions(sets, ultimo):
        s.append(x)
        if aux(sets, total, n, sets.index(x), s):
            return True
        s.pop()
    return False

def uniao(sets):
    total = 0
    tmp = set()
    for a in sets:
        tmp = tmp | a
    total = len(tmp)
    for n in range(len(sets)+1):
        if aux(sets, total, n, -1, []):
            return n
    return total



'''

Implemente um função que calcula a menor string que contém todas as palavras 
recebidas na lista de input. Assuma que todas as palavras são disjuntas entre si, 
ou seja, nunca haverá inputs onde uma das palavras está contida noutra.

'''
#11%

def extensions(strings, ss):
    return [pal for pal in strings if pal not in ss]

def complete(n, ss):
    return len(ss) == n

def valid(strings, ss):
    for pal in strings:
        if pal not in ss:
            return False
    return ss

def junta(ss, pal):
    r = 0
    for i in range(1,len(pal)):
        if ss[-i:] == pal[0:i]:
            r = i
    ss = ss + pal[r:]
    return ss
    
def aux(strings, n, ss):
    if complete(n, ss):
        return valid(strings, ss)
    for pal in extensions(strings, ss):
        ant = ss
        ss = junta(ss, pal)
        result = aux(strings, n, ss )
        if result:
            return result
        ss = ant
    return False
        
     

def superstring(strings):
    total = sum(map(len, strings))
    
    if total == 0:
        return ""
        
    minimo = len(min(strings, key=len))
    
    for i in range(minimo,total +1):
        result = aux(strings, i, "")
        if result:
            return result