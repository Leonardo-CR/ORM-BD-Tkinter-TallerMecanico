import tkinter as tk
from tkinter import font
from administrarUsuarios.opcionesUsuarios.crearRegistrosUsuarios import frameCrearRegistrosUsuarios
from administrarUsuarios.opcionesUsuarios.editarRegistrosUsuarios import frameEditarRegistrosUsuarios
from administrarUsuarios.opcionesUsuarios.eliminarRegistrosUsuarios import frameEliminarRegistrosUsuarios
from administrarUsuarios.opcionesUsuarios.verRegistrosUsuarios import frameVerRegistrosUsuarios



class frameUsuariosOpciones(tk.Toplevel):
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

        self.labelTitulo = tk.Label(self.contenedorTitulo, text="Administrar Usuarios")
        self.labelTitulo.place(x=20, y=0, width =700, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.contenedorOpciones = tk.Frame(self)
        self.contenedorOpciones.place(x=0, y =100, width =800, height =550)
        self.contenedorOpciones.config( bg="#C4C4C4")

        self.labelQueDesea = tk.Label(self.contenedorOpciones, text="¿Qué desea realizar el dia de hoy?")
        self.labelQueDesea.place(x=10, y=10, width =500, height =70)
        self.labelQueDesea.config(font=("Monserrat",19,), bg="#C4C4C4")

        self.botonCrearUsuario = tk.Button(self.contenedorOpciones, text="Crear Usuario", command=self.botonCrearUsuarioFuncion)
        self.botonCrearUsuario.place(x=130, y=90, width =500, height =70)
        self.botonCrearUsuario.config(font=("Monserrat",19,), bg="#031E66", fg="white")

        self.botonListaUsuarios = tk.Button(self.contenedorOpciones, text="Lista de Usuarios", command=self.botonVerUsuarioFuncion)
        self.botonListaUsuarios.place(x=130, y=180, width=500, height=70)
        self.botonListaUsuarios.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonEditarUsuario = tk.Button(self.contenedorOpciones, text="Editar Usuario", command=self.botonEditarUsuarioFuncion)
        self.botonEditarUsuario.place(x=130, y=270, width=500, height=70)
        self.botonEditarUsuario.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonEliminarUsuario = tk.Button(self.contenedorOpciones, text="Eliminar Usuario", command=self.botonEliminarUsuarioFuncion)
        self.botonEliminarUsuario.place(x=130, y=360, width=500, height=70)
        self.botonEliminarUsuario.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonSalir = tk.Button(self.contenedorOpciones, text="Salir", command=self.botonSalirFuncion)
        self.botonSalir.place(x=130, y=450, width=500, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")


    def botonSalirFuncion(self):
        self.destroy()

    def botonCrearUsuarioFuncion(self):
        self.ventanaCrearUsuarios = frameCrearRegistrosUsuarios(self)

    def botonEditarUsuarioFuncion(self):
        self.ventanaEditarUsuarios = frameEditarRegistrosUsuarios(self)

    def botonEliminarUsuarioFuncion(self):
        self.ventanaEliminarUsuarios = frameEliminarRegistrosUsuarios(self)

    def botonVerUsuarioFuncion(self):
        self.ventanaVerUsuarios = frameVerRegistrosUsuarios(self)


