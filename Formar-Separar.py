from Gato import Pila
class Pruebas():
    def __init__(self):
        self.pila = Pila()
    def Numero(self, numero):
        while numero > 0:
            self.pila.push(numero%10)
            numero = numero //10

    def formar(self):
      #self solo si es global
        res = 0
        cont = 0
        while self.pila.is_empty() == False:
            res += self.pila.pop()*10**cont
            cont += 1
        return res
    def ejecutar (self, numero):
        self.Numero(numero)
        return self.formar()
