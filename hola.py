##Resolucion quiz 4
class Buscar (object):
        def __init__ (self):
                pass
        def busqueda (self, num, lista):
                if type (num)== int and type (lista)== list:
                        return self.busqueda_aux (num,lista,0)
                else:return 'Error'
        def busqueda_aux (self, num, lista, indice):
                if lista == []:
                        return -1
                elif lista [0] == num:
                        return indice
                else: return self.busqueda_aux (num, lista [1:], indice +1)

## Buscar un numero denotro de una lista y dar como resultado una lista con los indices.
                
class Buscarnum (object):
        def __init__ (self):
                pass
        def busquedas (self, numero, lista1):
                if type (numero) == int and type (lista1)== list:
                        return self.busquedas_aux (numero, lista1, [], 0)
                else: return 'Error'
        def busquedas_aux (self, numero, lista1, resultado, indice):
                if len(lista1) == indice:
                        return resultado
                if lista1 [indice] == numero:
                        return self.busquedas_aux (numero, lista1, resultado + [indice], indice+1)
                if lista1 [indice] != indice:
                        return self.busquedas_aux (numero, lista1, resultado, indice+1)

#Busqueda binaria# Buscar un numero en una lista utilizando el algoritmo binario

class Binaria (object):
        def __init__(self)::
                pass
        def busquedabin (self, numerito, lista2):
                if type (numerito) == int and type (lista2) == list:
                        return self.busquedabin_aux (self, numerito, 0, lista2, [], len (lista2)//2)
                else:return 'Error'

        def busquedabin_aux (self, resultado,  ):
                if 
