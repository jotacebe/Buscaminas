###########################################################################################################
#     COSAS PENDIENTES DE HACER
#	    - Terminar la ventana de Ayuda
#	    - Hacer la ventana Acerca de...
#       - Terminar el boton Nuevo
#	    - Añadir mensajes para cuando se gana o se pierde.
#       - Documentar el código.
#       - Hacer que el tamaño de la ventana y los elementos de la interfaz se adapten al tamaño del tablero.  
###########################################################################################################

from tkinter import *
from tkinter import messagebox as msg
from random import randint

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Buscaminas")

botonNormal = PhotoImage(file="proyectos/buscaminas/img/botonNormal.gif") #1
bandera = PhotoImage(file="proyectos/buscaminas/img/bandera.gif") #2
bombaNormal = PhotoImage(file="proyectos/buscaminas/img/bombaNormal.gif")
bombaError = PhotoImage(file="proyectos/buscaminas/img/bombaError.gif")
bombaExplota = PhotoImage(file="proyectos/buscaminas/img/bombaExplota.gif") #5
bombaFantasma = PhotoImage(file="proyectos/buscaminas/img/bombaFantasma.gif")
bombaFondo = PhotoImage(file="proyectos/buscaminas/img/bombaFondo.gif")
numero1 = PhotoImage(file="proyectos/buscaminas/img/numero1.gif")
numero2 = PhotoImage(file="proyectos/buscaminas/img/numero2.gif")
numero3 = PhotoImage(file="proyectos/buscaminas/img/numero3.gif") #10
numero4 = PhotoImage(file="proyectos/buscaminas/img/numero4.gif")
numero5 = PhotoImage(file="proyectos/buscaminas/img/numero5.gif")
numero6 = PhotoImage(file="proyectos/buscaminas/img/numero6.gif")
numero7 = PhotoImage(file="proyectos/buscaminas/img/numero7.gif")
numero8 = PhotoImage(file="proyectos/buscaminas/img/numero8.gif") #15
botonDeshabilitado = PhotoImage(file="proyectos/buscaminas/img/botonDeshabilitado.gif")
banderaDeshabilitada = PhotoImage(file="proyectos/buscaminas/img/banderaDeshabilitada.gif")
botonPista = PhotoImage(file="proyectos/buscaminas/img/botonPista.gif") #18
bombilla = PhotoImage(file="proyectos/buscaminas/img/bombilla.gif")
gatoBase = PhotoImage(file="proyectos/buscaminas/img/botonNormalGato.gif") #20
gatoNormal = PhotoImage(file="proyectos/buscaminas/img/gatoNormal.gif")
gatoError = PhotoImage(file="proyectos/buscaminas/img/gatoError.gif")
gatoExplota = PhotoImage(file="proyectos/buscaminas/img/gatoExplota.gif")
gatoFantasma = PhotoImage(file="proyectos/buscaminas/img/gatoFantasma.gif") #24
banderaGato = PhotoImage(file="proyectos/buscaminas/img/banderaGato.gif") #25
gatoFondo = PhotoImage(file="proyectos/buscaminas/img/gatoFondo.gif")
florBase = PhotoImage(file="proyectos/buscaminas/img/botonNormalFlor.gif") #27
florNormal = PhotoImage(file="proyectos/buscaminas/img/florNormal.gif")
florError = PhotoImage(file="proyectos/buscaminas/img/florError.gif")
florExplota = PhotoImage(file="proyectos/buscaminas/img/florExplota.gif")
florFantasma = PhotoImage(file="proyectos/buscaminas/img/florFantasma.gif") #31
florFondo = PhotoImage(file="proyectos/buscaminas/img/florFondo.gif")
banderaFlor = PhotoImage(file="proyectos/buscaminas/img/banderaFlor.gif") #33

listaMinas = []
listaBotones = []
listaAdyacentes = []
listaNumeros = ["pyimage8", "pyimage9", "pyimage10", "pyimage11", "pyimage12", "pyimage13", "pyimage14", "pyimage15"]
listaBanderas = ["pyimage2", "pyimage25", "pyimage33"]
listaFondo = ["pyimage1", "pyimage20", "pyimage27"]
listaPistas = ["pyimage6", "pyimage24", "pyimage31"]
listaIconos = ["pyimage3", "pyimage21", "pyimage28"]
listaExplota = ["pyimage5", "pyimage23", "pyimage30"]
listaError = ["pyimage4", "pyimage22", "pyimage29"]

