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