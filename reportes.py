import curses
import pydot
import serpiente
import puntuacion
import os

class reportes:

    def __init__(self, window):
        self.window = window

    def pantallagenerarreportesnake(self, cabeza):
        self.window.addstr(16, 36, "Nombre del reporte: ")
        self.window.addstr(17, 36, "Presione Enter para guardar")
        tecla = -1
        posx = posicioninicial = 56
        auxnombre = ""
        while True:
            tecla = self.window.getch()
            if (tecla > 64 and tecla < 90) or (tecla > 96 and tecla < 123) or (tecla > 47 and tecla < 58):
                self.window.clear()
                self.window.border(0)
                self.window.addstr(16, 36, "Nombre del reporte: ")
                self.window.addstr(17, 36, "Presione Enter para guardar")
                self.window.addstr(16, posicioninicial, auxnombre)
                self.window.addstr(16, posx, chr(tecla))
                posx += 1
                auxnombre += chr(tecla)
            else:
                if tecla == 8:
                    if posx != posicioninicial:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(16, 36, "Nombre del reporte: ")
                        self.window.addstr(17, 36, "Presione Enter para guardar")
                        auxnombre = auxnombre[:-1]
                        self.window.addstr(16, posicioninicial, auxnombre)
                        posx -= 1
                else:
                    if (tecla == 459 or tecla == 10) and posx != posicioninicial:
                        break
        
        nodoaux = cabeza
        grafica = "digraph{\n"
        grafica += str("node[shape=record];\n")
        grafica += str("rankdir=LR;\n")
        control = 0
        while nodoaux:
            grafica += str("serpiente_" + str(control) + "[label=\"{<ant>|{" + str(nodoaux.caracter) + "|{(" + str(nodoaux.posicionx) + "," + str(nodoaux.posiciony) + ")}" + "}|<sig>}\"];\n")
            nodoaux = nodoaux.siguiente
            control += 1
        control = 0
        nodoaux = cabeza
        while nodoaux:
            if nodoaux.siguiente:
                grafica += str("serpiente_" + str(control) + ":sig->serpiente_" + str(control+ 1) + ":ant\n")
            
            if nodoaux.anterior:
                grafica += str("serpiente_" + str(control) + ":ant->serpiente_" + str(control - 1) + ":sig\n")
            
            nodoaux = nodoaux.siguiente
            control += 1
        grafica += str("}")
        #print(grafica)
        grafo = pydot.graph_from_dot_data(grafica)
        (g,) = grafo
        g.write_jpg(auxnombre + ".jpg")
   
    def pantallagenerarreportepunteo(self, pila):
        self.window.addstr(16, 36, "Nombre del reporte: ")
        self.window.addstr(17, 36, "Presione Enter para guardar")
        tecla = -1
        posx = posicioninicial = 56
        auxnombre = ""
        while True:
            tecla = self.window.getch()
            if (tecla > 64 and tecla < 90) or (tecla > 96 and tecla < 123) or (tecla > 47 and tecla < 58):
                self.window.clear()
                self.window.border(0)
                self.window.addstr(16, 36, "Nombre del reporte: ")
                self.window.addstr(17, 36, "Presione Enter para guardar")
                self.window.addstr(16, posicioninicial, auxnombre)
                self.window.addstr(16, posx, chr(tecla))
                posx += 1
                auxnombre += chr(tecla)
            else:
                if tecla == 8:
                    if posx != posicioninicial:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(16, 36, "Nombre del reporte: ")
                        self.window.addstr(17, 36, "Presione Enter para guardar")
                        auxnombre = auxnombre[:-1]
                        self.window.addstr(16, posicioninicial, auxnombre)
                        posx -= 1
                else:
                    if (tecla == 459 or tecla == 10) and posx != posicioninicial:
                        break
        
        nodoaux = pila
        grafica = "digraph{\n"
        grafica += str("node[shape=record];\n")
        grafica += str("pila[label=\"{")
        grafica += str("{ }")
        while nodoaux:
            grafica += str("|{(" + str(nodoaux.posicionx) + "," + str(nodoaux.posiciony) + ")}")
            nodoaux = nodoaux.anterior
        grafica += str("}\"];\n")
        grafica += str("}")
        #print(grafica)
        grafo = pydot.graph_from_dot_data(grafica)
        (g,) = grafo
        g.write_jpg(auxnombre + ".jpg")

    def pantallagenerarreportepuntuaciones(self, cola):
        self.window.addstr(16, 36, "Nombre del reporte: ")
        self.window.addstr(17, 36, "Presione Enter para guardar")
        tecla = -1
        posx = posicioninicial = 56
        auxnombre = ""
        while True:
            tecla = self.window.getch()
            if (tecla > 64 and tecla < 90) or (tecla > 96 and tecla < 123) or (tecla > 47 and tecla < 58):
                self.window.clear()
                self.window.border(0)
                self.window.addstr(16, 36, "Nombre del reporte: ")
                self.window.addstr(17, 36, "Presione Enter para guardar")
                self.window.addstr(16, posicioninicial, auxnombre)
                self.window.addstr(16, posx, chr(tecla))
                posx += 1
                auxnombre += chr(tecla)
            else:
                if tecla == 8:
                    if posx != posicioninicial:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(16, 36, "Nombre del reporte: ")
                        self.window.addstr(17, 36, "Presione Enter para guardar")
                        auxnombre = auxnombre[:-1]
                        self.window.addstr(16, posicioninicial, auxnombre)
                        posx -= 1
                else:
                    if (tecla == 459 or tecla == 10) and posx != posicioninicial:
                        break
        nodoaux = cola
        grafica = "digraph{\n"
        grafica += str("node[shape=record];\n")
        grafica += str("rankdir=LR;\n")
        control = 0
        while nodoaux:
            grafica += str("puntuacion" + str(control) + "[label=\"{<c>(" + str(nodoaux.nombre_usuario) + ","+ str(nodoaux.puntuacion) + ")" + "|<sig>}\"];\n")
            nodoaux = nodoaux.siguiente
            control += 1
        control = 0
        nodoaux = cola
        while nodoaux:
            if nodoaux.siguiente:
                grafica += str("puntuacion" + str(control) + ":sig->puntuacion" + str(control+ 1) + ":c\n")
            
            nodoaux = nodoaux.siguiente
            control += 1
        grafica += str("}")
        #print(grafica)
        grafo = pydot.graph_from_dot_data(grafica)
        (g,) = grafo
        g.write_jpg(auxnombre + ".jpg")

    def pantallagenerarreporteusuarios(self, usuario, fin):
        self.window.addstr(16, 36, "Nombre del reporte: ")
        self.window.addstr(17, 36, "Presione Enter para guardar")
        tecla = -1
        posx = posicioninicial = 56
        auxnombre = ""
        while True:
            tecla = self.window.getch()
            if (tecla > 64 and tecla < 90) or (tecla > 96 and tecla < 123) or (tecla > 47 and tecla < 58):
                self.window.clear()
                self.window.border(0)
                self.window.addstr(16, 36, "Nombre del reporte: ")
                self.window.addstr(17, 36, "Presione Enter para guardar")
                self.window.addstr(16, posicioninicial, auxnombre)
                self.window.addstr(16, posx, chr(tecla))
                posx += 1
                auxnombre += chr(tecla)
            else:
                if tecla == 8:
                    if posx != posicioninicial:
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(16, 36, "Nombre del reporte: ")
                        self.window.addstr(17, 36, "Presione Enter para guardar")
                        auxnombre = auxnombre[:-1]
                        self.window.addstr(16, posicioninicial, auxnombre)
                        posx -= 1
                else:
                    if (tecla == 459 or tecla == 10) and posx != posicioninicial:
                        break
        nodoaux = principio = usuario
        grafica = "digraph{\n"
        grafica += str("node[shape=record];\n")
        grafica += str("rankdir=LR;\n")
        if usuario:
            control = 0
            grafica += str("usuario" + str(control) + "[label=\"{<ant>|" + str(nodoaux.nombre_usuario) + "|<sig>}\"];\n")
            nodoaux = nodoaux.siguiente
            control += 1
            while nodoaux != principio:
                grafica += str("usuario" + str(control) + "[label=\"{<ant>|" + str(nodoaux.nombre_usuario) + "|<sig>}\"];\n")
                nodoaux = nodoaux.siguiente
                control += 1
            nodoaux = usuario
            control = 0
            if usuario != fin:
                #print()
                while nodoaux != fin:
                    grafica += str("usuario" + str(control) + ":sig->usuario" + str(control + 1) + ":ant\n")
                    if nodoaux != principio:
                        grafica += str("usuario" + str(control) + ":ant->usuario" + str(control - 1) + ":sig\n")
                    nodoaux = nodoaux.siguiente
                    control += 1
                grafica += str("usuario" + str(control) +":ant->usuario" + str(control - 1) + ":sig\n")
                grafica += str("usuario" + str(control) + ":sig->usuario0:ant\n")
                grafica += str("usuario0:ant->usuario" + str(control) + ":sig\n")
            else:
                grafica += str("usuario0:sig->usuario0:ant")
                grafica += str("usuario0:ant->usuario0:sig")
        grafica += str("}")
        #print(grafica)
        grafo = pydot.graph_from_dot_data(grafica)
        (g,) = grafo
        g.write_jpg(auxnombre + ".jpg")

    def pantallaopcionreportes(self, cola, usuario, fin):
        self.window.addstr(16, 37, "1 Reporte de puntuaciones")
        self.window.addstr(17, 39, "2 Reporte de usuarios")
        self.window.addstr(18, 45, "3 Regresar")
        while True:
            event = self.window.getch()

            if event == 49:
                self.window.clear()
                self.window.border(0)
                self.pantallagenerarreportepuntuaciones(cola)
                self.window.clear()
                self.window.border(0)
                self.window.addstr(16, 37, "1 Reporte de puntuaciones")
                self.window.addstr(17, 39, "2 Reporte de usuarios")
                self.window.addstr(18, 45, "3 Regresar")
            else:
                if event == 51:
                    break
                else:
                    if event == 50:
                        self.window.clear()
                        self.window.border(0)
                        self.pantallagenerarreporteusuarios(usuario, fin)
                        self.window.clear()
                        self.window.border(0)
                        self.window.addstr(16, 37, "1 Reporte de puntuaciones")
                        self.window.addstr(17, 39, "2 Reporte de usuarios")
                        self.window.addstr(18, 45, "3 Regresar")