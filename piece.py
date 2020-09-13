import random

class piece(object):
    position = ()

    def __init__(self):
        """
        Inicializamos la ficha en una pocisión generica 0,0
        """  
        self.position = (0,0) 

    def setPosition(self):
        """
        Esta función selecciona una pocisión al azar para una ficha dentro del tablero
        """
        x = random.randint(0, 7)
        y = random.randint(0,7)
        self.position = (x,y)
        return self.position
    

class peon(piece):
    def __init__(self):
        pass


class arfil(piece):
    def __init__(self):
        pass

class torre(piece):
    def __init__(self):
        pass

class reina(piece):
    def __init__(self):
        pass

class rey(piece):
    def __init__(self):
        pass

class caballo(piece):
    def __init__(self):
        pass
