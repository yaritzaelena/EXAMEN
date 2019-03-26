## Primer problema.

def combinaciones (hp, dell):
    if type(hp)== list and type (dell)== list:
        return purchase (hp, dell)

def purchase (hp, dell):
    if hp == []:
        return []
    if dell == []:
        return [hp[1:]+ dell[0]]+ purchase (hp [0], dell [1:])
    else return [hp[0]+dell[0]]+ purchase_aux (hp[0],dell[1:])

## Segundo ejercicio

math import sqrt
def std (lista, avg):
    if type (lista)== list:
        return std_aux (lista, avg)
    else return 'Error'

def std_aux (lista, avg):
    if lista == []:
        return sqrt (std (lista, avg)/ (len(lista)-1))
    if lista [0] >=0:
        return (lista [0]-avg)**2 + std_aux (lista [1:], avg)

## Tercer ejercicio

    def zscore (listax):
        if type (listax)== list:
            return zscore_aux (listax,s,avg)
        else: return 'Error'

    def zscore_aux (listax,s,avg):
        if lista == []:
            return 0
        elif lista [0]>=0:
            return (lista [0]- avg)/s + zscore_aux (lista [1:],s,avage)

## Cuarto ejercicio

    def rscore (zx, zy):
        if type (zx)== list and type (zy)== list and len (zx)== len (zy):
            return rscore_aux (zx, zy)
        else: return 'Error'

    def rscore_aux (zx, zy):
        if zx == []:
            return rscore ((zx, zy)/(len (zx)-1))
        if zx > 0 or zx < 0:
            return zx [0] * zy [0] + rscore_aux (zx [1:], zy [1:])


        