opcion = IntVar()
opImagen = IntVar()
opImagen.set(1)
menuAdyacentes = BooleanVar()
menuAdyacentes.set(False)
vidas = IntVar()
vidas.set(4)
tiempoIniciado = BooleanVar()
tiempoIniciado.set(False)
primeraCasilla = BooleanVar()
primeraCasilla.set(True)

personalizado = []
tamañoPersonalizado = [3, 3, 0]

marcoBotones = Frame(ventana)
marcoBotones.place(x=20, y=60)
marcoBotones.config(border=3, bg="#DDDDDD", relief=RIDGE)

contadorBanderas = Label(ventana, font=("Sans Sherif", 14), image=bombaFondo, compound=LEFT)
contadorBanderas.place(x=20, y=20)

pistas = Label(ventana, font=("Sans Sherif", 14), image=bombilla, compound=LEFT)
pistas.place(x=220, y=20)

def cambiarImagen():
    if opImagen.get() == 1:
        contadorBanderas.config(image=bombaFondo)
        for i in range(len(listaBotones)):
            if listaBotones[i].cget("image") in listaFondo:
                listaBotones[i].config(image=botonNormal)
            elif listaBotones[i].cget("image") in listaBanderas:
                listaBotones[i].config(image=bandera)
            elif listaBotones[i].cget("image") in listaIconos:
                listaBotones[i].config(image=bombaNormal)
            elif listaBotones[i].cget("image") in listaExplota:
                listaBotones[i].config(image=bombaExplota)
            elif listaBotones[i].cget("image") in listaError:
                listaBotones[i].config(image=bombaError)
    if opImagen.get() == 2:
        contadorBanderas.config(image=gatoFondo)
        for i in range(len(listaBotones)):
            if listaBotones[i].cget("image") in listaFondo:
                listaBotones[i].config(image=gatoBase)
            elif listaBotones[i].cget("image") in listaBanderas:
                listaBotones[i].config(image=banderaGato)
            elif listaBotones[i].cget("image") in listaIconos:
                listaBotones[i].config(image=gatoNormal)
            elif listaBotones[i].cget("image") in listaExplota:
                listaBotones[i].config(image=gatoExplota)
            elif listaBotones[i].cget("image") in listaError:
                listaBotones[i].config(image=gatoError)
    if opImagen.get() == 3:
        contadorBanderas.config(image=florFondo)
        for i in range(len(listaBotones)):
            if listaBotones[i].cget("image") in listaFondo:
                listaBotones[i].config(image=florBase)
            elif listaBotones[i].cget("image") in listaBanderas:
                listaBotones[i].config(image=banderaFlor)
            elif listaBotones[i].cget("image") in listaIconos:
                listaBotones[i].config(image=florNormal)
            elif listaBotones[i].cget("image") in listaExplota:
                listaBotones[i].config(image=florExplota)
            elif listaBotones[i].cget("image") in listaError:
                listaBotones[i].config(image=florError)

def dificultadFacil():
    xmax=10
    ymax=10
    tamaño = 100 
    minasMaximo = 10
    ventana.geometry("300x350")    
    opcion.set(1)
    vidas.set(4)
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)
    contadorBanderas.config(text=str(minasMaximo))
    pistas.config(text=vidas.get())

def dificultadMedia():
    xmax=15
    ymax=15
    tamaño = 225 
    minasMaximo = 40
    opcion.set(2) 
    vidas.set(5)
    ventana.geometry("430x500")
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)
    contadorBanderas.config(text=str(minasMaximo))
    pistas.config(text=vidas.get())

def dificultadDificil():
    xmax=15 
    ymax=30 
    tamaño = 450
    minasMaximo = 100
    opcion.set(3)
    vidas.set(8)
    ventana.geometry("800x500")
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)
    contadorBanderas.config(text=str(minasMaximo))
    pistas.config(text=vidas.get())

