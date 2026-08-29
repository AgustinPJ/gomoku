from juego import Juego
from tablero import Tablero

def mostrar_tablero(tablero: Tablero):  # muestra el tablero
    print( "   "+" ".join ( f"{i + 1 :>2}"  for i in range(tablero.dimension)))  #fila de indices
    for j in range(tablero.dimension):
            print((f"{j + 1 :>2} "+" ".join(" ."if celda is None else f"{celda :>2}" for celda in tablero.grilla[j])))  #muestra el indice de columna + fila grilla
def pedir_dimension():  # pide la dimension 
    while True:
        try:
            dimension = int(input("indica dimension del tablero(>=5): "))
            if dimension < 5:
                print("ERROR:dimension indicada muy pequeña, ingrese una dimension valida")
                continue
            return dimension
                
        except ValueError:
            print("ERROR:ingrese un numero entero por favor")
def main(): 
    dimension = pedir_dimension()
    juego = Juego(dimension)
    print("----- juego iniciado -----")
    while juego.estado == "jugando":
        mostrar_tablero(juego.tablero)
        print(f"----- Turno {juego.turno}----- ")
        fila = int(input("ingrese indice de la fila: ")) - 1
        columna = int(input("ingrese indice de la columna: ")) - 1
        valida, mensaje = juego.jugada(fila, columna)
        print({mensaje})
    mostrar_tablero(juego.tablero)
    try:    
        seguir = int(input("\nvolver a jugar 1.si / 2.no : " ))
        if seguir == 1:
            main()
        elif seguir == 2:
            print("----- gracias por jugar -----")
    except ValueError:
            print(" ingrese opcion valida (1 o 2)")

    
main()