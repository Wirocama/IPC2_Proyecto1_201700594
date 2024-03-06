from xml.dom import minidom
from colorama import Fore
import webbrowser
import os

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
                print("")
                print(Fore.YELLOW + "-------------------------------------------------------------")
                print(Fore.YELLOW + "                        Desea cambiar patron?                ")
                print(Fore.YELLOW + "-------------------------------------------------------------")
                print("")
                print(Fore.WHITE + "1. Si")
                print(Fore.WHITE + "2. No")
                cambio = input("Selecciona una opcion: ")
                if cambio == "1":
                    self.cambiarPatron(listadoPisos,listadoPatron)
                elif cambio == "2":
                    print("Volviendo al Menu")
                     

              

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
    
    def cambiarPatron(self,piso,patron):

        patronOriginal = patron
        patronNuevo = self.mostrarPatrones(piso)
        cadenaOriginal = patronOriginal.colores.combinarColores()
        cadenaNueva = patronNuevo.colores.combinarColores()
        print("CADENA ORIGINAL: " + cadenaOriginal)
        print("CADENA NUEVA: "+ cadenaNueva)

        #VARIABLES DE INFORMACION
        precioIntercambio = piso.intercambiar
        precioVolteo = piso.voltear

        contadorFila = 1
        contadorColumna = 1
        inciso = 1
        cadenaCambio = ""
        cadenaArchivo = ""
        precioTotal = 0

        print("")
        print(Fore.YELLOW + "-------------------------------------------------------------")
        print(Fore.YELLOW + "             En donde desea ver la informacion               ")
        print(Fore.YELLOW + "-------------------------------------------------------------")
        print("")
        print(Fore.WHITE + "1. Archivo")
        print(Fore.WHITE + "2. Consola")
        mostrarInformacion = input("Selecciona una opcion: ")
        
            

        #CAMBIO DE POSICIONES


        while True:
            colorOriginal = patronOriginal.colores.buscarColor(str(contadorFila), str(contadorColumna))
            colorNuevo = patronNuevo.colores.buscarColor(str(contadorFila), str(contadorColumna))

            if contadorColumna < int(piso.columnas) and contadorFila<= int(piso.filas):
                if colorOriginal == colorNuevo:
                    cadenaCambio += colorNuevo
                    if mostrarInformacion == "1": 
                        cadenaArchivo += "\n" + str(inciso) + ". Las posiciones son Iguales."
                        cadenaArchivo += "\n" + cadenaOriginal
                        cadenaArchivo += "\n" + cadenaCambio
                    elif mostrarInformacion == "2":
                        print(str(inciso) + ". Las posiciones son Iguales.")
                        print(cadenaOriginal)
                        print(cadenaCambio)
                else:
                    colorSiguiente = patronOriginal.colores.buscarColor(str(contadorFila), str(contadorColumna + 1))
                    if colorSiguiente == colorNuevo:
                        patronOriginal.colores.cambiarColor(colorSiguiente, str(contadorFila), str(contadorColumna))
                        patronOriginal.colores.cambiarColor(colorOriginal, str(contadorFila), str(contadorColumna + 1))
                        precioTotal += int(precioIntercambio)
                        cadenaCambio += colorSiguiente
                        if mostrarInformacion == "1": 
                            cadenaArchivo += "\n" + str(inciso) + ". Se intercambiaron dos posiciones."
                            cadenaArchivo += "\n" + cadenaOriginal
                            cadenaArchivo += "\n" + cadenaCambio
                            cadenaArchivo += "\n precio acumulado: Q. " + str(precioTotal)
                        elif mostrarInformacion == "2":
                            print(str(inciso) + ". Se intercambiaron dos posiciones.")
                            print(cadenaOriginal)
                            print(cadenaCambio)
                            print("Precio Acumulado: Q. " + str(precioTotal))
                    else:
                        patronOriginal.colores.cambiarColor(colorNuevo, str(contadorFila), str(contadorColumna))
                        cadenaCambio += colorNuevo
                        precioTotal += int(precioVolteo)
                        if mostrarInformacion == "1": 
                            cadenaArchivo += "\n" + str(inciso) + ". Se volteo una posicion."
                            cadenaArchivo += "\n" + cadenaOriginal
                            cadenaArchivo += "\n" + cadenaCambio
                            cadenaArchivo += "\n precio acumulado: Q. " + str(precioTotal)
                        elif mostrarInformacion == "2":
                            print(str(inciso) + ". Se volteo una posicion.")
                            print(cadenaOriginal)
                            print(cadenaCambio)
                            print("Precio Acumulado: Q. " + str(precioTotal)) 
                contadorColumna +=1
                inciso +=1

            elif contadorColumna == int(piso.columnas) and contadorFila <= int(piso.filas):
                if colorOriginal == colorNuevo:
                    cadenaCambio += colorNuevo
                    if mostrarInformacion == "1": 
                        cadenaArchivo += "\n" + str(inciso) + ". Las posiciones son Iguales."
                        cadenaArchivo += "\n" + cadenaOriginal
                        cadenaArchivo += "\n" + cadenaCambio
                    elif mostrarInformacion == "2":
                        print(str(inciso) + ". Las posiciones son Iguales.")
                        print(cadenaOriginal)
                        print(cadenaCambio)
                else:
                    colorSiguiente = patronOriginal.colores.buscarColor(str(contadorFila), str(contadorColumna + 1))
                    if colorSiguiente == colorNuevo:
                        patronOriginal.colores.cambiarColor(colorSiguiente, str(contadorFila), str(contadorColumna))
                        patronOriginal.colores.cambiarColor(colorOriginal, str(contadorFila), str(contadorColumna + 1))
                        precioTotal += int(precioIntercambio)
                        cadenaCambio += colorSiguiente
                        if mostrarInformacion == "1": 
                            cadenaArchivo += "\n" + str(inciso) + ". Se intercambiaron dos posiciones."
                            cadenaArchivo += "\n" + cadenaOriginal
                            cadenaArchivo += "\n" + cadenaCambio
                            cadenaArchivo += "\n precio acumulado: Q. " + str(precioTotal)
                        elif mostrarInformacion == "2":
                            print(str(inciso) + ". Se intercambiaron dos posiciones.")
                            print(cadenaOriginal)
                            print(cadenaCambio)
                            print("Precio Acumulado: Q. " + str(precioTotal))
                    else:
                        patronOriginal.colores.cambiarColor(colorNuevo, str(contadorFila), str(contadorColumna))
                        cadenaCambio += colorNuevo
                        precioTotal += int(precioVolteo)
                        if mostrarInformacion == "1": 
                            cadenaArchivo += "\n" + str(inciso) + ". Se volteo una posicion."
                            cadenaArchivo += "\n" + cadenaOriginal
                            cadenaArchivo += "\n" + cadenaCambio
                            cadenaArchivo += "\n precio acumulado: Q. " + str(precioTotal)
                        elif mostrarInformacion == "2":
                            print(str(inciso) + ". Se volteo una posicion.")
                            print(cadenaOriginal)
                            print(cadenaCambio)
                            print("Precio Acumulado: Q. " + str(precioTotal)) 
                contadorColumna = 1
                contadorFila +=1
                inciso +=1
            else: 
                break

        if mostrarInformacion == "1":
            cadenaArchivo += "\n El costo del cambio de patron es: Q. " + str(precioTotal)
            archivo = open("NuevoPatron.txt","w")
            archivo.write(cadenaArchivo)
            archivo.close()
            webbrowser.open("NuevoPatron.txt", new = 2, autoraise = True)
            
        elif mostrarInformacion == "2":
            print("El costo del camcio de patron es: Q. " + str(precioTotal)) 
        patronNuevo.colores.graficarPatron(piso.nombre)

    def listadoGeneral(self):
        print("")
        print(Fore.YELLOW + "-------------------------------------------------------------")
        print(Fore.YELLOW + "                   LISTADO GENERAL DE PISOS                  ")
        print(Fore.YELLOW + "-------------------------------------------------------------")
        print("")
        lista_pisos.recorrerPisos()






        

    

        





        










        
        
