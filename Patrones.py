from ListaColores import ListaColores

class Patrones:

    def __init__(self, codigo = None, patron = None):
        self.codigo = codigo
        self.patron = patron
        self.colores = ListaColores()
        self.siguiente = None
        self.anterior = None