#Sume los valores de dos listas de igual tamaño usando un for e indices
# El resultado es un numero con la suma de ambas

class Sumatoria (object):
    def __init__ (self):
        pass
    def sumatoria (self, lista, lista1):
        if type (lista) == list and type(lista1) == list and len(lista) == len(lista1):
            return self.sumatoria_aux(lista, lista1, 0)
        else: return 'Error'
    def sumatoria_aux(self, lista, lista1, indice):
        resultado = 0
        resultado1 = 0 
        for indice in range (len(lista)):
            resultado += lista[indice]
            resultado1 += lista1[indice]
            indice += 1
        return (resultado + resultado1)
    
##Formar nueva lista## 

class Suma (object):
    def __init__ (self):
        pass
    def suma (self, l, l1):
        if type (l) == list and type(l1) == list and len(l) == len(l1):
            return self.suma_aux(l, l1, 0)
        else: return 'Error'
    def suma_aux(self, l, l1, i):
        result = [] 
        for i in range (len(l)):
            result += [l[i] + l1[i]]
            i += 1
        return result

#Suma de matrices#

class SumaMat (object):
    def __init__ (self):
        pass
    def sumamat (self, l, l1):
        if type (l) == list and type(l1) == list and len(l) == len(l1):
            return self.sumamat_aux(l, l1)
        else: return 'Error'
    def sumamat_aux(self, l, l1):
        r = []
        rante = []
        for f in range(len (l)):
            for c in range (len (l[0])):
                rante += [l[f][c] + l1[f][c]]
            r += [rante]
         
        return r 
#Hcaer traspuesta de una matriz
    
class Tras (object):
    def __init__ (self):
        pass
    def tras (self, l):
        if type (l) == list:
            return self.tras_aux(l)
        else: return 'Error'
        
    def tras_aux(self, l):
        r = []        
        for c in range (len (l[0])):
            rante = []
            for f in range(len (l)):
                rante += [l[f][c]]
            r += [rante]
        return r
    
#Suma de diagonal
    
class Diagonal (object):
    def __init__ (self):
        pass
    def diagonal (self, l):
        if type (l) == list:
            return self.diagonal_aux(l)
        else: return 'Error'
        
    def diagonal_aux(self, l):
        r = 0       
        for f in range (len (l[0])):
            for f in range(len (l)):
                r += l[f][f]                    
        return r
    
    def diag_aux(self, l):
        diagonal = []     
        for f in range (len (l[0])):
            for f in range(len (l)):
                diagonal += [l[f][f]]                  
        return r
    
    def antidiagonal (matriz, filas):
        anti_diagonal = []
        for fila in range (filas):
            anti_diagonal += [matriz[fila][-(fila+1)]]
        return anti_diagonal

#Dibuejar * en el borde de la matriz

class Dibujar(object):
    def __init__(self):
        pass
    def dibujar (self, lista):
        if type (lista)== list:
            return self.dibujar_aux(lista)
        else: return 'Error'
    def dibujar_aux(self, lista):
        for fila in range (len(lista)):                
            for columna in range (len(lista)):
                if fila == 0 or fila == (len(lista)-1):
                    print('*', end= ' ')
                if columna == 0 or columna == (len(lista[0])-1):
                    print('*', end= ' ')
                else: print(' ', end= ' ')
                    
            print('')

class Triangulo(object):
    def __init__(self):
        pass
    def triangulo(self, base):
        if type (base) == int:
            return self.triangulo_aux(base)
        else: return 'Error'
    def triangulo_aux(self, base):
        mitad = (base*2)-1
        
        derecha = (mitad // 2)
        izquierda = (mitad // 2)
        for fila in range (0, mitad, 2):
            for columna in range (mitad)
                if fila == 0 and columna == derecha:
