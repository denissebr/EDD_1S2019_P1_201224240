import curses
import menu

#Tamaño de la ventana
ALTO = 35
ANCHO = 100
TIMEOUT = 500

curses.initscr()
window = curses.newwin(ALTO, ANCHO, 0, 0)
window.timeout(TIMEOUT)
window.keypad(True)
curses.noecho()
curses.curs_set(0)
window.border(0)

menusnake = menu.menu(window)
menusnake.pintarmenu()

while True:
    event = window.getch()

    if event == 54:
        break


    

curses.endwin()