# Suma de lista anidada utilizando indices

class Suma(object):
        def __init__ (self):
                pass
        def suma(self, lista1):
                if type (lista1) == list:
                   return self.suma_aux (lista1,0, 0)
                else: return 'Error'
        def suma_aux (self, lista1, resultado, indice):
                if indice == len(lista1):
                        return resultado
                elif type (lista1[indice]) == list:
                        return (self.suma_aux(lista1[indice],0,0) +
                                self.suma_aux(lista1,resultado,indice+1))
                else:return self.suma_aux(lista1,resultado + lista1[indice],indice+1)
               
#Hacer una funcion que reciba una lista y obtenga
#el numero mayor. Utilice indices

class lista(object):
        def __init__ (self):
                pass
        def mayor(self, lista):
                if type (lista) == list:
                        return self.mayor_aux(lista, 0, 0)
                else: return 'Error'
        def mayor_aux (lista, resultado, indice):
                if indice == len (lista):
                        return resultado
                elif lista [indice]> resultado:
                        return  mayor_aux (lista, lista[indice], indice+1)
                else: return  mayor_aux (lista, resultado, indice+1)
                
