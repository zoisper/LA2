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