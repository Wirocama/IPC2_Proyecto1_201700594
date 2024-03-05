from xml.dom import minidom
from colorama import Fore

from Piso import Piso
from ListaPisos import ListaPisos
from Patrones import Patrones
from ListaPatrones import ListaPatrones
from Color import Color



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
                patron = item.attributes["codigo"].value 
                nuevoPatron = Patrones(str(contadorPatrones),patron) 
                nuevoPiso.patrones.agregarPatron(nuevoPatron)

                #AGREGAR COLORES 
                colores = item.firstChild.data.strip()

                #CONTADORES FILAS Y COLUMNAS
                contadorFilas = 1
                contadorColumnas = 1

                for color in colores:
                    if contadorColumnas < int(columnas):
                        nuevoColor = Color(color, str(contadorFilas), str(contadorColumnas))
                        nuevoPatron.colores.agregarColor(nuevoColor)
                        contadorColumnas +=1
                    elif contadorColumnas == int(columnas):
                         nuevoColor = Color(color, str(contadorFilas), str(contadorColumnas))
                         nuevoPatron.colores.agregarColor(nuevoColor)
                         contadorFilas +=1
                         contadorColumnas = 1

                contadorPatrones +=1

            contadorPisos +=1
            contadorPatrones =1

    def graficar(self):
        listadoPisos = self.mostrarPisos()

        if listadoPisos is None:
            print("NO EXISTE EL PISO")
        else:
            listadoPatron = self.mostrarPatrones(listadoPisos)
            if listadoPatron is None:
                print("NO EXISTE EL PRATRON")
            else:
                listadoPatron.colores.graficarPatron(listadoPisos.nombre)
            

    def mostrarPisos(self):

        print("")
        print(Fore.YELLOW + "-------------------------------------------------------------")
        print(Fore.YELLOW + "                        Listado de Pisos                     ")
        print(Fore.YELLOW + "-------------------------------------------------------------")

        lista_pisos.recorrerPisos()
        seleccion = input ("SELECCIONES UN PISO: ")
        pisoBuscado = lista_pisos.buscarPisos(seleccion)
        return pisoBuscado
    
    def mostrarPatrones(self, piso):

        print("")
        print(Fore.YELLOW + "-------------------------------------------------------------")
        print(Fore.YELLOW + "                        Listado Patrones                     ")
        print(Fore.YELLOW + "-------------------------------------------------------------")

        piso.patrones.recorrerPatrones()
        seleccion = input ("SELECCIONES UN PATRON: ")
        patronBuscado = piso.patrones.buscarPatron(seleccion)
        return patronBuscado
    
        





        










        
        
