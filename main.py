from juego import Juego
from tablero import Tablero

def mostrar_tablero(tablero:Tablero):# muestra el tablero
   print( "  "+" ".join ( str(i+1)  for i in range(tablero.dimension))) #fila de indices
   for j in range(tablero.dimension):
        print((str(j+1)+" "+" ".join("."if celda is None else str(celda) for celda in tablero.grilla[j]))) #muestra el indice de columna + fila
def pedir_dimension():
    while True:
        try:
            dimension = int(input("indica dimension del tablero(>=5): "))
            if dimension <5:
                print("ERROR:dimension indicada muy pequeña, ingrese una dimension valida")
                continue
            break
                
        except ValueError:
            print("ERROR:ingrese un numero entero por favor")
def iniciar():
    dimension = pedir_dimension
    juego = juego(dimension)
    mostrar_tablero(juego)
    while juego.self.estado == "jugando":
        print("-----")