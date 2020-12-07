#################################################################################################
#     COSAS PENDIENTES DE HACER
#	- Opción del menú Juego - Pausa
#	- Opción del menú Opciones - Interrogantes
#	- Opción del menú Ayuda - Ayuda
#	- Opción del menú Ayuda - Acerca de...
#	- Habilitar contador de tiempo.
#	- Añadir a la ventana información sobre el tiempo y las banderas.
#	- Añadir a la ventana boton para Iniciar/Reiniciar
#	- Añadir lista de mejores resultados.
#   - Añadir mensajes para cuando se gana o se pierde.
#   - Documentar el código.
#   - Añadir accesos para el teclado más opciones del menú.
#   - Añadir la posibilidad de cambiar las imágenes.
#   - Hacer que la primera casilla que se destape no tenga mina.
#   - Hacer que mientras se esté pulsando sobre una casilla destapada, se marquen las que la rodean 
#     sin destapar.
#   - Hacer que el tamaño de la ventana y los elementos de la interfaz se adapten al tamaño del 
#     tablero.
#   - Hacer que la ventana de personalizar sea modal.
#   - Hacer que cuando se establezca un tamaño personalizado de tablero, al volver a entrar en la
#     ventana de personalizar muestre los valore indicados anteriormente.
#################################################################################################

from tkinter import *
from tkinter import messagebox as msg
from random import randint

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Buscaminas")
#ventana.resizable(False, False)

marcoBotones = Frame(ventana)
marcoBotones.place(x=20, y=60)
marcoBotones.config(border=3, bg="#999999")

botonNormal = PhotoImage(file="proyectos/buscaminas/img/botonNormal.gif")
bandera = PhotoImage(file="proyectos/buscaminas/img/bandera.gif")
bombaNormal = PhotoImage(file="proyectos/buscaminas/img/bombaNormal.gif")
bombaError = PhotoImage(file="proyectos/buscaminas/img/bombaError.gif")
bombaExplota = PhotoImage(file="proyectos/buscaminas/img/bombaExplota.gif")
numero1 = PhotoImage(file="proyectos/buscaminas/img/numero1.gif")
numero2 = PhotoImage(file="proyectos/buscaminas/img/numero2.gif")
numero3 = PhotoImage(file="proyectos/buscaminas/img/numero3.gif")
numero4 = PhotoImage(file="proyectos/buscaminas/img/numero4.gif")
numero5 = PhotoImage(file="proyectos/buscaminas/img/numero5.gif")
numero6 = PhotoImage(file="proyectos/buscaminas/img/numero6.gif")
numero7 = PhotoImage(file="proyectos/buscaminas/img/numero7.gif")
numero8 = PhotoImage(file="proyectos/buscaminas/img/numero8.gif")
botonDeshabilitado = PhotoImage(file="proyectos/buscaminas/img/botonDeshabilitado.gif")
banderaDeshabilitada = PhotoImage(file="proyectos/buscaminas/img/banderaDeshabilitada.gif")
banderaPista = PhotoImage(file="proyectos/buscaminas/img/banderaPistas.gif")
botonDeshabilitado2 = PhotoImage(file="proyectos/buscaminas/img/botonDeshabilitado.gif")
bombaFantasma = PhotoImage(file="proyectos/buscaminas/img/bombaFantasma.gif")

listaMinas = []
listaBotones = []
listaAdyacentes = []

opcion = IntVar()
opcion.set(1)

personalizado = []

def dificultadFacil():
    xmax=10 #límite de filas de botones
    ymax=10 #límite de columnas de botones
    tamaño = 100 #número de botones
    minasMaximo = 10 #número de minas iniciales --> 1/10 = 10 %
    #tamañoVentana = str(ymax*30) + "x" + str(xmax*30 + 50)
    ventana.geometry("300x350")
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)

def dificultadMedia():
    xmax=15 #límite de filas de botones
    ymax=15 #límite de columnas de botones
    tamaño = 225 #número de botones
    minasMaximo = 40 #número de minas iniciales
    #tamañoVentana = str(ymax*30) + "x" + str(xmax*30 + 50)
    ventana.geometry("430x500")
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)

def dificultadDificil():
    xmax=15 #límite de filas de botones
    ymax=30 #límite de columnas de botones
    tamaño = 450 #número de botones
    minasMaximo = 100 #número de minas iniciales
    #tamañoVentana = str(ymax*30) + "x" + str(xmax*30 + 50)
    ventana.geometry("800x500")
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)

def dificultadExtrema():
    xmax=25 #límite de filas de botones
    ymax=25 #límite de columnas de botones
    tamaño = 625 #número de botones
    minasMaximo = 250 #número de minas iniciales 
    #tamañoVentana = str(ymax*30) + "x" + str(xmax*30 + 50)
    ventana.geometry("680x710")
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)

