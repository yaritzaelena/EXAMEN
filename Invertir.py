from Gato import Pila
class Pruebas:
    def __init__(self):
        pass
    def test(self):
        try:
            self.stack = Pila()
            self.stack.push (1)
            self.stack.push (2)
            self.stack.push (3)
            self.stack.push (4)
            self.stack.push (5)
            self.stack.push (6)
            while self.stack.is_empty() == False:
                print(self.stack.pop(), end= ' ')
            print()
