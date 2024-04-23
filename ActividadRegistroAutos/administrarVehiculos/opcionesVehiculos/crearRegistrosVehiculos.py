import tkinter as tk
from tkinter import font

from ActividadRegistroAutos.ORM.ORM import Vehiculo
from tkinter import messagebox as ms



class frameCrearRegistrosVehiculos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #Comienzo desarrollo de la GUI
        #Desarrollo apartado bienvenida
        self.geometry("1100x650")
        self.resizable(False, False)

        self.contenedorTituloYDatos = tk.Frame(self)
        self.contenedorTituloYDatos.place(x=0, y =0, width =800, height =650)
        self.contenedorTituloYDatos.config( bg="#031E66")

        self.separadorTitulo = tk.Frame(self.contenedorTituloYDatos)
        self.separadorTitulo.place(x=0, y =100, width=800, height =10)
        self.separadorTitulo.config( bg="white")

        self.labelTitulo = tk.Label(self.contenedorTituloYDatos, text="Añadir vehiculo a Usuario(Propietario)")
        self.labelTitulo.place(x=20, y=0, width =700, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.labelIdPropietario = tk.Label(self.contenedorTituloYDatos, text="•Id Propietario:")
        self.labelIdPropietario.place(x=20, y=140, width=180, height=80)
        self.labelIdPropietario.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryIdpropietario = tk.Entry(self.contenedorTituloYDatos)
        self.entryIdpropietario.place(x=210, y=140, width=100, height=80)
        self.entryIdpropietario.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelMarca = tk.Label(self.contenedorTituloYDatos, text="•Marca:")
        self.labelMarca.place(x=20, y=230, width=180, height=80)
        self.labelMarca.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryMarca = tk.Entry(self.contenedorTituloYDatos)
        self.entryMarca.place(x=210, y=230, width=540, height=80)
        self.entryMarca.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelModelo = tk.Label(self.contenedorTituloYDatos, text="•Modelo:")
        self.labelModelo.place(x=20, y=320, width=180, height=80)
        self.labelModelo.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryModelo = tk.Entry(self.contenedorTituloYDatos)
        self.entryModelo.place(x=210, y=320, width=540, height=80)
        self.entryModelo.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelAño = tk.Label(self.contenedorTituloYDatos, text="•Año:")
        self.labelAño.place(x=20, y=410, width=180, height=80)
        self.labelAño.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryAño = tk.Entry(self.contenedorTituloYDatos)
        self.entryAño.place(x=210, y=410, width=200, height=80)
        self.entryAño.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelMatricula = tk.Label(self.contenedorTituloYDatos, text="•Matricula:")
        self.labelMatricula.place(x=370, y=410, width=180, height=80)
        self.labelMatricula.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryMatricula = tk.Entry(self.contenedorTituloYDatos)
        self.entryMatricula.place(x=550, y=410, width=200, height=80)
        self.entryMatricula.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelNumeroSerie = tk.Label(self.contenedorTituloYDatos, text="•Numero Serie:")
        self.labelNumeroSerie.place(x=20, y=500, width=180, height=80)
        self.labelNumeroSerie.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryNumeroSerie = tk.Entry(self.contenedorTituloYDatos)
        self.entryNumeroSerie.place(x=210, y=500, width=540, height=80)
        self.entryNumeroSerie.config(font=("Monserrat", 18), bg="white", fg="black")

        self.contenedorBotones = tk.Frame(self)
        self.contenedorBotones.place(x=800, y =0, width =300, height =650)
        self.contenedorBotones.config( bg="#C4C4C4")

        self.botonGuardar = tk.Button(self.contenedorBotones, text="Guardar", command=self.botonGuardarFuncion)
        self.botonGuardar.place(x=25, y=140, width=240, height=70)
        self.botonGuardar.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonLimpiar = tk.Button(self.contenedorBotones, text="Limpiar", command=self.botonSalirFuncion)
        self.botonLimpiar.place(x=25, y=280, width=240, height=70)
        self.botonLimpiar.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonSalir = tk.Button(self.contenedorBotones, text="Salir", command=self.botonSalirFuncion)
        self.botonSalir.place(x=25, y=420, width=240, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")


    def botonSalirFuncion(self):
        self.destroy()

    def botonGuardarFuncion(self):
        try:
            #obtengo los datos de los entrys
            IdPropietario = self.entryIdpropietario.get()
            Marca = self.entryMarca.get()
            Modelo = self.entryModelo.get()
            Año = self.entryAño.get()
            Placas = self.entryMatricula.get()
            NumeroSerie = self.entryNumeroSerie.get()

            #Uso el metodo registrarUsuario() de la clase Propietario (ORM)
            Vehiculo.registrarVehiculo(IdPropietario,Marca,Modelo,
                                       Año, Placas,NumeroSerie)

        except Exception as ErrorRegistrar:
            ms.showerror("Error de Registro de usuario", "Verifica que los datos esten bien escritos y que el Propietario exista")



