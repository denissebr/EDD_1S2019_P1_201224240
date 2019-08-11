import curses
import serpiente
import puntuacion
from curses import KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN

class juego:
    def __init__(self, window, usuario, timeout):
        self.window = window
        self.window.clear()
        self.window.border(0)
        self.posiniciousuario = 100 - len(usuario)
        self.usuario = usuario
        self.window.addstr(0, self.posiniciousuario - 2, self.usuario)
        snake = serpiente.cuerposerpiente(10, 15, window, timeout)
        score = puntuacion.pilapuntuacion()
        self.window.addstr(0, 0, "Puntuacion: {}".format(score.size()))
        self.window.timeout(timeout)
        while True:
            self.window.clear()
            self.window.border(0)
            self.window.addstr(0, 0, "Puntuacion: {}".format(score.size()))
            snake.pintar()
            self.window.addstr(34, 0, "Presione P para pausar")
            self.window.addstr(0, self.posiniciousuario - 2, self.usuario)
            event = window.getch()

            if event in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
                snake.cambiardireccion(event)
            else:
                if event == 112:
                    window.clear()
                    window.border(0)
                    
                    window.addstr(34, 0, "Presione P para reanudar el juego")
                    window.addstr(0, self.posiniciousuario - 2, self.usuario)
                    tecla = -1
                    while tecla != 112:
                        tecla = window.getch()
            
            snake.mover()