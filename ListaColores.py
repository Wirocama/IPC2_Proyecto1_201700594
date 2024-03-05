from Color import Color
import webbrowser
import os


class ListaColores:

    def __init__(self):
       self.raiz=Color()
       self.ultimo=self.raiz

    def agregarColor(self, nuevoColor):
        if self.raiz.color is None:
            self.raiz = nuevoColor
        elif self.raiz.siguiente is None:
            self.raiz.siguiente = nuevoColor
            nuevoColor.anterior = self.raiz
            self.ultimo = nuevoColor
        else:
            self.ultimo.siguiente = nuevoColor
            nuevoColor.anterior = self.ultimo
            self.ultimo = nuevoColor

    def graficarPatron(self,titulo):
        nodoAux = self.raiz

        #CREACION DE ARCHIVO DE GRAFICA
        cadena = 'digraph { '
        cadena +='label ='
        cadena += titulo 
        cadena += ';'
        cadena += 'abcd [shape=none, margin=0, label=<'
        cadena += '<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0" CELLPADDING="20" COLOR="red">'
        cadena += '<TR>'

        filaAux = nodoAux.fila
        while True:
            if nodoAux.siguiente is not None:
                if nodoAux.fila == filaAux:
                    if nodoAux.color == "B":
                        cadena += '<TD BGCOLOR="black"></TD>'
                    elif nodoAux.color == "W":
                        cadena += '<TD BGCOLOR="white"></TD>'
                    nodoAux = nodoAux.siguiente
                else:
                    filaAux = nodoAux.fila
                    cadena += '</TR>'
                    cadena += '<TR>'
                    if nodoAux.color == "B":
                        cadena += '<TD BGCOLOR="black"></TD>'
                    elif nodoAux.color == "W":
                        cadena += '<TD BGCOLOR="white"></TD>'
                    nodoAux = nodoAux.siguiente
            else:
                if nodoAux.color == "B":
                    cadena += '<TD BGCOLOR="black"></TD>'
                elif nodoAux.color == "W":
                    cadena += '<TD BGCOLOR="white"></TD>'
                cadena += '</TR>'
                cadena += '</TABLE>>];'
                break
        cadena += '}'

        #CREAR ARCHIVO
    
        grafica = open("./grafica.dot", "w")
        grafica.write(cadena)
        grafica.close()

        #CONVERTIR .DOT A IMAGEN
        os.system('dot -Tjpg grafica.dot -o grafica.jpg')

        #ABRIR ARCHIVO 
        webbrowser.open("grafica.jpg", new = 2, autoraise = True)