def dificultadExtrema():
    xmax=25 
    ymax=25 
    tamaño = 625 
    minasMaximo = 200 
    opcion.set(4) 
    vidas.set(11)
    ventana.geometry("680x710")
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)
    contadorBanderas.config(text=str(minasMaximo))
    pistas.config(text=vidas.get())

def dificultadPersonalizada(x, y, t, m):
    xmax = x
    ymax = y
    tamaño = t
    minasMaximo = m
    vidas.set(5)
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)
    contadorBanderas.config(text=str(minasMaximo))
    pistas.config(text=vidas.get())

def personalizar():
    personalizar = Toplevel(ventana)
    personalizar.resizable(False, False)
    personalizar.title("Personalizar tablero")
    personalizar.geometry("500x200")
    personalizar.attributes("-toolwindow", True, "-topmost", True)

    marco = Frame(personalizar)
    marco.place(x=20, y=20)

    textoProporcion = Label(personalizar)
    textoProporcion.place(x=20, y=120)

    primeraCasilla.set(True)
    
    def valor(e):
        tamañoPersonalizado[0] = cuadrosVertical.get()
        tamañoPersonalizado[1] = cuadrosHorizontal.get()
        tamañoPersonalizado[2] = minas.get()
        textoVertical.config(text=cuadrosVertical.get())
        textoHorizontal.config(text=cuadrosHorizontal.get())
        textoMinas.config(text=minas.get())
        minas.config(to_=tamañoPersonalizado[0]*tamañoPersonalizado[1]-1)
        proporcion = float(minas.get() / (cuadrosVertical.get() * cuadrosHorizontal.get()))
        textoProporcion.config(text="La proporción actual es de {:.3f} minas por casilla.".format(proporcion))
       
    texto1 = Label(marco, text="Cuadros en vertical: ", width=17, anchor="e", justify=LEFT).grid(row=0, column=0)
    texto2 = Label(marco, text="Cuadros en horizontal: ", width=17, anchor="e", justify=LEFT).grid(row=1, column=0)
    texto3 = Label(marco, text="Número de minas: ", width=17, anchor="e", justify=LEFT).grid(row=2, column=0)
      
    cuadrosVertical = Scale(marco, from_=3, to_=20, resolution=1, orient="horizontal", width=18, length=300, showvalue=False, command=valor)
    cuadrosVertical.grid(row=0, column=1)
    cuadrosHorizontal = Scale(marco, from_=3, to_=50, resolution=1, orient="horizontal", width=18, length=300, showvalue=False, command=valor)
    cuadrosHorizontal.grid(row=1, column=1)
    minas = Scale(marco, from_=1, to_=tamañoPersonalizado[0]*tamañoPersonalizado[1], resolution=1, orient="horizontal", width=18, length=300, showvalue=False, command=valor)
    minas.grid(row=2, column=1)

    cuadrosVertical.set(tamañoPersonalizado[0])
    cuadrosHorizontal.set(tamañoPersonalizado[1])
    minas.set(tamañoPersonalizado[2])
 
    textoVertical = Label(marco, text="3", width=3, anchor="e", justify=LEFT, bg="#CCCCCC", bd=1, relief=SUNKEN)
    textoVertical.grid(row=0, column=3)
    textoHorizontal = Label(marco, text="3", width=3, anchor="e", justify=LEFT, bg="#CCCCCC", bd=1, relief=SUNKEN)
    textoHorizontal.grid(row=1, column=3)
    textoMinas = Label(marco, text="1", width=3, anchor="e", justify=LEFT, bg="#CCCCCC", bd=1, relief=SUNKEN)
    textoMinas.grid(row=2, column=3)
    
    def enviar():
        personalizado.clear()
        personalizado.append(cuadrosVertical.get())
        personalizado.append(cuadrosHorizontal.get())
        personalizado.append(cuadrosHorizontal.get()*cuadrosVertical.get())
        personalizado.append(minas.get())
        dificultadPersonalizada(personalizado[0], personalizado[1], personalizado[2], personalizado[3])
        personalizar.destroy()

    confirmar = Button(personalizar, text="Aceptar", command=lambda: enviar())
    confirmar.place(x=425, y=140)

