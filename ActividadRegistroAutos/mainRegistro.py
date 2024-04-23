import tkinter as tk
from tkinter import font
from administrarUsuarios.usuariosOpciones import frameUsuariosOpciones
from administrarContactos.contactosOpciones import frameContactosOpciones
from administrarVehiculos.vehiculosOpciones import frameVehiculosOpciones


class framePrincipal(tk.Frame):
    def __init__(self, contenedor):
        super().__init__(contenedor)
        letra_montserrat = font.Font(family="Montserrat")
        #Comienzo desarrollo de la GUI
        #Desarrollo apartado bienvenida
        self.contenedor = contenedor
        self.contenedor.geometry("800x650")
        self.contenedor.resizable(False, False)

        self.contenedorBienvenida = tk.Frame(self.contenedor)
        self.contenedorBienvenida.place(x=0, y =0, width =800, height =100)
        self.contenedorBienvenida.config( bg="#031E66")

        self.labelBienvenida = tk.Label(self.contenedorBienvenida, text="Bienvenid@ al sistema de Registros")
        self.labelBienvenida.place(x=20, y=0, width =700, height =100)
        self.labelBienvenida.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.contenedorOpciones = tk.Frame(self.contenedor)
        self.contenedorOpciones.place(x=0, y =100, width =800, height =480)
        self.contenedorOpciones.config( bg="#C4C4C4")

        self.labelQueDesea = tk.Label(self.contenedorOpciones, text="¿Qué desea realizar el dia de hoy?")
        self.labelQueDesea.place(x=10, y=10, width =500, height =70)
        self.labelQueDesea.config(font=("Monserrat",19,), bg="#C4C4C4")

        self.botonAdministrarUsuarios = tk.Button(self.contenedorOpciones, text="Administrar Usuarios", command=self.botonAdministrarUsuariosFuncion)
        self.botonAdministrarUsuarios.place(x=130, y=90, width =500, height =70)
        self.botonAdministrarUsuarios.config(font=("Monserrat",19,), bg="#031E66", fg="white")

        self.botonAdministrarContactos = tk.Button(self.contenedorOpciones, text="Administrar Contactos", command=self.botonAdministrarContactosFuncion)
        self.botonAdministrarContactos.place(x=130, y=180, width=500, height=70)
        self.botonAdministrarContactos.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonAdministrarVehiculos = tk.Button(self.contenedorOpciones, text="Administrar Vehiculos", command=self.botonAdministrarVehiculosFuncion)
        self.botonAdministrarVehiculos.place(x=130, y=270, width=500, height=70)
        self.botonAdministrarVehiculos.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonSalir = tk.Button(self.contenedorOpciones, text="Salir",command=self.botonSalirFuncion)
        self.botonSalir.place(x=130, y=360, width=500, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")
        #580 utilizado

        self.contenedorBy = tk.Frame(self.contenedor)
        self.contenedorBy.place(x=0, y=580, width=800, height=120)
        self.contenedorBy.config(bg="#031E66")

        self.labelBy = tk.Label(self.contenedorBy, text="By: Cruz Rosas Leonardo Daniel")
        self.labelBy.place(x=0, y=0, width=700, height=80)
        self.labelBy.config(font=("Monserrat", 15), bg="#031E66", fg="white")

    def botonAdministrarUsuariosFuncion(self):
        self.ventanaUsuarios = frameUsuariosOpciones(self.contenedor)

    def botonAdministrarContactosFuncion(self):
        self.ventanaContactos = frameContactosOpciones(self.contenedor)

    def botonAdministrarVehiculosFuncion(self):
        self.ventanaVehiculos = frameVehiculosOpciones(self.contenedor)

    def botonSalirFuncion(self):
        self.contenedor.destroy()



