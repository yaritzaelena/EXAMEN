#Pregunta 1 
class Matriz (object):
    def __init__(self):
        pass
    def matriz (self, numero):
        if type (numero) == int :
            return self.matriz_aux (numero, [],0,0,0, [])
        else: return 'Error'
    def matriz_aux(numero, indice, fila, columna, resultado):
        if fila == numero-1 and columna == numero-1 :
            return resultado 
        if c<= numero 
        return self.matriz_aux (numero, indice+columna, fila+1, columna+1 )
            if fila>0 and fila< numero:
                return self.matriz_aux (numero, indice+1)

#Pregunta 2 
class Permutaciones (object):
    def __init__(self):
        pass
    def permutacion(self, n, x):
        if (n>x) or (n=x):
            return self.permutacion_aux (n,x,0,1,n-x)
        else: return 'Error'
    def permutacion_aux(n,x,resultado1, resultado2, indice, resta):
        if indice == numero:
            resultado1/resultado2
        if indice< numero:
            return self.permutacion_aux(n,x,resultado1(n-indice), resultado2, indice+1, resta)
        if indice < resta:
            return self.permutacion_aux(n,x,resultado1, resultado2(resta-indice), indice+1, resta)
        
#Pregunta 3 
class Magia (object):
    def __init__ (self):
        pass
    def es_magico(self, matriz):
        if type (matriz)==lista:
            return self.sumafila(matriz, 0,0,0)
        else:return 'Error' 

    def sumafila(matriz, fila, columna, resultado):
        if fila == len(matriz) and columna == len (matriz[0]):
            return suma1 and self.diagonal (matriz, 0, 0, 0)
        elif columna == len (matriz [0]):
            return self.sumafila (matriz, fila+1, 0, suma1+ matriz [f],[c])
        else: return self.sumafila(matriz, fila, columna+1, suma+matriz [f][c])

    def diagonal(self, matriz, fila, columna, suma2):
        if fila == len(matriz) and columna == len(matriz[0]):
            return suma2 and self.antidiag(matriz, len(matriz[0]), -1, 0)
        else: return self.diagonal(matriz, fila+1, columna+1, suma2= matriz[fila][columna])
    
    def antidiag (self, matriz, fila, columna, suma3):
        if fila == len (matriz) and columna== (-(len(matriz[0]))):
            return suma3 and self.sumacolumna(matriz,0,0,0,-1)
        else: return self.antidiag(matriz, fila-1, columna-1, suma3+ matriz[fila][columna])

    def sumacolumna(self, matriz, fila, columna, suma4, indice):
        if fila == len(matriz) and columna == (len(matriz[0])):
            return suma4 and self.verificacion (suma1,suma2,suma3,suma4)
        elif fila> indice:
            return self.sumacolumna(matriz, fila+1, 0, sumaz+matriz[fila][columna], indice+1)
        else:return self.sumacolumna(matriz, 0, columna+1, suma4+matriz[fila][columna], -1)
        
    def verificacion(self, suma1, suma2, suma3, suma4):
        if suma1 == suma2 and suma1 == suma3 and suma1 == suma4:
            return True 
        else: return False 

    #Pregunta 4 

    class Grafico (object):
        def __init__ (self):
            pass 
        def grafico (self, lista):
            if type(lista)==list:
                return grafico_aux (lista,[], 0)
        def grafico_aux (lista, resultado, indice):
            if indice == lista[0]:
                return resultado
            else: return 
                grafico_aux (lista, resultado+[*]xlista[indice], indice+1)