def dificultadPersonalizada(x, y, t, m):
    xmax = x
    ymax = y
    tamaño = t
    minasMaximo = m
    dibujarElementos(xmax, ymax, tamaño, minasMaximo)

def personalizar():
    personalizar = Tk()
    personalizar.resizable(False, False)
    personalizar.title("Personalizar tablero")
    personalizar.geometry("500x200")

    marco = Frame(personalizar)
    marco.place(x=20, y=20)

    def valor(e):
        textoVertical.config(text=cuadrosVertical.get())
        textoHorizontal.config(text=cuadrosHorizontal.get())
        textoMinas.config(text=minas.get())
        minasMaximo = cuadrosHorizontal.get()*cuadrosVertical.get()
        minas.config(to_=minasMaximo)
           
    texto1 = Label(marco, text="Cuadros en vertical: ", width=17, anchor="e", justify=LEFT).grid(row=0, column=0)
    texto2 = Label(marco, text="Cuadros en horizontal: ", width=17, anchor="e", justify=LEFT).grid(row=1, column=0)
    texto3 = Label(marco, text="Número de minas: ", width=17, anchor="e", justify=LEFT).grid(row=2, column=0)
      
    cuadrosVertical = Scale(marco, from_=3, to_=20, resolution=1, orient="horizontal", width=18, length=300, showvalue=False, command=valor)
    cuadrosVertical.grid(row=0, column=1)
    cuadrosHorizontal = Scale(marco, from_=3, to_=50, resolution=1, orient="horizontal", width=18, length=300, showvalue=False, command=valor)
    cuadrosHorizontal.grid(row=1, column=1)
    minas = Scale(marco, from_=1, to_=cuadrosHorizontal.get()*cuadrosVertical.get(), resolution=1, orient="horizontal", width=18, length=300, showvalue=False, command=valor)
    minas.grid(row=2, column=1)
   
    textoVertical = Label(marco,text="3", width=3, anchor="e", justify=LEFT, bg="#CCCCCC", bd=1, relief=SUNKEN)
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
        if listaBotones[i].cget("image") == "pyimage2":
            banderas += 1
    return banderas

def verAdyacentes(e, coord, xmax, ymax):
    listaAdyacentes.clear()
    adyacentes = calcularAdyacentes(coord, xmax, ymax)   
    for i in adyacentes:
        if listaBotones[i].cget("image")=="pyimage1" or listaBotones[i].cget("image")=="pyimage2":
            listaAdyacentes.append(listaBotones[i])
            if listaBotones[i].cget("image") == "pyimage1":
                listaBotones[i].config(image=botonDeshabilitado2)

def ocultarAdyacentes(e, coord, xmax, ymax, tamaño, minasMaximo):
    minas = contarMinas(coord, xmax, ymax)
    banderas = contarBanderas(coord, xmax, ymax)
    adyacentes = calcularAdyacentes(coord, xmax, ymax)
    for i in adyacentes:
        if listaBotones[i].cget("image") == "pyimage17":
            listaBotones[i].config(image=botonNormal)
            if minas == banderas:
                comprobarMinas(i, xmax, ymax, tamaño, minasMaximo)
                 
def revelarTablero():
    for i in range(len(listaBotones)):
        if listaBotones[i].bind("<Button-1>"):
            if listaMinas[i] == 1 and listaBotones[i].cget("image") == "pyimage1": 
                listaBotones[i].config(image=bombaNormal)
                listaBotones[i].unbind("<Button-1>")
            elif listaMinas[i] == 1 and listaBotones[i].cget("image") == "pyimage2":
                listaBotones[i].config(image=banderaDeshabilitada)
                listaBotones[i].unbind("<Button-1>")
            elif listaMinas[i] == 0 and listaBotones[i].cget("image") == "pyimage1":
                    listaBotones[i].config(image=botonDeshabilitado)
                    listaBotones[i].unbind("<Button-1>")
            elif listaMinas[i] == 0 and  listaBotones[i].cget("image") == "pyimage2":
                listaBotones[i].config(image=bombaError)
                listaBotones[i].unbind("<Button-1>")

def pista():
    for i in range(0,len(listaBotones)):
        if listaBotones[i].bind("<Button-1>") and listaMinas[i] == 1:
            listaBotones[i].config(image=banderaPista)
            listaBotones[i].unbind("<Button-1>")    
            break

