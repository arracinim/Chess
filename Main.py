import sys
sys.path.append(".")

from board import board
from piece import peon, torre, caballo,alfil,reina, rey
import numpy as np

#Main
if __name__ == "__main__":
    boardDictionary = {}
    pieceNames = ["PEON", "ALFIL", "REINA", "REY", "TORRE", "CABALLO"]
    

    """Para cada pieza generamos un tablero diferente, inicializamos en una pocisión 
        Aleatoria del tablero y generamos las posibles pocisiones"""

    for piece in pieceNames:
        if piece == "PEON":
            boardDictionary[piece+" BOARD"] = board()
            peon = peon()
            #generamos una pocision incial aleatoria para la ficha
            posicionInicial = peon.setPosition()
            #Generamos la lista con los posibles movimientos para la pieza en cuestion
            posiblesMovimientos = peon.Move()
            #Añadimos la pocision inicial de la ficha al tablero
            boardDictionary[piece+" BOARD"].pieceposition(posicionInicial[0],posicionInicial[1])
            #Agregamos al tablero las posibles posiciones para la ficha en cuestion
            for movimiento in posiblesMovimientos:
                try:
                    boardDictionary[piece+" BOARD"].pieceMovement(movimiento)
                except:
                    pass

        elif piece == "ALFIL":
            boardDictionary[piece+" BOARD"] = board()
            alfil = alfil()
            #generamos una pocision incial aleatoria para la ficha
            posicionInicial = alfil.setPosition()
            #Generamos la lista con los posibles movimientos para la pieza en cuestion
            posiblesMovimientos = alfil.Move()
            #Añadimos la pocision inicial de la ficha al tablero
            boardDictionary[piece+" BOARD"].pieceposition(posicionInicial[0],posicionInicial[1])
            #Agregamos al tablero las posibles posiciones para la ficha en cuestion
            for movimiento in posiblesMovimientos:
                try:
                    boardDictionary[piece+" BOARD"].pieceMovement(movimiento)
                except:
                    pass
            

        elif piece == "REINA":
            boardDictionary[piece+" BOARD"] = board()
            reina = reina()
            #generamos una pocision incial aleatoria para la ficha
            posicionInicial = reina.setPosition()
            #Generamos la lista con los posibles movimientos para la pieza en cuestion
            posiblesMovimientos = reina.Move()
            #Añadimos la pocision inicial de la ficha al tablero
            boardDictionary[piece+" BOARD"].pieceposition(posicionInicial[0],posicionInicial[1])
            #Agregamos al tablero las posibles posiciones para la ficha en cuestion
            for movimiento in posiblesMovimientos:
                try:
                    boardDictionary[piece+" BOARD"].pieceMovement(movimiento)
                except:
                    pass
            

        elif piece == "REY":
            boardDictionary[piece+" BOARD"] = board()
            rey = rey()
            #generamos una pocision incial aleatoria para la ficha
            posicionInicial = rey.setPosition()
            #Generamos la lista con los posibles movimientos
            posiblesMovimientos = rey.Move()
            #Añadimos la pocision inicial de la ficha al tablero
            boardDictionary[piece+" BOARD"].pieceposition(posicionInicial[0],posicionInicial[1])
            #Agregamos al tablero las posibles posiciones para la ficha en cuestion
            for movimiento in posiblesMovimientos:
                try:
                    boardDictionary[piece+" BOARD"].pieceMovement(movimiento)
                except:
                    pass
            


        elif piece == "TORRE":
            boardDictionary[piece+" BOARD"] = board()
            torre = torre()
            #generamos una pocision incial aleatoria para la ficha
            posicionInicial = torre.setPosition()
            #Generamos la lista con los posibles movimientos
            posiblesMovimientos = torre.Move()
            #Añadimos la pocision inicial de la ficha al tablero
            boardDictionary[piece+" BOARD"].pieceposition(posicionInicial[0],posicionInicial[1])
            #Agregamos al tablero las posibles posiciones para la ficha en cuestion
            for movimiento in posiblesMovimientos:
                try:
                    boardDictionary[piece+" BOARD"].pieceMovement(movimiento)
                except:
                    pass
            


        elif piece == "CABALLO":
            boardDictionary[piece+" BOARD"] = board()
            caballo = caballo()
            #generamos una pocision incial aleatoria para la ficha
            posicionInicial = caballo.setPosition()
            #Generamos la lista con los posibles movimientos
            posiblesMovimientos = caballo.Move()
            #Añadimos la pocision inicial de la ficha al tablero
            boardDictionary[piece+" BOARD"].pieceposition(posicionInicial[0],posicionInicial[1])
            #Agregamos al tablero las posibles posiciones para la ficha en cuestion
            for movimiento in posiblesMovimientos:
                try:
                    boardDictionary[piece+" BOARD"].pieceMovement(movimiento)
                except:
                    pass
            

        else:
            pass

        #IMPRIMIMOS LOS DIFERENTES POSIBLES MOVIMIENTOS PARA UNA FICHA DADA UNA POCISION ALEATORIA.

