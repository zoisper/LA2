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
#9%

def aux(lista,p):
    if len(lista) == 0:
        return 0
    elif lista[0]>=p:
        return 1 + aux(lista[1:],lista[0])
    else:
        return aux(lista[1:], p)

def crescente(lista):
    r = 0
    for i in range (1,len(lista)+1):
        r = max(r, aux(lista[-i:], lista[-i]))
    return r

"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""
#9%

def aux(texto, palavra):
    for i in range (1,len(palavra)+1):
        if i > len(texto) or (texto[-i] != palavra[-i]):
            return False
    return True

def espaca(frase,palavras):
    result = ""
    palavras.sort(key=len, reverse=True)
    while frase:
        for pal in palavras:
            if(aux(frase,pal)):
                result = pal + result
                frase = frase[:len(frase) -len(pal)]
                break
        if len(frase) >0:
            result = " " + result 
    return result


