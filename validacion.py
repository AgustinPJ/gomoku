from tablero import Tablero

class validador:
    def __init__(self):
        pass

    def validar_fila(self,Tablero,fila:int,turno:str) : # valida si hay 5 en fila
        contador= 0
        for col in range(Tablero.dimension):
            if Tablero.grilla[fila][col] == turno:
                contador +=1
                if contador == 5:
                    return True
            else:
                contador = 0
        return False
    
    def validar_columna(self,Tablero,columna:int,turno:str): # valida si hay 5 en columna
        contador= 0
        for fil in range(Tablero.dimension):
            if Tablero.grilla[fil][columna] == turno:                        
                contador +=1
                if contador == 5:
                    return True
            else:
                contador = 0
        return False
    
    def validar_diagonal_negativa(self,Tablero,fila:int,columna:int,turno: str): # valida si hay 5 en diagonal descendiente
        contador = 1
        for i in range(1,5):
            if Tablero.esta_en_rango(fila + i,columna + i) and Tablero.grilla[fila + i][(columna + i)] == turno: # parte inferior/derecha
                contador += 1
                if contador == 5:
                    return True
            else:
                break
        for j in range(1,5):
            if Tablero.esta_en_rango(fila - j,columna - j) and Tablero.grilla[fila - j][(columna - j)] == turno: # parte superior/izquierda
                contador +=1
                if contador == 5:
                    return True
            else:
                break
        return False
    
    def validar_diagonal_positiva(self,Tablero,fila:int,columna:int,turno: str): # valida si hay 5 en diagonal ascendente
        contador = 1
        for i in range(1,5):
            if Tablero.esta_en_rango(fila - i,columna + i) and Tablero.grilla[fila - i][(columna + i)] == turno: # parte superior/derecha
                contador += 1
                if contador == 5:
                    return True
            else:
                break  
        for j in range(1,5):
            if Tablero.esta_en_rango(fila + j,columna - j) and Tablero.grilla[fila + j][(columna - j)] == turno:# parte inferior/izquierda
                contador +=1
                if contador == 5:
                    return True
            else:
                break
        return False
    def validar_ganador(self,Tablero,fila:int,columna:int,turno:str): # valida si hay ganador
        return (self.validar_fila(Tablero,fila,turno) 
                or self.validar_columna(Tablero,columna,turno) 
                or self.validar_diagonal_negativa(Tablero,fila,columna,turno) 
                or self.validar_diagonal_positiva(Tablero,fila,columna,turno))
    
    def validar_empate(self,Tablero,turnos_jugados:int): # valida si hay empate
        return turnos_jugados == Tablero.dimension * Tablero.dimension