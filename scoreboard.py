class nodocolapuntuacion:
    def __init__(self, nombreusuario, puntuacion):
        self.nombre_usuario = nombreusuario
        self.puntuacion = puntuacion
        self.siguiente = None

class colapuntuacion:
    def __init__(self, window):
        self.iniciocola = None
        self.fincola = None
        self.window = window

    def Queue(self, nombre, puntuacion):
        nuevonodo = nodocolapuntuacion(nombre, puntuacion)
        if self.iniciocola is None:
            self.iniciocola = nuevonodo
            self.fincola = nuevonodo
        else:
            self.fincola.siguiente = nuevonodo
            self.fincola = self.fincola.siguiente

    def Unqueued(self):
        nodoaux = self.iniciocola
        self.iniciocola = self.iniciocola.siguiente
        nodoaux.siguiente = None

    def size(self):
        cont = 0
        nodoaux = self.iniciocola
        while nodoaux:
            cont += 1
            nodoaux = nodoaux.siguiente
        return cont

    def get_cola(self):
        return self.iniciocola

    def mostrarpuntuaciones(self):
        pos = int((35 - self.size())/2)
        nodoaux = self.iniciocola
        self.window.clear()
        self.window.border(0)
        self.window.addstr(0, 44, "PUNTUACIONES")
        while nodoaux:
            nombre = nodoaux.nombre_usuario
            punteo = nodoaux.puntuacion
            
            self.window.addstr(pos, 47-len(nombre), nombre)
            self.window.addstr(pos, 53, "{}".format(punteo))
            pos += 1
            nodoaux = nodoaux.siguiente
        self.window.addstr(pos, 45, "1 Regresar")
        while True:
            event = self.window.getch()
            if event == 49:
                break


