from tkinter import *
from tkinter import filedialog
from colorama import Fore
from Informacion import Informacion

info = Informacion()


def menu():

    while True:

        #MENU PRINCIPAL
        print("")

        print(Fore.YELLOW + "-------------------------------------------------------------")
        print(Fore.YELLOW + "                        MENÚ PRINCIPAL                       ")
        print(Fore.YELLOW + "-------------------------------------------------------------")

        print("")
        print(Fore.WHITE + "1. Cargar Archivo")
        print(Fore.WHITE + "2. Mostrar la grafica del Patron")
        print(Fore.WHITE + "3. Seleccionar nuevo codigo de Patron")
        print(Fore.WHITE + "4. Mostrar todos los pisos")
        print(Fore.WHITE + "5. Salir")
        print("")

        #INPUT DE SELECCIÓN
        valor = input(Fore.CYAN + "Seleccionar Una Opción: ")

        if valor == "1":
            #MÉTODO PARA CARGAR EL ARCHIVO

            cargar_archivo()
    
            
        elif valor == "2":   
            info.graficar()

        elif valor == "3":   
            #opcion 3
            pass
        
        elif valor == "4":   
            #opcion 4
            pass

                    
        elif valor == "5":
            break        

        else:
            print("")
            print(Fore.RED + "-------------------------------------------------------------")
            print(Fore.RED + "           INGRESE UNA DE LAS OPCIONES ANTERIORES            ")
            print(Fore.RED + "-------------------------------------------------------------")
            print("")    

def cargar_archivo():
    

    print(Fore.YELLOW + "\n-------------------------------------------------------------")
    print(Fore.WHITE + "                         CARGAR ARCHIVO                       ")
    print(Fore.YELLOW + "-------------------------------------------------------------")
    
    #try:
    #RUTA DEL DOCUMENTO
    ruta = filedialog.askopenfilename(initialdir = "/Desktop", title = "Seleccionar Archivo",
    filetypes=(("Todos los Archivos","*.*"),("Archivos de Texto","*.txt")))

    info.obtenerInformacion(ruta)
    print("")
    print(Fore.GREEN + "La ruta del Archivo es: " + Fore.WHITE + ruta) 
    print("ARCHIVO LEIDO CORRECTAMENTE")  
    #except:
        
        #print(Fore.RED + "\n||||||||||||||||||| " + Fore.WHITE + "ERROR AL LEER ARCHIVO"+ Fore.RED + " |||||||||||||||||||")
        
menu()