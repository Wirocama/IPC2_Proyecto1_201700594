from Patrones import Patrones 


class ListaPatrones:

    def __init__(self):
       self.raiz=Patrones()
       self.ultimo=self.raiz

    def agregarPatron(self, nuevoPatron):
        if self.raiz.codigo is None:
            self.raiz = nuevoPatron
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoPatron
            nuevoPatron.anterior = self.raiz
            self.ultimo = nuevoPatron
        else:
            self.ultimo.siguiente = nuevoPatron
            nuevoPatron.anterior = self.ultimo
            self.ultimo = nuevoPatron
