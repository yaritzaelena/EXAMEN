class Pila:
    def __init__(self):
        self. __pi = []
    def len (self):
        return len(self.__pi)
    def is_empty(self):
        return len(self.__pi) == 0
    def push (self, e) :
        return self.__pi.append(e)
    def pop(self):
        if self.is_empty():
            raise MiGatito('Stack is empty')
        else:
            return self.__pi.pop()
    def top (self):

        if self.is_empty():
            raise MiGatito ('Stack is empty')
        else:return self. __pi[-1]
    def test(self):
        try:
            self.stack = Pila()
            self.stack.push (5)
            self.stack.push (8)
            print ('Numero de elementos de la pila: ', self.stack.len())
            print ('Elemento en la parte superior de la pila: ', self.stack.top())
            print ('Saca el elemento: ', self.stack.pop())
            print ('saca el elemento: ', self.stack.pop())
            x = 5
            y = 0
            c = x/y
        except MiGatito as e:
            print ('Ocurrio un error al sacar un elemento de una pila vacia', str (type(e)), e.message())
        except ZeroDivisionError as d:
            print ('Ocurrio un error al dividir')
        else:
            print('Resultado')
        finally:
            print('Finally')

    


        
class MiGatito(Exception):
    def __init__(self, message):
        self.message = message
class DivisionCero(ZeroDivisionError):
    def __init__(self, message):
        self.message = message 