def imagenAdyacentes(minas):
    numeroBandera = None
    if minas == 1:
        numeroBandera = numero1
    elif minas == 2:
        numeroBandera = numero2
    elif minas == 3:
        numeroBandera = numero3
    elif minas == 4:
        numeroBandera = numero4
    elif minas == 5:
        numeroBandera = numero5
    elif minas == 6:
        numeroBandera = numero6
    elif minas == 7:
        numeroBandera = numero7
    elif minas == 8:
        numeroBandera = numero8
    return numeroBandera

def contarBanderas(coord, xmax, ymax):
    banderas = 0
    adyacentes = calcularAdyacentes(coord, xmax, ymax)
    for i in adyacentes:
        if listaBotones[i].cget("image") in listaBanderas: 
            banderas += 1
    return banderas

def verAdyacentes(e, coord, xmax, ymax):
    if menuAdyacentes.get() == True:
        listaAdyacentes.clear()
        adyacentes = calcularAdyacentes(coord, xmax, ymax)   
        for i in adyacentes:
            if listaBotones[i].cget("image") in listaFondo or listaBotones[i].cget("image") in listaBanderas:
                listaAdyacentes.append(listaBotones[i])
                if listaBotones[i].cget("image") in listaFondo:
                    listaBotones[i].config(image=botonPista)

def ocultarAdyacentes(e, coord, xmax, ymax, tamaño, minasMaximo):
    minas = contarMinas(coord, xmax, ymax)
    banderas = contarBanderas(coord, xmax, ymax)
    adyacentes = calcularAdyacentes(coord, xmax, ymax)
    for i in adyacentes:
        if listaBotones[i].cget("image") == "pyimage18":
            if opImagen.get() == 1:
                listaBotones[i].config(image=botonNormal)
            elif opImagen.get() == 2:
                listaBotones[i].config(image=gatoBase)
            elif opImagen.get() == 3:
                listaBotones[i].config(image=florBase)
            if minas == banderas:
                comprobarMinas(i, xmax, ymax, tamaño, minasMaximo)
                 
def revelarTablero():
    for i in range(len(listaBotones)):
        if listaMinas[i] == 1 and listaBotones[i].cget("image") in listaFondo:
            if opImagen.get() == 1:
                listaBotones[i].config(image=bombaNormal)
            elif opImagen.get() == 2:
                listaBotones[i].config(image=gatoNormal)
            elif opImagen.get() == 3:
                listaBotones[i].config(image=florNormal)
            listaBotones[i].unbind("<Button-1>")
        elif listaMinas[i] == 1 and listaBotones[i].cget("image") in listaBanderas:
            listaBotones[i].config(image=banderaDeshabilitada)
            listaBotones[i].unbind("<Button-1>")
            listaBotones[i].unbind("<Button-3>")
        elif listaMinas[i] == 0 and listaBotones[i].cget("image") in listaFondo:
            listaBotones[i].config(image=botonDeshabilitado)
            listaBotones[i].unbind("<Button-1>")
        elif listaMinas[i] == 0 and  listaBotones[i].cget("image") in listaBanderas:
            if opImagen.get() == 1:
                listaBotones[i].config(image=bombaError)
            elif opImagen.get() == 2:
                listaBotones[i].config(image=gatoError)
            elif opImagen.get() == 3:
                listaBotones[i].config(image=florError)
            listaBotones[i].unbind("<Button-1>")

def ayuda():
    ventanaAyuda = Toplevel(ventana)
    ventanaAyuda.resizable = False
    ventanaAyuda.geometry("400x400")
    ventanaAyuda.title("Ayuda")
    ventanaAyuda.attributes("-topmost", True)

    titulo = Label(ventanaAyuda, text="Cómo jugar al buscaminas.")
    titulo.place(x=20, y=20)
                        
