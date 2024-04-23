import tkinter as tk
from tkinter import font
from ActividadRegistroAutos.ORM.ORM import Contacto
from tkinter import messagebox as ms


class frameCrearRegistrosContactos(tk.Toplevel):
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

        self.labelTitulo = tk.Label(self.contenedorTituloYDatos, text="Añadir contacto a Usuario(Propietario)")
        self.labelTitulo.place(x=20, y=0, width =700, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.labelIdPropietario = tk.Label(self.contenedorTituloYDatos, text="•Id Propietario:")
        self.labelIdPropietario.place(x=20, y=140, width=180, height=80)
        self.labelIdPropietario.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryIdpropietario = tk.Entry(self.contenedorTituloYDatos)
        self.entryIdpropietario.place(x=210, y=140, width=100, height=80)
        self.entryIdpropietario.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelTipoContacto = tk.Label(self.contenedorTituloYDatos, text="•Tipo contacto:")
        self.labelTipoContacto.place(x=20, y=260, width=180, height=80)
        self.labelTipoContacto.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryTipoContacto = tk.Entry(self.contenedorTituloYDatos)
        self.entryTipoContacto.place(x=210, y=260, width=540, height=80)
        self.entryTipoContacto.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelDescripcionContacto = tk.Label(self.contenedorTituloYDatos, text="•Descripción:")
        self.labelDescripcionContacto.place(x=20, y=380, width=180, height=80)
        self.labelDescripcionContacto.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryDescripcionContacto = tk.Entry(self.contenedorTituloYDatos)
        self.entryDescripcionContacto.place(x=210, y=380, width=540, height=80)
        self.entryDescripcionContacto.config(font=("Monserrat", 18), bg="white", fg="black")


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
            tipoContacto = self.entryTipoContacto.get()
            descripcionContacto = self.entryDescripcionContacto.get()
            #Uso el metodo registrarUsuario() de la clase Propietario (ORM)
            Contacto.registrarContacto(IdPropietario,tipoContacto,descripcionContacto)

        except Exception as ErrorRegistrar:
            ms.showerror("Error de Registro de usuario", "Verifica que los datos esten bien escritos")





