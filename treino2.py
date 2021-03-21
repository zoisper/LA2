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
        if x-1>=0 and (x-1,y) not in visitados and mapa[y][x-1] == '.':
            orla.append((x-1,y))
        if x+1<len(mapa) and (x+1,y) not in visitados and mapa[y][x+1] == '.':
            orla.append((x+1,y))
        if y-1>=0 and (x,y-1) not in visitados and mapa[y-1][x] == '.':
            orla.append((x,y-1))
        if y+1<len(mapa) and (x,y+1) not in visitados and mapa[y+1][x] == '.':
            orla.append((x,y+1))
    return len(visitados)


    #ou

    def area(p,mapa):
    deslocamentos = [(-1,0), (1,0), (0,-1),(0,1)]
    visitados = {p}
    orla = [p]

    while orla:
        x,y = orla.pop(0)
        for dx,dy in deslocamentos:
            candidato = (x+dx,y+dy)
            if candidato[0] >=0 and candidato[0]<len(mapa) and candidato[1] >=0 and candidato[1]<len(mapa) and mapa[candidato[1]][candidato[0]] == '.' and candidato not in visitados:
                orla.append(candidato)
                visitados.add(candidato) 


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
    deslocamentos = [(-1,-2), (-1,2), (1,-2), (1,2), (-2,-1), (-2,1), (2,-1),(2,1)]
    orla = [o]
    dist = {o:0}
    result = -1
    while result == -1:
        k = orla.pop(0)
        numSaltos = dist[k]
        for delta in deslocamentos:
            candidato = (delta[0]+k[0],delta[1]+k[1])
            if candidato == d:
                result = numSaltos + 1
                break
            elif candidato not in dist:
                dist[candidato] = numSaltos +1
                orla.append(candidato)
        
    return result


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

    return grafo
 
def tamanho(ruas):
    dists = build(ruas)
    for k in dists:
        for i in dists:
            for j in dists:
                if k not in dists[i] or j not in dists[k]:
                    dists[i][j] = float("inf")
                    dists[j][i] = float("inf")
                elif j not in dists[i]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    dists[j][i] = dists[i][k] + dists[k][j]
                elif dists[i][k] + dists[k][j] < dists[i][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]
                    dists[j][i] = dists[i][k] + dists[k][j]
    result = max ([max(dists[a].items(), key=lambda k: k[1])[1] for a in dists])
    return result



'''
O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.
'''

def absorve(fronteiras,paises):
    for fronteira in fronteiras:
        if len(fronteira & paises)>0:
            paises = paises | fronteira
    return paises

def insere(continentes, fronteira):
    encontrado = 0
    for continente in continentes:
        if len(fronteira & continente)>0:
            fronteira = fronteira | continente
            continentes.remove(continente)
            continentes.append(fronteira)
            encontrado = 1
            break
    if encontrado == 0:
            continentes.append(fronteira)
    return continentes


def maior(vizinhos):
    result = 0
    fronteiras = [set(v) for v in vizinhos]
    continentes = []
    for paises in fronteiras:
        paises = absorve(fronteiras,paises)
        continentes = insere(continentes,paises)
    if continentes:
        result = len(max(continentes, key=lambda x: len(x)))
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
    orla = ["Paul Erdos"]
    numErdos = {"Paul Erdos":0}
    while orla:
        o = orla.pop(0)
        for a in artigos:
            if o in artigos[a]:
                for autor in artigos[a]:
                    if autor not in numErdos:
                        numErdos[autor] = numErdos[o] +1
                        orla.append(autor)
    result = sorted(a for a in numErdos.items() if a[1]<=n)
    result.sort(key=lambda x: x[1])
    result = [a[0] for a in result]
    return result


'''
Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.
'''

def caminho(mapa):
    fim = (len(mapa)-1,len(mapa)-1)
    if fim == (0,0):
        return ""
    deslocamentos = [(-1,0),(0,-1),(1,0),(0,1)]
    orla = [(0,0)]
    caminho = {(0,0):""}
    result = -1
    while orla:
        x,y = orla.pop(0)
        for dx, dy in deslocamentos:
            candidato = (x+dx,y+dy)
            if candidato[0] >=0 and candidato[0] < len(mapa) and candidato[1] >=0 and candidato[1] < len(mapa) and mapa[candidato[1]][candidato[0]] == ' ' and candidato not in caminho:
                orla.append(candidato)
                if dx == -1:
                    caminho[candidato] = caminho[(x,y)] + 'O'
                elif dx == 1:
                    caminho[candidato] = caminho[(x,y)] + 'E'
                elif dy == -1:
                    caminho[candidato] = caminho[(x,y)] + 'N'
                elif dy == 1:
                    caminho[candidato] = caminho[(x,y)] + 'S'
                if candidato == fim:
                    result = caminho[candidato]
                    break
    return result


'''
Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''

def bfs(mapa, origem):
    largura = len(mapa[0])
    cumprimento = len(mapa)
    if origem[1] == cumprimento-1:
        return 0
    orla = [origem]
    dists = {origem:0}
    deslocamentos = [(-1,0),(1,0),(0,-1),(0,1)]
    while orla:
        x,y = min(orla,key=lambda k: dists[k])
        orla.remove((x,y))
        for dx,dy in deslocamentos:
            candidato = (x+dx,y+dy)
            if candidato[0]>=0 and candidato[0]<largura and candidato[1]>=0 and candidato[1]<cumprimento:
                peso = abs(int(mapa[candidato[1]][candidato[0]]) - int(mapa[y][x]))
                if peso <=2 and candidato not in dists:
                    orla.append(candidato)
                    dists[candidato] = dists[(x,y)] + peso +1
                elif peso <=2 and dists[candidato] >=  dists[(x,y)] + peso +1 :
                    dists[candidato] = dists[(x,y)] + peso +1
    result = [dists[a] for a in dists if a[1] == cumprimento-1]
    if result:
        return min(result)
    return float("inf")


def travessia(mapa):
    result = []
    for origem in range(len(mapa[0])):
        result.append((origem,bfs(mapa,(origem,0))))
    result.sort()
    result.sort(key=lambda x: x[1])
    return result[0]


'''
Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.
'''

def build(rotas):
    grafo = {}
    for rota in rotas:
        for cidade in range(0,len(rota)-2,2):
            partida = rota[cidade]
            destino = rota[cidade+2]
            distancia = rota[cidade+1]
            if partida not in grafo:
                grafo[partida] = {}
            if destino not in grafo:
                grafo[destino] = {}
            grafo[partida][destino] = distancia 
            grafo[destino][partida] = distancia
    return grafo


def viagem(rotas,o,d):
    grafo = build(rotas)
    result = float("inf")
    orla = [o]
    dists = {o:0}
    while orla:
        partida = min(orla, key=lambda x: dists[x])
        orla.remove(partida)
        if partida == d:
            result = dists[partida]
            break
        for destino in grafo[partida]:
            if destino not in dists:
                dists[destino] = dists[partida] + grafo[partida][destino]
                orla.append(destino)
            elif dists[destino] > dists[partida] + grafo[partida][destino]:
                dists[destino] = dists[partida] + grafo[partida][destino]
    return result
