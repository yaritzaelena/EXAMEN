#Recursion de pila
def simple_pila (num, n):
    if isinstance (num, int) and isinstance (n, int):
        return simple_pila_aux(num, n-1)

def simple_pila_aux(num, n):
    if n == 0:
        return 0
    else: return (num * n) + simple_pila_aux(num, n-1)

#Recursion de cola
def simple_cola(num, n):
    if isinstance(num, int) and isinstance(n, int):
        return simple_cola_aux(num, n-1, 0)

def simple_cola_aux(num, n, resultado):
    if n== 0:
        return resultado
    else: return simple_cola_aux(num-1, n-1, resultado + num*n)
    
def simple_iteracionWhile_aux(num, n):
    resultado = 0
    while n>0:
        resultado += (num*n)
        n -= 1
def simple_iteracionFor_aux(num, n):
    resultado = 0
    for i in range(n):
        resultado += (num *(i+1))
        print (num, * (i+1))

##Dado un numero, almacenar los digitos pares de este en una lista
##y los digitos impares en otra lista.Utilice un while

def Numero(num):
    if type (num) == int:
        return numero(num, [], [])

def numero(num, pares, impares):
    while num > 0:
        if (num % 10) % 2 == 0:
            pares += [num%10]
            num//= 10
        if (num % 10) % 2 != 0:
            impares += [num%10]
            num //= 10
    print(pares, impares)
    
##Dado un numero, forme un nuevo numero solo con los digitos pares de dicho numero.
##Utilice un While
def Par(num):
        if type (num) == int:
            return par(num,0, 0)
def par (num, indice, numerito):
    while num>0:
        if (num % 10) % 2 == 0:
            numerito += ((num%10)*(10**indice))
            indice += 1
        num//= 10
    print (numerito)
##Dado un numero forme otro par y otro impar, use While

def ParImpar(num):
        if type (num) == int:
            return parimpar(num,0, 0, 0,0)
def parimpar (num, indice1, indice2, numeritopar, numeritoimpar):
    while num>0:
        if (num % 10) % 2 == 0:
            numeritopar += ((num%10)*(10**indice1))
            indice1 += 1
        num//= 10
        
        if (num % 10) % 2 != 0:
            numeritoimpar += ((num%10)*(10**indice2))
            indice2 += 1
        num//= 10
    print (numeritopar, numeritoimpar)            

####################################################################################
    ###SUMA UTILIZANDO WHILE AND FOR###
    
def sumaWhile(lista):
    resultado = 0
    contador = 0
    largo = len(lista)
    while contador < largo:
        resultado += lista [contador]
        contador += 1
    return resultado

def sumaSlicing(lista):
    resultado = 0
    while lista != []:
        resultado += lista[0]
        lista = lista [1:]
    return resultado

def sumaFor(lista):
    resultado = 0
    for contador in range (len(lista)):
        resultado += lista[contador]
    return resultado

def sumaFor(lista):
    resultado = 0.
    for valor in lista:
        resultado += valor
        return resultado 
