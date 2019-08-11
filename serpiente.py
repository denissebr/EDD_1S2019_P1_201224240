from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

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