class nodopuntuacion:
    def __init__(self, posx, posy):
        self.posicionx = posx
        self.posiciony = posy
        self.anterior = None

class pilapuntuacion:
    def __init__(self):
        self.pila = None

    def push(self, posx, posy):
        nuevonodo = nodopuntuacion(posx, posy)
        if self.pila is None:
            self.pila = nuevonodo
        else:
            nuevonodo.anterior = self.pila
            self.pila = nuevonodo

    def pop(self):
        nodoaux = self.pila
        self.pila = self.pila.anterior
        nodoaux.anterior = None

    def size(self):
        if self.pila is None:
            return 0
        else:
            nodoaux = self.pila
            contador = 1
            nodoaux = nodoaux.anterior
            while nodoaux:
                contador += 1
                nodoaux = nodoaux.anterior
            return contador