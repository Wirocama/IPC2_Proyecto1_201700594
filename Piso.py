from ListaPatrones import ListaPatrones

class Piso:

    def __init__(self, codigo = None, nombre = None, filas = None, columnas = None, voltear = None, intercambiar = None):
        self.codigo = codigo
        self.nombre = nombre 
        self.filas = filas
        self.columnas = columnas
        self.voltear = voltear
        self.intercambiar = intercambiar
        self.patrones = ListaPatrones()
        self.siguiente = None
        self.anterior = None

        



