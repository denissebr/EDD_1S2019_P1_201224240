import curses

class menu:
    def __init__(self, window):
        self.window = window

    def pintarmenu(self):
        self.window.addstr(15, 46, "1 Jugar")
        self.window.addstr(16, 43, "2 Puntuaciones")
        self.window.addstr(17, 45, "3 Usuarios")
        self.window.addstr(18, 45, "4 Reportes")
        self.window.addstr(19, 43, "5 Carga Masiva")
        self.window.addstr(20, 46, "6 Salir")

    def menupausa(self):
        self.window.addstr(0, 47, "Pausa")
        self.window.addstr(16, 40, "1 Reporte Serpiente")
        self.window.addstr(17, 42, "2 Reporte Punteo")
        self.window.addstr(18, 42, "P Reanudar Juego")

    def menugameover(self):
        self.window.addstr(0, 45, "Game over")
        self.window.addstr(16, 40, "1 Reporte Serpiente")
        self.window.addstr(17, 42, "2 Reporte Punteo")
        self.window.addstr(18, 41, "3 Regresar al menu")