def menúOpciones():
    menuPrincipal = Menu(ventana, tearoff=0)
    ventana.config(menu=menuPrincipal)

    menuJuego = Menu(menuPrincipal, tearoff=0)
    menuOpciones = Menu(menuPrincipal, tearoff=0)
    menuAyuda = Menu(menuPrincipal, tearoff=0)
    menuDificultad = Menu(menuJuego, tearoff=0)
    menuImagenes = Menu(menuJuego, tearoff=0)

    menuPrincipal.add_cascade(label="Juego", menu=menuJuego)
    menuPrincipal.add_cascade(label="Opciones", menu=menuOpciones)
    menuPrincipal.add_cascade(label="Ayuda", menu=menuAyuda)

    menuDificultad.add_radiobutton(label="Principiante", variable=opcion, value=1, command=dificultadFacil, accelerator="CTRL + 1")
    menuDificultad.add_radiobutton(label="Intermedio", variable=opcion, value=2, command=dificultadMedia, accelerator="CTRL + 2")
    menuDificultad.add_radiobutton(label="Difícil", variable=opcion, value=3, command=dificultadDificil, accelerator="CTRL + 3")
    menuDificultad.add_radiobutton(label="Extremo", variable=opcion, value=4, command=dificultadExtrema, accelerator="CTRL + 4")
    menuDificultad.add_separator()
    menuDificultad.add_radiobutton(label="Personalizado...", variable=opcion, value=5, command=personalizar)

    menuImagenes.add_radiobutton(label="Minas", variable=opImagen, value=1, command=lambda: cambiarImagen())
    menuImagenes.add_radiobutton(label="Gatos", variable=opImagen, value=2, command=lambda: cambiarImagen())
    menuImagenes.add_radiobutton(label="Flores", variable=opImagen, value=3, command=lambda: cambiarImagen())

    menuJuego.add_command(label="Nuevo", accelerator="F2", command=lambda: nuevo())
    menuJuego.add_cascade(label="Dificultad", menu=menuDificultad)
    menuJuego.add_separator()
    menuJuego.add_command(label="Salir", command=lambda: ventana.quit())

    menuOpciones.add_checkbutton(label="Adyacentes", onvalue=1, offvalue=0, variable=menuAdyacentes)
    menuOpciones.add_cascade(label="Imágenes", menu=menuImagenes)
    menuOpciones.add_command(label="Pista", accelerator="F3", command=lambda: solucion())
    menuOpciones.add_command(label="Ver solución", command=lambda: revelarTablero(), accelerator="CTRL + R")

    menuAyuda.add_command(label="Ayuda", command=ayuda, accelerator="F1")
    menuAyuda.add_command(label="Acerca de...")

def nuevo():
    primeraCasilla.set(True)
    if opcion.get() == 1:
        dificultadFacil()
    elif opcion.get() == 2:
        dificultadMedia()
    elif opcion.get() == 3:
        dificultadDificil()
    elif opcion.get() == 4:
        dificultadExtrema()
    else:
        dificultadPersonalizada(personalizado[0], personalizado[1], personalizado[2], personalizado[3])
    reiniciar.place(x=-50, y=-50)
    
def calcularAdyacentes(coord, xmax, ymax):   
    adyacentes = [] 
    #Esquina superior izquierda:
    if coord == 0:
        adyacentes = [coord + 1, coord + ymax, coord + ymax + 1]
    #Esquina superior derecha:
    elif coord == ymax - 1:
        adyacentes = [coord - 1, coord + ymax, coord + ymax - 1]
    #Esquina inferior izquierda:
    elif coord == xmax * ymax - ymax:
        adyacentes = [coord + 1, coord - ymax, coord - ymax + 1]
    #Esquina inferior derecha:
    elif coord == xmax * ymax - 1:
        adyacentes = [coord - 1, coord - ymax, coord - ymax - 1]
    #Borde izquierdo
    elif 0 < coord < xmax * ymax - ymax and coord % ymax == 0:
        adyacentes = [coord - ymax, coord - ymax + 1, coord + 1, coord + ymax, coord + ymax + 1]
    #Borde superior:
    elif 0 < coord < ymax - 1:
        adyacentes = [coord - 1, coord + 1, coord + ymax - 1, coord + ymax, coord + ymax + 1]
    #Borde inferior
    elif xmax * ymax - ymax < coord < xmax * ymax - 1:
        adyacentes = [coord - 1, coord + 1, coord - ymax - 1, coord - ymax, coord - ymax + 1]
    #Borde derecho:
    elif ymax - 1 < coord < xmax * ymax - 1 and (coord + 1) % ymax == 0:
        adyacentes = [coord - ymax, coord - ymax - 1, coord - 1, coord + ymax - 1, coord + ymax]
    else:
        adyacentes = [coord - ymax - 1, coord - ymax, coord - ymax + 1, coord - 1, coord + 1, coord + ymax - 1, coord + ymax, coord + ymax + 1]

    return adyacentes

