from curses import KEY_RIGHT, KEY_LEFT
import os

class nodousuario:
    def __init__(self, nombreusuario):
        self.nombre_usuario = nombreusuario
        self.anterior = None
        self.siguiente = None

class listausuarios:
    def __init__(self, window):
        self.window = window
        self.principio = None
        self.fin = None

    def insetarusuario(self, nombre):
        nodonuevo = nodousuario(nombre)
        if self.principio is None:
            self.principio = nodonuevo
            self.fin = nodonuevo
            self.principio.siguiente = self.fin
            self.principio.anterior = self.fin
        else:
            self.fin.siguiente = nodonuevo
            nodonuevo.siguiente = self.principio
            nodonuevo.anterior = self.fin
            self.fin = nodonuevo
            self.principio.anterior = self.fin

    def get_inicio(self):
        return self.principio

    def get_fin(self):
        return self.fin

    def mostrarusuarios(self):
        nodoaux = self.principio
        cadenanombre = ""
        self.window.clear()
        self.window.border(0)
        while True:
            event = self.window.getch()

            if self.principio is None:
                self.window.addstr(17, 42, "1 Crear Usuario")
            else:
                cadenanombre = "<< "
                cadenanombre += nodoaux.nombre_usuario
                cadenanombre += " >>"
                posicioninicionombre = 100 - len(cadenanombre)
                posicioninicionombre = posicioninicionombre / 2
                self.window.addstr(16, round(posicioninicionombre), cadenanombre)
                self.window.addstr(17, 42, "1 Crear Usuario")
                self.window.addstr(18, 43, "2 Seleccionar")
#mover entre usuarios
            if event == KEY_RIGHT and self.principio is not None:
                nodoaux = nodoaux.siguiente
                self.window.clear()
                self.window.border(0)
            else:
                if event == KEY_LEFT and self.principio is not None:
                    nodoaux = nodoaux.anterior
                    self.window.clear()
                    self.window.border(0)
                
#crear usuarios
            if event == 49:
                posx = posicicioninicial = 48
                auxnombre = ""
                self.window.clear()
                self.window.border(0)
                self.window.addstr(17, 40, "Nombre: ")
                self.window.addstr(18, 40, "Presione Enter para guardar")
                while True:
                    event1 = self.window.getch()
                    if (event1 > 64 and event1 < 90) or (event1 > 96 and event1 < 123) or (event1 > 47 and event1 < 58):
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(17, 40, "Nombre: ")
                        self.window.addstr(18, 40, "Presione Enter para guardar")
                        self.window.addstr(17, posicicioninicial, auxnombre)
                        self.window.addstr(17, posx, chr(event1))
                        posx += 1
                        auxnombre += chr(event1)
                    else:
                        if event1 == 8:
                            if posx != posicicioninicial:
                                self.window.clear()
                                self.window.border(0)
                                self.window.addstr(17, 40, "Nombre: ")
                                self.window.addstr(18, 40, "Presione Enter para guardar")
                                auxnombre = auxnombre[:-1]
                                self.window.addstr(17, posicicioninicial, auxnombre)
                                posx -= 1
                        else:
                            if (event1 == 459 or event1 == 10) and posx != posicicioninicial:
                                self.insetarusuario(auxnombre)
                                nodoaux = self.principio
                                break
                self.window.clear()
                self.window.border(0)
            else:
                if event == 50 and nodoaux is not None:
                    return nodoaux.nombre_usuario

    def carga_masiva(self):
        self.window.addstr(16, 20, "Archivo csv: ")
        self.window.addstr(17, 20, "Presione Enter para cargar")
        tecla = -1
        posx = posicioninicial = 33
        auxnombre = ""
        while True:
            tecla = self.window.getch()
            if (tecla > 31 and tecla < 127) or tecla == 92:
                self.window.clear()
                self.window.border(0)
                self.window.addstr(16, 20, "Archivo csv: ")
                self.window.addstr(17, 20, "Presione Enter para cargar")
                self.window.addstr(16, posicioninicial, auxnombre)
                self.window.addstr(16, posx, chr(tecla))
                posx += 1
                auxnombre += chr(tecla)
            else:
                if tecla == 8:
                    if posx != posicioninicial:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(16, 20, "Archivo csv: ")
                        self.window.addstr(17, 20, "Presione Enter para cargar")
                        auxnombre = auxnombre[:-1]
                        self.window.addstr(16, posicioninicial, auxnombre)
                        posx -= 1
                else:
                    if (tecla == 459 or tecla == 10) and posx != posicioninicial:
                        if os.path.exists(auxnombre):
                            archivo = open(auxnombre, "r")
                            cont = 0
                            for linea in archivo.readlines():
                                linea = linea.replace("\n", "")
                                if cont != 0 and len(linea) > 0:
                                    self.insetarusuario(linea)
                                cont+=1
                            archivo.close
                            break
                        else:
                            self.window.addstr(18, 36, "El archivo no existe.")
        