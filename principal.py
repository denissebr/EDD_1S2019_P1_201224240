import curses
import menu
import usuario
import juego

#Tamaño de la ventana
ALTO = 35
ANCHO = 100
TIMEOUT = 500
USUARIOACTIVO = ""

curses.initscr()
window = curses.newwin(ALTO, ANCHO, 0, 0)
window.timeout(TIMEOUT)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
window.border(0)

menusnake = menu.menu(window)
menusnake.pintarmenu()
usuarios = usuario.listausuarios(window)

while True:
    event = window.getch()

    if event == 54:
        break
    else:
        if event == 49 and not USUARIOACTIVO:
            USUARIOACTIVO = usuarios.mostrarusuarios()
            if USUARIOACTIVO:
                pantallajuego = juego.juego(window, USUARIOACTIVO, TIMEOUT)
        else:
            if event == 49 and USUARIOACTIVO:
                pantallajuego = juego.juego(window, USUARIOACTIVO, TIMEOUT)

    

curses.endwin()