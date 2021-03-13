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
    return dists


def fw(adj):
    dist = {}
    
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[d][o]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d] 

    return dist

def fixRuas(ruas):
    adj = {}
    
    for rua in ruas:
        a = rua[0]
        b = rua[-1]
        n = len(rua)
        if a not in adj:
            adj[a] = {}
        if b not in adj:
            adj[b] = {}
        if b not in adj[a]:
            adj[a][b] = float("inf")
        if a not in adj[b]:
            adj[b][a] = float("inf")
        adj[a][b] = min(n, adj[a][b])
        adj[b][a] = min(n, adj[b][a])
    return adj
