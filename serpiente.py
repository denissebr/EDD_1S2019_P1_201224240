from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

class nodoserpiente:
    def __init__(self, posx, posy, caracter = '#'):
        self.posicionx = posx
        self.posiciony = posy
        self.siguiente = None
        self.anterior = None
        self.caracter = caracter

class cuerposerpiente:
    def __init__(self, posx, posy, window, timeout):
        self.cabeza = nodoserpiente(posx, posy, "$")
        self.cola = nodoserpiente(posx - 1, posy)
        self.cabeza.siguiente = self.cola
        self.cola.anterior = self.cabeza
        auxcola = nodoserpiente(posx - 2, posy)
        self.cola.siguiente = auxcola
        auxcola.anterior = self.cola
        self.cola = self.cola.siguiente
        self.window = window
        self.timeout = timeout
        self.direccion = KEY_RIGHT

    def pintar(self):
        nodoaux = self.cabeza
        while nodoaux != None:
            self.window.addstr(nodoaux.posiciony, nodoaux.posicionx, nodoaux.caracter)
            nodoaux = nodoaux.siguiente

    def cambiardireccion(self, direccion):
        if self.direccion == 261 and (direccion == 259 or direccion == 258):
            self.direccion = direccion
        else:
            if self.direccion == 259 and (direccion == 260 or direccion == 261):
                self.direccion = direccion
            else:
                if self.direccion == 260 and (direccion == 259 or direccion == 258):
                    self.direccion = direccion
                else:
                    if self.direccion == 258 and (direccion == 260 or direccion == 261):
                        self.direccion = direccion

    def get_Cabeza(self):
        return self.cabeza
    
    def mover(self):
        if self.direccion == 261: #DERECHA
            nodoaux = self.cabeza
            posicionxant = nodoaux.posicionx
            posicionyant = nodoaux.posiciony
            nodoaux.posicionx = nodoaux.posicionx + 1
            nodoaux = nodoaux.siguiente
            while nodoaux:
                auxx = nodoaux.posicionx
                auxy = nodoaux.posiciony
                nodoaux.posicionx = posicionxant
                nodoaux.posiciony = posicionyant
                posicionxant = auxx
                posicionyant = auxy
                nodoaux = nodoaux.siguiente
        else:
            if self.direccion == 259: #ARRIBA
                nodoaux = self.cabeza
                posicionxant = nodoaux.posicionx
                posicionyant = nodoaux.posiciony
                nodoaux.posiciony = nodoaux.posiciony - 1
                nodoaux = nodoaux.siguiente
                while nodoaux:
                    auxx = nodoaux.posicionx
                    auxy = nodoaux.posiciony
                    nodoaux.posicionx = posicionxant
                    nodoaux.posiciony = posicionyant
                    posicionxant = auxx
                    posicionyant = auxy
                    nodoaux = nodoaux.siguiente
            else:
                if self.direccion == 260: #IZQUIERDA
                    nodoaux = self.cabeza
                    posicionxant = nodoaux.posicionx
                    posicionyant = nodoaux.posiciony
                    nodoaux.posicionx = nodoaux.posicionx - 1
                    nodoaux = nodoaux.siguiente
                    while nodoaux:
                        auxx = nodoaux.posicionx
                        auxy = nodoaux.posiciony
                        nodoaux.posicionx = posicionxant
                        nodoaux.posiciony = posicionyant
                        posicionxant = auxx
                        posicionyant = auxy
                        nodoaux = nodoaux.siguiente
                else:
                    if self.direccion == 258:#ABAJO
                        nodoaux = self.cabeza
                        posicionxant = nodoaux.posicionx
                        posicionyant = nodoaux.posiciony
                        nodoaux.posiciony = nodoaux.posiciony + 1
                        nodoaux = nodoaux.siguiente
                        while nodoaux:
                            auxx = nodoaux.posicionx
                            auxy = nodoaux.posiciony
                            nodoaux.posicionx = posicionxant
                            nodoaux.posiciony = posicionyant
                            posicionxant = auxx
                            posicionyant = auxy
                            nodoaux = nodoaux.siguiente
                        

class comida:
    def __init__(self, window):
        self.window = window
    
    def generar_comida(self, score):
        self.poscomidax = randint(1, 98)
        self.poscomiday = randint(1, 33)
        if score == 0:
            self.tipocomida = 10
        else:
            self.tipocomida = randint(1, 100)

    def pintar_comida(self):
        if self.tipocomida < 80:
            self.window.addstr(self.poscomiday, self.poscomidax, "+")
        else:
            self.window.addstr(self.poscomiday, self.poscomidax, "*")

    def coordenadacomidax(self):
        return self.poscomidax

    def coordenadacomiday(self):
        return self.poscomiday

    def obtenertipocomida(self):
        return self.tipocomida