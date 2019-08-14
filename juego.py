import curses
import serpiente
import puntuacion
import menu
import reportes
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN

class juego:
    def __init__(self, window, usuario, timeout, puntuacion1):
        self.window = window
        self.window.clear()
        self.timeout = timeout
        self.nivel = 1
        self.window.border(0)
        self.posiniciousuario = 100 - len(usuario)
        self.usuario = usuario
        self.window.addstr(0, self.posiniciousuario - 2, self.usuario)
        snake = serpiente.cuerposerpiente(10, 15, window, timeout)
        self.score = puntuacion.pilapuntuacion()
        self.window.addstr(0, 2, "Puntuacion: {}".format(self.score.size()))
        self.window.timeout(timeout)
        comida = serpiente.comida(window)
        comida.generar_comida(self.score.size())
        while True:
            self.window.clear()
            self.window.border(0)
            self.window.addstr(0, 2, "Puntuacion: {}".format(self.score.size()))
            self.window.addstr(0, 46, "Nivel: {}".format(self.nivel))
            snake.pintar()
            comida.pintar_comida()
            self.window.addstr(34, 0, "Presione P para pausar")
            self.window.addstr(0, self.posiniciousuario - 2, self.usuario)
            event = window.getch()

            if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                snake.cambiardireccion(event)
            else:
                if event == 112:
                    self.window.clear()
                    self.window.border(0)
                    menupause = menu.menu(window)
                    menupause.menupausa()
                    self.window.addstr(34, 0, "Presione P para reanudar el juego")
                    self.window.addstr(0, self.posiniciousuario - 2, self.usuario)
                    tecla = -1
                    while tecla != 112:
                        tecla = window.getch()
                        if tecla == 49:
                            self.window.clear()
                            self.window.border(0)
                            rep = reportes.reportes(window)
                            rep.pantallagenerarreportesnake(snake.get_Cabeza())
                        else:
                            if tecla == 50:
                                self.window.clear()
                                self.window.border(0)
                                rep = reportes.reportes(window)
                                rep.pantallagenerarreportepunteo(self.score.get_pila())
                        self.window.clear()
                        self.window.border(0)
                        menupause.menupausa()
                        self.window.addstr(34, 0, "Presione P para reanudar el juego")
                        self.window.addstr(0, self.posiniciousuario - 2, self.usuario)
                    
                    self.window.clear()
                    self.window.border(0)
                    self.window.addstr(0, 2, "Puntuacion: {}".format(self.score.size()))
                    self.window.addstr(0, 46, "Nivel: {}".format(self.nivel))
                    snake.pintar()
                    comida.pintar_comida()
                    self.window.addstr(34, 0, "Presione P para pausar")
                    self.window.addstr(0, self.posiniciousuario - 2, self.usuario)

            snake.mover()
            if snake.get_Cabeza().posicionx == comida.coordenadacomidax() and snake.get_Cabeza().posiciony == comida.coordenadacomiday():
                tipocomida = comida.obtenertipocomida()
                if tipocomida < 80:
                    posxcomida = comida.coordenadacomidax()
                    posycomida = comida.coordenadacomiday()
                    self.score.push(posxcomida, posycomida)
                    snake.agregar()
                    auxscore = int(round(self.score.size() % 15))
                    if auxscore == 0 and self.score.size() > 0:
                        self.timeout = round(self.timeout / 2)
                        self.window.timeout(self.timeout)
                        self.nivel += 1
                else:
                    auxscore = int(round(self.score.size() % 15))
                    if auxscore == 0:
                        self.timeout = self.timeout * 2
                        self.window.timeout(self.timeout)
                        self.nivel -= 1
                    self.score.pop()

                    snake.eliminar()
                comida.generar_comida(self.score.size())
                print(comida.obtenertipocomida())

            if snake.chocar() == True:
                self.window.clear()
                self.window.border(0)
                menupause = menu.menu(window)
                menupause.menugameover()
                #puntuacion1 = score.size()
                tecla = -1
                while True:
                    tecla = self.window.getch()
                    if tecla == 51:
                        break
                    else:
                        if tecla == 49:
                            self.window.clear()
                            self.window.border(0)
                            rep = reportes.reportes(window)
                            rep.pantallagenerarreportesnake(snake.get_Cabeza())
                            self.window.clear()
                            self.window.border(0)
                            menupause.menugameover()
                        else:
                            if tecla == 50:
                                self.window.clear()
                                self.window.border(0)
                                rep = reportes.reportes(window)
                                rep.pantallagenerarreportepunteo(self.score.get_pila())
                                self.window.clear()
                                self.window.border(0)
                                menupause.menugameover()

                if tecla == 51:
                    break
                #break

    def get_score(self):
        return self.score.size()