def contarMinas(coord, xmax, ymax):
    minas = 0
    adyacentes = calcularAdyacentes(coord, xmax, ymax)
    for i in adyacentes:
        i = int(i)
        if listaMinas[i] == 1:
            minas += 1
    return minas

def comprobarMinas(coord, xmax, ymax, tamaño, minasMaximo):
    if 0 <= coord <= tamaño-1 and listaBotones[coord].bind("<Button-1>"):
        if listaMinas[coord] == 1:
            if primeraCasilla.get() == True:
                control = True
                while control:
                    minaX = randint(0,xmax-1) 
                    minaY = randint(0,ymax-1) 
                    posicion = ymax*minaX + minaY
                    if listaMinas[posicion] != 1:
                        listaMinas[posicion] = 1
                        control = False
                listaMinas[coord] = 0
                comprobarMinas(coord, xmax, ymax, tamaño, minasMaximo)
            else:
                perder(coord)
        else:
            primeraCasilla.set(False)
            listaBotones[coord].config(image=botonDeshabilitado)
            listaBotones[coord].unbind("<Button-1>")
            minasAdyacentes = contarMinas(coord, xmax, ymax)
            numero = imagenAdyacentes(minasAdyacentes)
            if minasAdyacentes > 0:
                listaBotones[coord].config(image=numero)
            else:                    
                adyacentes = calcularAdyacentes(coord, xmax, ymax)
                for i in range(len(adyacentes)):
                    comprobarMinas(adyacentes[i], xmax, ymax, tamaño, minasMaximo)                
            if comprobarSiGanar(minasMaximo, tamaño):
                ganar()
            if listaBotones[coord].cget("image") in listaNumeros:
                listaBotones[coord].bind("<Button-1>", lambda e, c=coord, x=xmax, y=ymax: verAdyacentes(e, c, x, y))
                listaBotones[coord].bind("<ButtonRelease-1>", lambda e, c=coord, x=xmax, y=ymax, t=tamaño, m=minasMaximo: ocultarAdyacentes(e, c, x, y, t, m))

def perder(coord):
    if opImagen.get() == 1:
        listaBotones[coord].config(image=bombaExplota)
    elif opImagen.get() == 2:
        listaBotones[coord].config(image=gatoExplota)
    elif opImagen.get() == 3:
        listaBotones[coord].config(image=florExplota)
    listaBotones[coord].unbind("<Button-1>")
    revelarTablero()
    #msg.showinfo(message="Has perdido")
    reiniciar.place(x=120, y=20)

def ganar():
    revelarTablero()
    #msg.showinfo(message="Has ganado")
    reiniciar.place(x=50, y=20)

def colocarMinas(xmax, ymax, tamaño, minasMaximo):
    listaMinas.clear()
    num = 0
    for i in range(tamaño):
        listaMinas.append(0)

    while num < minasMaximo:
        minaX = randint(0,xmax-1) 
        minaY = randint(0,ymax-1) 
        posicion = ymax*minaX + minaY
        if listaMinas[posicion] != 1:
            listaMinas[posicion] = 1
            num += 1
            
def ponerBandera(e, coord, xmax, ymax, tamaño, minasMaximo):
    if listaBotones[coord].cget("image") in listaBanderas:
        if opImagen.get() == 1:
            listaBotones[coord].config(image=botonNormal)
        elif opImagen.get() == 2:
            listaBotones[coord].config(image=gatoBase)
        elif opImagen.get() == 3:
            listaBotones[coord].config(image=florBase)
        contadorBanderas.config(text=str(int(contadorBanderas.cget("text"))+1))
        listaBotones[coord].bind("<Button-1>", lambda e, c=coord, t=tamaño, x=xmax, y=ymax, m=minasMaximo: comprobarMinas(c, x, y, t, m))
    elif listaBotones[coord].cget("image") in listaFondo:
        if opImagen.get() == 1:
            listaBotones[coord].config(image=bandera)
        elif opImagen.get() == 2:
            listaBotones[coord].config(image=banderaGato)
        elif opImagen.get() == 3:
            listaBotones[coord].config(image=banderaFlor)
        contadorBanderas.config(text=str(int(contadorBanderas.cget("text"))-1))
        listaBotones[coord].unbind("<Button-1>")
            
