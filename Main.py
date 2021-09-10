import time, os

from Sintactico import parser
from Sintactico import cnt

file = open("Estudiantes.txt",'r',encoding="utf-8")
cadena = ""
for i in file:
    cadena += i
file.close()

def Menu():
    print("         .:Menu:.")
    print("")
    print("     [1] Procesar")
    print("     [2] Mostrar Estudiantes")
    print("     [3] Mostrar Tareas")
    print("     [0] Salir")
    print("")
    
    opcion = input("    Ingrese opcion: ")

    if opcion == "1":
        os.system("cls")
        Procesar()
        Menu()
    elif opcion  == "2":
        os.system("cls")
        MostrarEstudiante()
        Menu()
    elif opcion == "3":
        os.system("cls")
        MostrarTarea()
        Menu()
    elif opcion == "0":
        os.system("cls")
        exit()
    else:
        print("     Opcion incorrecta")
        time.sleep(1)
        os.system("cls")
        Menu()

def Procesar():

    parser.parse(cadena)
    # print(cadena)

    os.system("pause")
    os.system("cls")

def MostrarEstudiante():
            
    for i in cnt.cadenaF.split('\n'):
        print(i)
    print("")

    os.system("pause")
    os.system("cls")

def MostrarTarea():
    
    for i in cnt.cadenaT.split('\n'):
        print(i)
    print("")

    os.system("pause")
    os.system("cls")

Menu()