from xml.dom import minidom
from Piso import Piso
from ListaPisos import ListaPisos
from Patrones import Patrones
from ListaPatrones import ListaPatrones


lista_pisos = ListaPisos()
lista_patrones = ListaPatrones()

class Informacion:

    def obtenerInformacion(self, ruta = None):

        lectura = minidom.parse(ruta)
        contadorPisos = 1
        contadorPatrones = 1

        #LECTURA DEL ARCHIVO
        #AGREGAR PISO
        etiquetaPisos = lectura.getElementsByTagName("piso")
        for etiqueta in etiquetaPisos:
            nombrePiso = etiqueta.attributes["nombre"].value 
            if etiqueta.hasAttribute("nombre"):

                r = etiqueta.getElementsByTagName("R")[0]
                filas = r.childNodes[0].data.strip()

                c = etiqueta.getElementsByTagName("C")[0]
                columnas = c.childNodes[0].data.strip()

                f = etiqueta.getElementsByTagName("F")[0]
                voltear = f.childNodes[0].data.strip()

                s = etiqueta.getElementsByTagName("S")[0]
                intercambiar = s.childNodes[0].data.strip()

                nuevoPiso = Piso(str(contadorPisos), nombrePiso, filas, columnas, voltear, intercambiar)
                lista_pisos.agregarPiso(nuevoPiso)

                patron = etiqueta.getElementsByTagName("patron")

            for item in patron:
                codigo = item.attributes["codigo"].value 
                nuevoPatron = Patrones(str(contadorPatrones),codigo) 
                lista_patrones.agregarPatron(nuevoPatron)
                contadorPatrones +=1

        contadorPisos +=1






        
        