def comprobarSiGanar(minasMaximo, tamaño):
    contarNormal = 0
    mina = 0
    for i in range(tamaño):
        if listaBotones[i].cget("image") in listaFondo or listaBotones[i].cget("image") in listaBanderas:
            contarNormal += 1
    if contarNormal == minasMaximo:
        for i in range(tamaño):
            if listaBotones[i].cget("image") in listaFondo or listaBotones[i].cget("image") in listaBanderas and listaMinas[i] == 1:
                mina += 1
    if mina == minasMaximo:          
        return True
    else: 
        return False

def dibujarElementos(xmax, ymax, tamaño, minasMaximo):
    if opImagen.get() == 1:
        fondo = botonNormal
    elif opImagen.get() == 2:
        fondo = gatoBase
    elif opImagen.get() == 3:
        fondo = florBase
    for i in listaBotones:
        i.destroy()
    listaBotones.clear()
    i = 0
    while i < tamaño:     
        for j in range(xmax):
            for k in range(ymax):
                nombreBoton = str(i)
                texto = str(ymax*j + k)
                nombreBoton = Label(marcoBotones, image=fondo, border=0)  
                nombreBoton.grid(row=j, column=k)
                nombreBoton.bind("<Button-3>", lambda e, c=int(texto), t=tamaño, x=xmax, y=ymax, m=minasMaximo: ponerBandera(e, c, x, y, t, m))
                nombreBoton.bind("<Button-1>", lambda e, c=int(texto), t=tamaño, x=xmax, y=ymax, m=minasMaximo: comprobarMinas(c, x, y, t, m))
                listaBotones.append(nombreBoton)
                i += 1 
    colocarMinas(xmax, ymax, tamaño, minasMaximo)

def solucion():
    for i in range(len(listaMinas)):
        if listaMinas[i] == 1 and listaBotones[i].cget("image") in listaFondo:
            if opImagen.get() == 1:
                listaBotones[i].config(image=bombaFantasma)
            elif opImagen.get() == 2:
                listaBotones[i].config(image=gatoFantasma)
            elif opImagen.get() == 3:
                listaBotones[i].config(image=florFantasma)           
    ventana.after(100, ocultarSolucion)    

def ocultarSolucion():
    for i in range(len(listaMinas)):
        if listaMinas[i] == 1 and listaBotones[i].cget("image") in listaPistas:
            if opImagen.get() == 1:
                listaBotones[i].config(image=botonNormal)
            elif opImagen.get() == 2:
                listaBotones[i].config(image=gatoBase)
            elif opImagen.get() == 3:
                listaBotones[i].config(image=florBase)
    if vidas.get()==0:
        revelarTablero()
    vidas.set(vidas.get()-1)
    if vidas.get() >= 0:
        pistas.config(text=vidas.get())

reiniciar = Button(ventana, text="Nuevo", command=nuevo)
reiniciar.place(x=-200, y=-200)

dificultadFacil()
menúOpciones()

ventana.bind("<F1>", lambda e: ayuda())
ventana.bind("<F2>", lambda e: nuevo())
ventana.bind("<F3>", lambda e: solucion())
ventana.bind("<Control-Key-1>", lambda e: dificultadFacil())
ventana.bind("<Control-Key-2>", lambda e: dificultadMedia())
ventana.bind("<Control-Key-3>", lambda e: dificultadDificil())
ventana.bind("<Control-Key-4>", lambda e: dificultadExtrema())
ventana.bind("<Control-Key-r>", lambda e: revelarTablero())
ventana.bind("<Control-Key-R>", lambda e: revelarTablero())

ventana.mainloop()

