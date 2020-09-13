import random

class piece(object):

    def __init__(self, tipoFicha):
        """
        Inicializamos la ficha en una pocisión generica 0,0
        """  
        self.tipo = tipoFicha
        self.position = (0,0) 

    def setPosition(self):
        """
        Esta función selecciona una pocisión al azar para una ficha dentro del tablero
        """
        x = random.randint(0, 7)
        y = random.randint(0,7)
        self.position = (x,y)
        return self.position

    def getPosition(self):
        """
        Retorna: Pocisión actual de la ficha
        """
        return self.position
    
    def getTipo(self):
        """
            Retorna el tipo de pieza
        """
        return self.tipo


class peon(piece):
    def __init__(self):
        self.tipo = "PEON"
        self.position = (0,0)

    def Move(self):
        """
        Return: Lista con posibles movimientos de la ficha
        """
        #generar los posibles movimientos para la ficha
        #Para un peón los movimiento son una y dos casillas hacia adelante
        listaMovimientos = []
        listaMovimientos.append([self.position[0]+1,self.position[1]])
        listaMovimientos.append([self.position[0]+2,self.position[1]])
        listaMovimientos.append([self.position[0]-1,self.position[1]])
        listaMovimientos.append([self.position[0]-2,self.position[1]])
        return listaMovimientos


class alfil(piece):
    def __init__(self):
        self.tipo = "ALFIL"
        self.position = (0,0)

    def Move(self):
        """
        Return: Lista con posibles movimientos de la ficha
        """
        #generar los posibles movimientos para la ficha
        #Para un alfil el movimiento es en X
        listaMovimientos = []
        columna = self.position[1]
        fila = self.position[0]

        for i in range(1,8):
            listaMovimientos.append([fila-i,columna-i])
            listaMovimientos.append([fila+i,columna+i])
            listaMovimientos.append([fila-i,columna+i])
            listaMovimientos.append([fila+i,columna-i])

        return listaMovimientos

class torre(piece):
    def __init__(self):
        self.tipo = "TORRE"
        self.position = (0,0)

    def Move(self):
        """
        Return: Lista con posibles movimientos de la ficha
        """
        #generar los posibles movimientos para la ficha
        #Para una torre los movimiento son en forma de cruz

        listaMovimientos = []
        columna = self.position[1]
        fila = self.position[0]

        for j in range(8):
            if j != columna:
                listaMovimientos.append([fila, j])

        for i in range(8):
            if i != fila:
                listaMovimientos.append([i, columna])

        return listaMovimientos

class reina(piece):
    def __init__(self):
        self.tipo = "REINA"
        self.position = (0,0)

    def Move(self):
        """
        Return: Lista con posibles movimientos de la ficha
        """
        #generar los posibles movimientos para la ficha
        #Para la reina los posibles movimientos son en X y en cruz
        listaMovimientos = []
        columna = self.position[1]
        fila = self.position[0]

        #AGREGAMOS LOS MOVIMIENTOS EN CRUZ
        for j in range(8):
            if j != columna:
                listaMovimientos.append([fila, j])

        for i in range(8):
            if i != fila:
                listaMovimientos.append([i, columna])

        #AGREGAMOS LOS MOVIMIENTOS EN X 
        for i in range(1,8):
            listaMovimientos.append([fila-i,columna-i])
            listaMovimientos.append([fila+i,columna+i])
            listaMovimientos.append([fila-i,columna+i])
            listaMovimientos.append([fila+i,columna-i])

        return listaMovimientos

class rey(piece):
    def __init__(self):
        self.tipo = "REY"
        self.position = (0,0)

    def Move(self):
        """
        Return: Lista con posibles movimientos de la ficha
        """
        #generar los posibles movimientos para la ficha
        #Para un rey los posibles movimientos son un cuadrado alrededor de la ficha
        listaMovimientos = []
        columna = self.position[1]
        fila = self.position[0]
        listaMovimientos.append([fila-1,columna-1])
        listaMovimientos.append([fila-1, columna])
        listaMovimientos.append([fila-1, columna+1])
        listaMovimientos.append([fila, columna-1])
        listaMovimientos.append([fila, columna+1])
        listaMovimientos.append([fila+1, columna-1])
        listaMovimientos.append([fila+1, columna])
        listaMovimientos.append([fila+1,columna+1])

        return listaMovimientos


class caballo(piece):
    def __init__(self):
        self.tipo = "CABALLO"
        self.position = (0,0)

    def Move(self):
        """
        Return: Lista con posibles movimientos de la ficha
        """
        #generar los posibles movimientos para la ficha
        #Para un caballo los posibles movimientos son en L
        listaMovimientos = []
        columna = self.position[1]
        fila = self.position[0]

        #cuadrante1
        listaMovimientos.append([fila + 2, columna + 1])
        listaMovimientos.append([fila + 1, columna + 2])
        #cuadrante2
        listaMovimientos.append([fila - 1, columna + 2])
        listaMovimientos.append([fila - 2, columna + 1])
        #cuadrante3
        listaMovimientos.append([fila - 2, columna - 1])
        listaMovimientos.append([fila - 1, columna  - 2])
        #Cuadrante4
        listaMovimientos.append([fila + 1, columna - 2])
        listaMovimientos.append([fila + 2, columna  - 1])

        return listaMovimientos
