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