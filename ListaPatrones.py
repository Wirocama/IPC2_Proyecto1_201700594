from Patrones import Patrones 
from colorama import Fore


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

    def recorrerPatrones(self):
        nodoAux = self.raiz 

        while True:
            print(Fore.LIGHTWHITE_EX + nodoAux.codigo + ". " + nodoAux.patron)
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else: 
                break

    def buscarPatron(self, codigo):
        nodoAux = self.raiz 

        while nodoAux.codigo != codigo:
            if nodoAux.siguiente is not None:
                nodoAux = nodoAux.siguiente
            else:
                return None 
        return nodoAux
