import curses
import serpiente
import puntuacion
import menu
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN

class juego:
    def __init__(self, window, usuario, timeout):
        self.window = window
        self.window.clear()
        self.timeout = timeout
        self.nivel = 1
        self.window.border(0)
        self.posiniciousuario = 100 - len(usuario)
        self.usuario = usuario
        self.window.addstr(0, self.posiniciousuario - 2, self.usuario)
        snake = serpiente.cuerposerpiente(10, 15, window, timeout)
        score = puntuacion.pilapuntuacion()
        self.window.addstr(0, 2, "Puntuacion: {}".format(score.size()))
        self.window.timeout(timeout)
        comida = serpiente.comida(window)
        comida.generar_comida(score.size())
        while True:
            self.window.clear()
            self.window.border(0)
            self.window.addstr(0, 2, "Puntuacion: {}".format(score.size()))
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
                    window.clear()
                    window.border(0)
                    menupause = menu.menu(window)
                    menupause.menupausa()
                    window.addstr(34, 0, "Presione P para reanudar el juego")
                    window.addstr(0, self.posiniciousuario - 2, self.usuario)
                    tecla = -1
                    while tecla != 112:
                        tecla = window.getch()
                    self.window.clear()
                    self.window.border(0)
                    self.window.addstr(0, 2, "Puntuacion: {}".format(score.size()))
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
                    score.push(posxcomida, posycomida)
                    snake.agregar()
                    auxscore = int(round(score.size() % 15))
                    if auxscore == 0 and score.size() > 0:
                        self.timeout = round(self.timeout / 2)
                        self.window.timeout(self.timeout)
                        self.nivel += 1
                else:
                    auxscore = int(round(score.size() % 15))
                    if auxscore == 0:
                        self.timeout = self.timeout * 2
                        self.window.timeout(self.timeout)
                        self.nivel -= 1
                    score.pop()

                    snake.eliminar()
                comida.generar_comida(score.size())
                print(comida.obtenertipocomida())

            if snake.chocar() == True:
                window.clear()
                window.border(0)
                menupause.menugameover()
                #break