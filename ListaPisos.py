from Piso import Piso

class ListaPisos:

    def __init__(self):
       self.raiz=Piso()
       self.ultimo=self.raiz

    def agregarPiso(self, nuevoPiso):
        if self.raiz.codigo is None:
            self.raiz = nuevoPiso
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoPiso
            nuevoPiso.anterior = self.raiz
            self.ultimo = nuevoPiso
        else:
            self.ultimo.siguiente = nuevoPiso
            nuevoPiso.anterior = self.ultimo
            self.ultimo = nuevoPiso

        