import tkinter as tk
from tkinter import font
from administrarContactos.opcionesContactos.crearRegistrosContactos import frameCrearRegistrosContactos
from administrarContactos.opcionesContactos.editarRegistrosContactos import frameEditarRegistrosContactos
from administrarContactos.opcionesContactos.eliminarRegistrosContactos import frameEliminarRegistrosContactos
from administrarContactos.opcionesContactos.verRegistrosContactos import frameVerRegistrosContactos



class frameContactosOpciones(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #Comienzo desarrollo de la GUI
        #Desarrollo apartado bienvenida
        self.geometry("800x650")
        self.resizable(False, False)

        self.contenedorTitulo = tk.Frame(self)
        self.contenedorTitulo.place(x=0, y =0, width =800, height =100)
        self.contenedorTitulo.config( bg="#031E66")

        self.labelTitulo = tk.Label(self.contenedorTitulo, text="Administrar Contactos")
        self.labelTitulo.place(x=20, y=0, width =700, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.contenedorOpciones = tk.Frame(self)
        self.contenedorOpciones.place(x=0, y =100, width =800, height =550)
        self.contenedorOpciones.config( bg="#C4C4C4")

        self.labelQueDesea = tk.Label(self.contenedorOpciones, text="¿Qué desea realizar el dia de hoy?")
        self.labelQueDesea.place(x=10, y=10, width =500, height =70)
        self.labelQueDesea.config(font=("Monserrat",19,), bg="#C4C4C4")

        self.botonCrearContacto = tk.Button(self.contenedorOpciones, text="Añadir Contacto", command=self.botonCrearContactoFuncion)
        self.botonCrearContacto.place(x=130, y=90, width =500, height =70)
        self.botonCrearContacto.config(font=("Monserrat",19,), bg="#031E66", fg="white")

        self.botonListaContactos = tk.Button(self.contenedorOpciones, text="Lista de Contactos", command=self.botonVerContactosFuncion)
        self.botonListaContactos.place(x=130, y=180, width=500, height=70)
        self.botonListaContactos.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonEditarContacto = tk.Button(self.contenedorOpciones, text="Editar Contacto", command=self.botonEditarContactoFuncion)
        self.botonEditarContacto.place(x=130, y=270, width=500, height=70)
        self.botonEditarContacto.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonEliminarContacto = tk.Button(self.contenedorOpciones, text="Eliminar Contacto", command=self.botonEliminarContactoFuncion)
        self.botonEliminarContacto.place(x=130, y=360, width=500, height=70)
        self.botonEliminarContacto.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonSalir = tk.Button(self.contenedorOpciones, text="Salir", command=self.botonSalirFuncion)
        self.botonSalir.place(x=130, y=450, width=500, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

    def botonSalirFuncion(self):
        self.destroy()

    def botonCrearContactoFuncion(self):
        self.ventanaCrearContactos = frameCrearRegistrosContactos(self)

    def botonEditarContactoFuncion(self):
        self.ventanaEditarContactos = frameEditarRegistrosContactos(self)

    def botonEliminarContactoFuncion(self):
        self.ventanaEliminarContactos = frameEliminarRegistrosContactos(self)

    def botonVerContactosFuncion(self):
        self.ventanaVerContactos = frameVerRegistrosContactos(self)


