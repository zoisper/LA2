

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
    escolhidos = []
    for i in alunos:
        for j in prefs[i]:
            if j not in escolhidos:
                escolhidos.append(j)
                del prefs[i]
                break
    return sorted(prefs)


'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''

def apelidos(nomes):
    nomes.sort()
    nomes.sort(key=lambda x : len(x.split()))
    return nomes



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
dic = {}
for i in ruas:
    if i[0] not in dic:
        dic[i[0]] = 1
    else:
        dic[i[0]] += 1
    if i[-1] not in dic:
        dic[i[-1]] = 1
    elif i[0] != i[-1]:
        dic[i[-1]] +=1
result = sorted(dic.items())
result.sort(key=lambda x : x[1])
return result

'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def primo(n):
	if n <= 1:
		return False
	for i in range(2, n):
		if n%i == 0:
			return False
	return True

def factoriza(n):
	r = 0
	for i in range (2, n):
		if primo(i) and n%i == 0:
			r += i
			while n%i == 0:
				n /= i
	return r

"""
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
"""
def frequencia(texto):
	dic ={}
	lista = texto.split()
	for i in lista:
		if i not in dic:
			dic[i] = 1
		else:
			dic[i] +=1
	lista = sorted(dic.items())
	lista.sort(key=lambda t : t[1], reverse=True)
	lista = [l[0] for l in lista]
	return lista


# outra versao

from collections import Counter

def frequencia2(texto):
	lista = texto.split()
	lista.sort(key=Counter(lista).get, reverse=True)
	lista = list(dict.fromkeys(lista))
	return lista


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
	equipas = dict((e,[0,0]) for (e,g,e,g) in jogos)
	for i in jogos:
		if i[1] > i[3]:
			equipas[i[0]][0] +=3
		elif i[1] < i[3]:
			equipas[i[2]][0] +=3
		else:
			equipas[i[0]][0] +=1 
			equipas[i[2]][0] +=1
		equipas[i[0]][1] += i[1]
		equipas[i[2]][1] += i[3]
		equipas[i[0]][1] -= i[3]
		equipas[i[2]][1] -= i[1]
	classificacao = list(equipas.items())
	classificacao.sort()
	classificacao.sort(key=lambda e : e[1][1], reverse=True)
	classificacao.sort(key=lambda e : e[1][0], reverse=True)
	classificacao = [(e[0],e[1][0]) for e in classificacao]
	return classificacao


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
	dados = dict((e,c) for (c,e) in log)
	log = list(map(lambda tuplo : (list(tuplo[0]), tuplo[1]),log))
	troca = lambda x,y : y if x == '*' else x
	intersecta = lambda x,y : map(troca, x,y)
	for i in range (len(log)-1):
		for j in range(i+1, len(log)):
			if log[i][1] == log[j][1]:
				dados[log[i][1]] = "".join(intersecta(log[j][0], log[i][0]))
	result = sorted(dados.items())
	result.sort(key=lambda x : sum(map(lambda l: 0 if l == '*' else 1, x[1] )), reverse=True)
	result = [(b,a) for (a,b) in result]
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
	palavra = list(palavra)
	aux = palavra.copy()
	for i in range(n-1):
		if aux[0] == aux[-1]:
			palavra.pop()
		palavra.extend(aux)
	palavra = "".join(palavra)
	return palavra


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
	comandos = comandos.split('H')
	if comandos[-1] == '':
		comandos.pop()
	for i in comandos:
		aux = [0,0,0,0]
		movs = [0,0,0,0]
		p = 3
		for j in i:
			if j == 'E':
				p = (p + 1) % 4
			elif j == 'D':
				p = (p + 3) % 4
			elif p >=2:
				aux[p] += 1
				aux[(p+2)%4] +=1
				movs[p] = max(movs[p], aux[p])
			else:
				aux[p] -= 1
				aux[(p+2)%4] -=1
				movs[p] = min(movs[p], aux[p])
		result.append(tuple(movs))
	return result



prefs = {30000:[1],20000:[2],10000:[3]}

print(aloca(prefs))

