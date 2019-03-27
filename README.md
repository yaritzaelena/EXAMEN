# EXAMEN
## Pregunta 1 examen 

def combinaciones (hp, dell):
        if (type (hp) == list and type (dell) == list and len (hp)>0
        and len (dell)>0):
                return combinaciones_aux (hp, dell)
        else: return 'Error'
def combinaciones_aux (hp, dell):
        if hp == []:
                return []
        else: return comb_aux (hp [0], dell)+ combinaciones_aux (hp[1:], dell)

def comb_aux (valor, dell):
        if dell == []:
                return []
        else: return [valor + dell [0]] + comb_aux (valor, dell [1:])


## Pregunta 1 con recursion de cola
        
def combinaciones1 (hp, dell):
        if (type (hp) == list and type (dell) == list and len (hp)>0
        and len (dell)>0):
                return combinaciones_aux (hp, dell, [])
        else: return 'Error'

def combinaciones_aux1 (hp, dell, resultadoo):
        if hp == []:
                return []
        else: return combinaciones_aux1 (hp[1:], dell, resultadoo + comb_aux1 (hp [0], dell, []))

def comb_aux1 (valor, dell, resultadoo):
        if dell == []:
                return []
        else: return [valor + dell [0]] + comb_aux1 (valor, dell [1:], resultadoo+[valor + dell [0]])
print (combinaciones1 (hp,dell))

 ## problema 2

import math
def std (lista, avg):
        if type (lista) == list and type (avg) == float:
                return math.sqrt (std_aux (lista, avg)/ (len (lista)-1))
        else: return 'Error'

def std_aux (lista, avg):
        if lista == []:
                return 0
        else: return ((lista [0]-avg)**2)+ std_aux (lista[1:], avg)
## problema 2 colaa

import math
def std (lista, avg):
        if type (lista) == list and type (avg) == float:
                return math.sqrt (std_aux (lista, avg,0)/ (len (lista)-1))
        else: return 'Error'

def std_aux (lista, avg, resultado):
        if lista == []:
                return 0
        else: return std_aux (lista[1:], avg, resultado+ (lista [0]-avg)**2)



## Problema 3


def zscore (lista, avg, s):
        if type (lista) == list and type (avg)== float and type (s) == float:
                return zscore_aux (lista, avg,s)
        else: return 'Error'

def zscore (lista, avg, s):
        if lista == []:
                return []
        else: return ([lista [0]- avg/s]+ zscore_aux (lista [1:], avg, s))
        
## problema 3 colaa              
def zscore1 (lista, avg, s):
        if type (lista) == list and type (avg)== float and type (s) == float:
                return zscore_aux (lista, avg,s, [])
        else: return 'Error'

def zscore_aux (lista, avg, s, resultado):
        if lista == []:
                return []
        else: return zscore_aux (lista [1:], avg, s, resultado + [lista [0]- avg/s])

## problema 4
            
def rscore (sx, sy):
        if type (sx) == list and type (sy)== list and len (sx) == len (sy):
                return rscore_aux (sx, sy)/ (len (sx)-1)
        else: return 'Error'

def rscore_aux (sx, sy):
        if sx == []:
                return 0
        else: return (sx [0]*sy [0])+rscore_aux (sx [1:],sy [1:])
## problema 4 colaa 

def rscore (sx, sy):
        if type (sx) == list and type (sy)== list and len (sx) == len (sy):
                return rscore_aux (sx, sy, 0)/ (len (sx)-1)
        else: return 'Error'

def rscore_aux (sx, sy, resultado):
        if sx == []:
                return resultado
        else: return rscore_aux (sx [1:],sy [1:], resultado+sx [0]*sy [0])
