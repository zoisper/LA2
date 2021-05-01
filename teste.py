def aux(texto, flag, dic, size):
    if not texto:
        return ""
    if (len(texto),flag) in dic:
        return dic[(len(texto),flag)]
    
    elif flag == True:
        dic[(len(texto), True)] = texto[0] +  " "* (len(texto[1:])>0) +  aux(texto[1:], False, dic, len(texto[1:]))
        return dic[(len(texto), True)]
    else:
        list = []
        r1 = texto[0] + " "* (len(texto[1:])>0) + aux(texto[1:], False, dic, len(texto[1:]))
        r2 =  texto[0] + " " + texto[0] + " "* (len(texto[1:])>0) + aux(texto[1:], True, dic, len(texto[1:]))
        list.append(r1)
        list.append(r2)
        list.sort()
        list.sort(key=len, reverse=True)
        r = list[0]
        dic[(len(texto),False)] = r
        return  dic[(len(texto), False)]
    
    

def duplica(texto):
    temp = texto.split(' ')
    
    return aux(temp, False, {}, 0)


def duplica(texto):
temp = texto.split(' ')
lista = [[len(x), x,1] for x in temp]
lista[0][2] = 2
anterior = lista.copy()
for i in range (1,len(lista)):
    if lista[i-1][2] == 1:
        lista[i][2] =2
    elif lista[i][0] > lista[i-1][0]:
        lista[i][2] = 2
        lista[i-1][2] = 1




result = ""
for t,p,q in lista:
    result += " " + p
    if q >1:
        result += " " + p


if result[0] == " ":
    result = result[1:]
    
return result