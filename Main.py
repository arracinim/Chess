import sys
sys.path.append(".")

from board import board
#from piece import *


#Main
if __name__ == "__main__":
    boardDictionary = {}
    pieceNames = ["PEON", "ARFIL", "REINA", "REY", "TORRE", "CABALLO"]
    

    """Para cada pieza generamos un tablero diferente, inicializamos en una pocisión 
        Aleatoria del tablero y generamos las posibles pocisiones"""

    for piece in pieceNames:
        if piece == "PEON":
            boardDictionary[piece+" BOARD"] = board()

        elif piece == "ARFIL":
            boardDictionary[piece+" BOARD"] = board()

        elif piece == "REINA":
            boardDictionary[piece+" BOARD"] = board()

        elif piece == "REY":
            boardDictionary[piece+" BOARD"] = board()

        elif piece == "TORRE":
            boardDictionary[piece+" BOARD"] = board()

        elif piece == "CABALLO":
            boardDictionary[piece+" BOARD"] = board()

        else:
            pass