def menúOpciones():
    menuPrincipal = Menu(ventana, tearoff=0)
    ventana.config(menu=menuPrincipal)

    menuJuego = Menu(menuPrincipal, tearoff=0)
    menuOpciones = Menu(menuPrincipal, tearoff=0)
    menuAyuda = Menu(menuPrincipal, tearoff=0)
    menuDificultad = Menu(menuJuego, tearoff=0)

    menuPrincipal.add_cascade(label="Juego", menu=menuJuego)
    menuPrincipal.add_cascade(label="Opciones", menu=menuOpciones)
    menuPrincipal.add_cascade(label="Ayuda", menu=menuAyuda)

    menuDificultad.add_radiobutton(label="Principiante", variable=opcion, value=1, command=dificultadFacil)
    menuDificultad.add_radiobutton(label="Intermedio", variable=opcion, value=2, command=dificultadMedia)
    menuDificultad.add_radiobutton(label="Difícil", variable=opcion, value=3, command=dificultadDificil)
    menuDificultad.add_radiobutton(label="Extremo", variable=opcion, value=4, command=dificultadExtrema)
    menuDificultad.add_separator()
    menuDificultad.add_radiobutton(label="Personalizado...", variable=opcion, value=5, command=personalizar)

    menuJuego.add_command(label="Nuevo", accelerator="F2", command=nuevo)
    menuJuego.add_command(label="Pausa", accelerator="P")
    menuJuego.add_cascade(label="Dificultad", menu=menuDificultad)
    menuJuego.add_separator()
    menuJuego.add_command(label="Salir", command=lambda: ventana.quit())

    menuOpciones.add_checkbutton(label="Interrogantes", onvalue=1)
    menuOpciones.add_separator()
    menuOpciones.add_command(label="Pista", command=lambda: pista())
    menuOpciones.add_command(label="Ver solución", command=lambda: revelarTablero())

    menuAyuda.add_command(label="Ayuda")
    menuAyuda.add_command(label="Acerca de...")

def nuevo(e):
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
    x = coord // xmax
    y = coord % xmax
    if 0 <= coord <= tamaño-1 and listaBotones[coord].bind("<Button-1>"):
        if listaMinas[coord] == 1:
            perder(coord)
        else:
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
            if listaBotones[coord].cget("image") in ["pyimage6", "pyimage7", "pyimage8", "pyimage9", "pyimage10", "pyimage11", "pyimage12", "pyimage13"]:
                listaBotones[coord].bind("<Button-3>", lambda e, c=coord, x=xmax, y=ymax: verAdyacentes(e, c, x, y))
                listaBotones[coord].bind("<ButtonRelease-3>", lambda e, c=coord, x=xmax, y=ymax, t=tamaño, m=minasMaximo: ocultarAdyacentes(e, c, x, y, t, m))

def perder(coord):
    listaBotones[coord].config(image=bombaExplota)
    listaBotones[coord].unbind("<Button-1>")
    revelarTablero()
    #msg.showinfo(message="Has perdido")

def ganar():
    revelarTablero()
    #msg.showinfo(message="Has ganado")

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

def ponerBandera(e, coord, tamaño):
    contadorBanderas = 0
    for i in range(tamaño):
        if listaBotones[i].cget("image") == "pyimage2":
            contadorBanderas += 1
    if listaBotones[coord].bind("<Button-1>"):
        if listaBotones[coord].cget("image") == "pyimage2":
            listaBotones[coord].config(image=botonNormal)
            contadorBanderas -= 1
        elif listaBotones[coord].cget("image") == "pyimage1": 
            listaBotones[coord].config(image=bandera)
            contadorBanderas += 1 

def comprobarSiGanar(minasMaximo, tamaño):
    contarNormal = 0
    banderaCorrecta = 0
    for i in range(tamaño):
        if listaBotones[i].bind("<Button-1>"):
            contarNormal += 1
        if listaBotones[i].cget("image") == "pyimage2" or listaBotones[i].cget("image") == "pyimage2" and listaMinas[i] == 1:
            banderaCorrecta += 1
    if contarNormal == minasMaximo or banderaCorrecta == minasMaximo:
        return True
    else: 
        return False

def dibujarElementos(xmax, ymax, tamaño, minasMaximo):
    for i in listaBotones:
        i.destroy()
    listaBotones.clear()
    i = 0
    while i < tamaño:     
        for j in range(xmax):
            for k in range(ymax):
                nombreBoton = str(i)
                texto = str(ymax*j + k)
                nombreBoton = Label(marcoBotones, image=botonNormal, border=0)  
                nombreBoton.grid(row=j, column=k)
                nombreBoton.bind("<Button-3>", lambda e, coord = int(texto), tamaño=tamaño: ponerBandera(e, coord, tamaño))
                nombreBoton.bind("<Button-1>", lambda e, coord=int(texto), tamaño=tamaño, xmax=xmax, ymax=ymax, minasMaximo=minasMaximo: comprobarMinas(coord, xmax, ymax, tamaño, minasMaximo))
                listaBotones.append(nombreBoton)
                i += 1 
    colocarMinas(xmax, ymax, tamaño, minasMaximo)
    
dificultadFacil()
menúOpciones()

def solucion(e):
    for i in range(len(listaMinas)):
        if listaMinas[i] == 1:
            listaBotones[i].config(image=bombaFantasma)

ventana.bind("<F2>", nuevo)
ventana.bind("<F3>", solucion)
ventana.mainloop()
