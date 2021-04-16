#https://codeboard.io/projects/155406

"""
Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""
#13%

def crescente(lista):
    if not lista:
        return 0   
    
    inferiores = [1 for i in lista]

    for i in range (len(lista)):
        for j in range(0,i):
            if lista[j] <= lista[i]:
                inferiores[i] = max(inferiores[i], inferiores[j] +1)
                
    return max(inferiores)



"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""
#10%

def espaca(frase,palavras):
    result = ""
    dic = {}
    for i in range (len(frase)+1):
        for j in range(0,i):
            if frase[j:i] in palavras and i not in dic:
                if j in dic:
                    dic[i] = dic[j] + " " + frase[j:i]
                else:
                    dic[i] = frase[j:i]
                
    if dic:
        result = dic[len(frase)]
    return result


"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""
#10%

def aux(capacidade, objectos):
    if capacidade == 0 or not objectos:
        return 0
    elif objectos[0][2] >capacidade:
        return aux(capacidade, objectos[1:])
    else: 
        r1 =  objectos[0][1] + aux(capacidade-objectos[0][2], objectos[1:])
        r2 =  aux(capacidade, objectos[1:])
        return max(r1,r2)
    
def ladrao(capacidade,objectos):
    objectos.sort(key=lambda x: x[1], reverse=True)
    return aux(capacidade, objectos)


"""

Implemente uma função que determina qual a probabilidade de um robot regressar 
ao ponto de partido num determinado número de passos. Sempre que o robot dá um 
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'), 
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o 
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.

"""
#11%

def aux(passos, probs, pos, dic):
    if passos == 0:
        return pos == (0,0)
    
    if (passos-1,(pos[0],pos[1]+1)) not in dic:
        dic[(passos-1,(pos[0],pos[1]+1))] = aux(passos-1, probs, (pos[0],pos[1]+1), dic)
    u = probs['U']*dic[(passos-1,(pos[0],pos[1]+1))]
    
    if (passos-1,(pos[0],pos[1]-1)) not in dic:
        dic[(passos-1,(pos[0],pos[1]-1))] = aux(passos-1, probs, (pos[0],pos[1]-1), dic)
    d = probs['D']*dic[(passos-1,(pos[0],pos[1]-1))]
    
    if (passos-1,(pos[0]+1,pos[1])) not in dic:
        dic[(passos-1,(pos[0]+1,pos[1]))] = aux(passos-1, probs, (pos[0]+1,pos[1]), dic)
    r = probs['R']*dic[(passos-1,(pos[0]+1,pos[1]))]
    
    if (passos-1,(pos[0]-1,pos[1])) not in dic:
        dic[(passos-1,(pos[0]-1,pos[1]))] = aux(passos-1, probs, (pos[0]-1,pos[1]), dic)
    l = probs['L']*dic[(passos-1,(pos[0]-1,pos[1]))]

    
    return u+d+r+l
    
    

def probabilidade(passos,probs):
    return round(aux(passos, probs, (0,0), {}),2)


"""

Um fugitivo pretende atravessar um campo  no mínimo tempo possível (desde o 
canto superior esquerdo até ao canto inferior direito). Para tal só se poderá 
deslocar para a direita ou para baixo. No entanto, enquanto atravessa o campo 
pretende saquear ao máximo os bens deixados por fugitivos anteriores. Neste 
problema pretende-se que implemente uma função para determinar qual o máximo 
valor que o fugitivo consegue saquear enquanto atravessa o campo. 
A função recebe o mapa rectangular defindo com uma lista de strings. Nestas
strings o caracter '.' representa um espaço vazio, o caracter '#' representa 
um muro que não pode ser atravessado, e os digitos sinalizam posições onde há 
bens abandonados, sendo o valor dos mesmos igual ao digito.
Deverá devolver o valor máximo que o fugitivo consegue saquear enquanto 
atravessa o campo deslocando-se apenas para a direita e para baixo. Assuma que 
é sempre possível atravessar o campo dessa forma.

"""
#10%

def aux(mapa, pos, fim, dic):
    if pos == fim:
        if (mapa[fim[1]][fim[0]]) != '.':
            return int (mapa[fim[1]][fim[0]])
        else:
            return 0
    if pos not in dic:
        r = 0
        d = 0
        if mapa[pos[1]][pos[0]] != '.':
            r = int (mapa[pos[1]][pos[0]])
            d = int (mapa[pos[1]][pos[0]])
            
        if pos[0]+1 <= fim[0] and mapa[pos[1]][pos[0]+1] != '#':
            r += aux(mapa, (pos[0]+1, pos[1]), fim, dic)
        
        if pos[1]+1 <= fim[1] and mapa[pos[1]+1][pos[0]] != '#':
            d += aux(mapa, (pos[0], pos[1]+1), fim, dic)
        dic[pos] = max(r,d)
    
    return dic[pos]


def saque(mapa):
    pos = (0,0)
    fim = (len(mapa[0])-1, len(mapa)-1)
    return aux(mapa, pos, fim, {})

"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""
#13%

def maxPrefix(lista):
    r = [float("-inf"),0]
    aux = [0,0]
    for i in range(len(lista)):
        aux[0] +=lista[i]
        aux[1] =i
        if aux[0] > r[0]:
            r[0] = aux[0]
            r[1] = aux[1]
    return r

def maxsoma(lista):
    soma, size = maxPrefix(lista)
    aux = soma
    for i in range(size):
        aux -= lista[i]
        soma = max(soma, aux)
    
    return soma


"""

Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.

"""
#10%

def aux(soma, lista, size):
    if soma == 0 :
        return True
    if size == 0 or soma <0:
        return False
    else:
        return aux(soma - lista[0], lista[1:],size-1) or aux(soma, lista[1:],size-1) 
    

def validas(soma,listas):
    result = []
    for lista in listas:
        size = len(lista)
        if aux(soma,lista,size):
            result.append(lista)
    return result

"""

Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""
#13%

def vendedor(capacidade,produtos):
    d ={}
    d[0] = 0
    saco = {}
    for cap in range(1, capacidade+1):
        r = 0
        for p in produtos:
            if p[2] <= cap:
                a = p[1] + d[cap - p[2]]
                if a > r:
                    r = a
                    saco[cap] = p
        d[cap] = r
    
    
    valor = d[capacidade]
    lista = []
    
    while capacidade:
        if capacidade in saco:
            lista.append(saco[capacidade][0])
            capacidade -= saco[capacidade][2]
        else:
            break
    lista.sort()
    
    return (valor,lista)