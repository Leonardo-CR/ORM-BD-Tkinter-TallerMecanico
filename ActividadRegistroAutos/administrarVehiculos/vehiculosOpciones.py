import tkinter as tk
from tkinter import font
from administrarVehiculos.opcionesVehiculos.crearRegistrosVehiculos import frameCrearRegistrosVehiculos
from administrarVehiculos.opcionesVehiculos.editarRegistrosVehiculos import frameEditarRegistrosVehiculos
from administrarVehiculos.opcionesVehiculos.eliminarRegistrosVehiculos import frameEliminarRegistrosVehiculos
from administrarVehiculos.opcionesVehiculos.verRegistrosVehiculos import frameVerRegistrosVehiculos




class frameVehiculosOpciones(tk.Toplevel):
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

        self.labelTitulo = tk.Label(self.contenedorTitulo, text="Administrar Vehiculos")
        self.labelTitulo.place(x=20, y=0, width =700, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.contenedorOpciones = tk.Frame(self)
        self.contenedorOpciones.place(x=0, y =100, width =800, height =550)
        self.contenedorOpciones.config( bg="#C4C4C4")

        self.labelQueDesea = tk.Label(self.contenedorOpciones, text="¿Qué desea realizar el dia de hoy?")
        self.labelQueDesea.place(x=10, y=10, width =500, height =70)
        self.labelQueDesea.config(font=("Monserrat",19,), bg="#C4C4C4")

        self.botonCrearVehiculo = tk.Button(self.contenedorOpciones, text="Añadir Vehiculo", command=self.botonCrearVehiculoFuncion)
        self.botonCrearVehiculo.place(x=130, y=90, width =500, height =70)
        self.botonCrearVehiculo.config(font=("Monserrat",19,), bg="#031E66", fg="white")

        self.botonListaVehiculos = tk.Button(self.contenedorOpciones, text="Lista de Vehiculos", command=self.botonVerVehiculoFuncion)
        self.botonListaVehiculos.place(x=130, y=180, width=500, height=70)
        self.botonListaVehiculos.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonEditarVehiculo = tk.Button(self.contenedorOpciones, text="Editar Vehiculo", command=self.botonEditarVehiculoFuncion)
        self.botonEditarVehiculo.place(x=130, y=270, width=500, height=70)
        self.botonEditarVehiculo.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonEliminarVehiculo = tk.Button(self.contenedorOpciones, text="Eliminar Vehiculo", command=self.botonEliminarVehiculoFuncion)
        self.botonEliminarVehiculo.place(x=130, y=360, width=500, height=70)
        self.botonEliminarVehiculo.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonSalir = tk.Button(self.contenedorOpciones, text="Salir", command=self.botonSalirFuncion)
        self.botonSalir.place(x=130, y=450, width=500, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

    def botonSalirFuncion(self):
        self.destroy()

    def botonCrearVehiculoFuncion(self):
        self.ventanaCrearVehiculos = frameCrearRegistrosVehiculos(self)

    def botonEditarVehiculoFuncion(self):
        self.ventanaEditarVehiculos = frameEditarRegistrosVehiculos(self)

    def botonEliminarVehiculoFuncion(self):
        self.ventanaEliminarVehiculos = frameEliminarRegistrosVehiculos(self)

    def botonVerVehiculoFuncion(self):
        self.ventanaVerVehiculos = frameVerRegistrosVehiculos(self)


