import tkinter as tk
from tkinter import font
from ActividadRegistroAutos.ORM.ORM import Propietario
from tkinter import messagebox as ms



class frameCrearRegistrosUsuarios(tk.Toplevel):
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

        self.labelTitulo = tk.Label(self.contenedorTituloYDatos, text="Crear registro de Usuario (Propietario)")
        self.labelTitulo.place(x=20, y=0, width =700, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.labelNombre = tk.Label(self.contenedorTituloYDatos, text="•Nombre:")
        self.labelNombre.place(x=20, y=140, width=180, height=80)
        self.labelNombre.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryNombre = tk.Entry(self.contenedorTituloYDatos)
        self.entryNombre.place(x=210, y=140, width=540, height=80)
        self.entryNombre.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelApellidos = tk.Label(self.contenedorTituloYDatos, text="•Apellidos:")
        self.labelApellidos.place(x=20, y=260, width=180, height=80)
        self.labelApellidos.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryApellidos = tk.Entry(self.contenedorTituloYDatos)
        self.entryApellidos.place(x=210, y=260, width=540, height=80)
        self.entryApellidos.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelRFC = tk.Label(self.contenedorTituloYDatos, text="•RFC:")
        self.labelRFC.place(x=20, y=380, width=180, height=80)
        self.labelRFC.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryRFC = tk.Entry(self.contenedorTituloYDatos)
        self.entryRFC.place(x=210, y=380, width=540, height=80)
        self.entryRFC.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelDomicilio = tk.Label(self.contenedorTituloYDatos, text="•Domicilio:")
        self.labelDomicilio.place(x=20, y=500, width=180, height=80)
        self.labelDomicilio.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryDomicilio = tk.Entry(self.contenedorTituloYDatos)
        self.entryDomicilio.place(x=210, y=500, width=540, height=80)
        self.entryDomicilio.config(font=("Monserrat", 18), bg="white", fg="black")

        self.contenedorBotones = tk.Frame(self)
        self.contenedorBotones.place(x=800, y =0, width =300, height =650)
        self.contenedorBotones.config( bg="#C4C4C4")

        self.botonGuardar = tk.Button(self.contenedorBotones, text="Guardar", command=self.botonGuardarFuncion)
        self.botonGuardar.place(x=25, y=140, width=240, height=70)
        self.botonGuardar.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonLimpiar = tk.Button(self.contenedorBotones, text="Limpiar", command=self.botonLimpiarFuncion)
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
            nombre = self.entryNombre.get()
            apellido = self.entryApellidos.get()
            rfc = self.entryRFC.get()
            domicilio = self.entryDomicilio.get()
            #Uso el metodo registrarUsuario() de la clase Propietario (ORM)
            Propietario.registrarUsuario(nombre,apellido,rfc,domicilio)
        except Exception as ErrorRegistrar:
            ms.showerror("Error de Registro de usuario", "Verifica que los datos esten bien escritos")
    def botonLimpiarFuncion(self):
        self.entryNombre.delete(0,tk.END)
        self.entryApellidos.delete(0,tk.END)
        self.entryRFC.delete(0,tk.END)
        self.entryDomicilio.delete(0,tk.END)
