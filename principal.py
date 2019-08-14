import curses
import menu
import usuario
import juego
import scoreboard
import reportes

#Tamaño de la ventana
ALTO = 35
ANCHO = 100
TIMEOUT = 300
USUARIOACTIVO = ""
PUNTUACION = 0

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
puntuaciones = scoreboard.colapuntuacion(window)

while True:
    event = window.getch()

    if event == 54:
        break
    else:
        if event == 49 and not USUARIOACTIVO:
            USUARIOACTIVO = usuarios.mostrarusuarios()
            if USUARIOACTIVO:
                pantallajuego = juego.juego(window, USUARIOACTIVO, TIMEOUT, PUNTUACION)
                PUNTUACION = pantallajuego.get_score()
                #print(PUNTUACION)
                puntuaciones.Queue(USUARIOACTIVO, PUNTUACION)
                if puntuaciones.size() > 10:
                    puntuaciones.Unqueued()
                window.clear()
                window.border(0)
                menusnake.pintarmenu()
        else:
            if event == 49 and USUARIOACTIVO:
                pantallajuego = juego.juego(window, USUARIOACTIVO, TIMEOUT, PUNTUACION)
                PUNTUACION = pantallajuego.get_score()
                #print(PUNTUACION)
                puntuaciones.Queue(USUARIOACTIVO, PUNTUACION)
                if puntuaciones.size() > 10:
                    puntuaciones.Unqueued()
                window.clear()
                window.border(0)
                menusnake.pintarmenu()
            else:
                if event == 50:
                    puntuaciones.mostrarpuntuaciones()
                    window.clear()
                    window.border(0)
                    menusnake.pintarmenu()
                else:
                    if event == 51:
                        USUARIOACTIVO = usuarios.mostrarusuarios()
                        window.clear()
                        window.border(0)
                        menusnake.pintarmenu()
                    else:
                        if event == 52:
                            window.clear()
                            window.border(0)
                            repo = reportes.reportes(window)
                            repo.pantallaopcionreportes(puntuaciones.get_cola(), usuarios.get_inicio(), usuarios.get_fin())
                            window.clear()
                            window.border(0)
                            menusnake.pintarmenu()
                        else:
                            if event == 53:
                                window.clear()
                                window.border(0)
                                usuarios.carga_masiva()
                                window.clear()
                                window.border(0)
                                menusnake.pintarmenu()
    
curses.endwin()