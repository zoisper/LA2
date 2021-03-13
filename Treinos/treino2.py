#https://codeboard.io/projects/153023


'''
Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 
'''

def area(p,mapa):
    visitados = set()
    orla = [p]
    while orla:
        x,y = orla.pop(0)
        visitados.add((x,y))
        if x-1>=0 and (x-1,y) not in visitados and mapa[x-1][y] == '.':
            orla.append((x-1,y))
        if x+1<len(mapa) and (x+1,y) not in visitados and mapa[x+1][y] == '.':
            orla.append((x+1,y))
        if y-1>=0 and (x,y-1) not in visitados and mapa[x][y-1] == '.':
            orla.append((x,y-1))
        if y+1<len(mapa) and (x,y+1) not in visitados and mapa[x][y+1] == '.':
            orla.append((x,y+1))
    return len(visitados)


'''
O objectivo deste problema é determinar quantos movimentos são necessários para 
movimentar um cavalo num tabuleiro de xadrez entre duas posições.
A função recebe dois pares de coordenadas, que identificam a origem e destino pretendido,
devendo devolver o número mínimo de saltos necessários para atingir o destino a partir da origem.
Assuma que o tabuleiro tem tamanho ilimitado.

'''

def saltos(o,d):
    if o == d:
        return 0
    orla = [(o[0],o[1],0)]
    visitados = set()
    while orla:
        x,y,s = orla.pop(0)
        visitados.add((x,y))
        if (x-2,y-1) not in visitados:
            if (x-2,y-1)  == d:
                return s+1
            orla.append((x-2,y-1,s+1))
        if (x+2,y-1) not in visitados:
            if (x+2,y-1)  == d:
                return s+1
            orla.append((x+2,y-1,s+1))
        if (x-2,y+1) not in visitados:
            if (x-2,y+1)  == d:
                return s+1
            orla.append((x-2,y+1,s+1))
        if (x+2,y+1) not in visitados:
            if (x+2,y+1)  == d:
                return s+1
        if (x+1,y-2) not in visitados:
            if (x+1,y-2)  == d:
                return s+1
            orla.append((x+1,y-2,s+1))
        if (x-1,y-2) not in visitados:
            if (x-1,y-2)  == d:
                return s+1
            orla.append((x-1,y-2,s+1))
        if (x+1,y+2) not in visitados:
            if (x+1,y+2)  == d:
                return s+1
            orla.append((x+1,y+2,s+1))
        if (x-1,y+2) not in visitados:
            if (x-1,y+2)  == d:
                return s+1
            orla.append((x-1,y+2,s+1))
    return 0


'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

'''
def build(ruas):
    grafo = {}
    for r in ruas:
        if r[0] not in grafo:
            grafo[r[0]] = {}
            grafo[r[0]][r[0]] = 0
        if r[-1] not in grafo:
            grafo[r[-1]] = {}
            grafo[r[-1]][r[-1]] = 0
        if r[0] != r[-1]:
            if r[-1] not in grafo[r[0]]:
                grafo[r[0]][r[-1]] = len(r)
                grafo[r[-1]][r[0]] = len(r)
            else:
                grafo[r[0]][r[-1]] = min(len(r), grafo[r[0]][r[-1]])
                grafo[r[-1]][r[0]] = min(len(r), grafo[r[-1]][r[0]])

    
    for a in grafo:
        for b in grafo:
            if b not in grafo[a]:
                grafo[a][b] = float("inf")

    return grafo
 
def tamanho(ruas):
    dists = build(ruas)
    for k in dists:
        for i in dists:
            for j in dists:
                if dists[i][k] + dists[k][j] < dists[i][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
    result = max ([max(dists[a].items())[1] for a in dists])
    return result

'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def maior(vizinhos):
    orla = vizinhos.copy()
    result = 0
    while orla:
        remover = []
        v = set(orla.pop(0))
        for o in orla:
            s = set(o)
            if len(v & s) > 0:
                v = v | s
                remover.append(o)
        if len(v) > result:
            result = len(v)
        for i in remover:
            orla.remove(i)
    return result


'''
O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.
'''

def erdos(artigos,n):
    numErd = {'Paul Erdos':0}
    erds = ['Paul Erdos']
    for e in erds:
        for a in artigos:
            if e in artigos[a]:
                for autor in artigos[a]:
                    if autor not in numErd:
                        numErd[autor] = numErd[e] + 1
                        erds.append(autor)
                    elif autor != e:
                        numErd[autor] = min(numErd[autor], numErd[e]+1)
    result = sorted([(e,numErd[e]) for e in numErd if numErd[e] <=n])
    result.sort(key=lambda x: x[1])
    result = [e[0] for e in result]
    return result