import tkinter as tk
from tkinter import font
from ActividadRegistroAutos.ORM.ORM import Contacto
from tkinter import messagebox as ms


class frameEditarRegistrosContactos(tk.Toplevel):
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

        self.labelTitulo = tk.Label(self.contenedorTituloYDatos, text="Editar datos de Contacto (Propietario)")
        self.labelTitulo.place(x=20, y=0, width =700, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.labelIDContacto = tk.Label(self.contenedorTituloYDatos,text="•ID Contacto:")
        self.labelIDContacto.place(x=20, y=140, width=180, height=80)
        self.labelIDContacto.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryIDContacto = tk.Entry(self.contenedorTituloYDatos)
        self.entryIDContacto.place(x=210, y=140, width=120, height=80)
        self.entryIDContacto.config(font=("Monserrat", 18), bg="white", fg="black")


        self.labelIDUsuario = tk.Label(self.contenedorTituloYDatos, text="•ID Usuario:")
        self.labelIDUsuario.place(x=20, y=230, width=180, height=80)
        self.labelIDUsuario.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryIDUsuario = tk.Entry(self.contenedorTituloYDatos)
        self.entryIDUsuario.place(x=210, y=230, width=120, height=80)
        self.entryIDUsuario.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelTipoContacto = tk.Label(self.contenedorTituloYDatos, text="•Tipo contacto:")
        self.labelTipoContacto.place(x=20, y=320, width=180, height=80)
        self.labelTipoContacto.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryTipoContacto = tk.Entry(self.contenedorTituloYDatos)
        self.entryTipoContacto.place(x=210, y=320, width=540, height=80)
        self.entryTipoContacto.config(font=("Monserrat", 18), bg="white", fg="black")

        self.labelDescripcionContacto = tk.Label(self.contenedorTituloYDatos, text="•Descripción:")
        self.labelDescripcionContacto.place(x=20, y=410, width=180, height=80)
        self.labelDescripcionContacto.config(font=("Monserrat", 18), bg="#031E66", fg="white")

        self.entryDescripcionContacto = tk.Entry(self.contenedorTituloYDatos)
        self.entryDescripcionContacto.place(x=210, y=410, width=540, height=80)
        self.entryDescripcionContacto.config(font=("Monserrat", 18), bg="white", fg="black")


        self.contenedorBotones = tk.Frame(self)
        self.contenedorBotones.place(x=800, y =0, width =300, height =650)
        self.contenedorBotones.config( bg="#C4C4C4")

        self.botonBuscar = tk.Button(self.contenedorBotones, text="Buscar", command=self.botonBuscarFuncion)
        self.botonBuscar.place(x=25, y=90, width=240, height=70)
        self.botonBuscar.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonEditar = tk.Button(self.contenedorBotones, text="Editar", command=self.botonEditarFuncion)
        self.botonEditar.place(x=25, y=210, width=240, height=70)
        self.botonEditar.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonLimpiar = tk.Button(self.contenedorBotones, text="Limpiar", command=self.botonLimpiarFuncion)
        self.botonLimpiar.place(x=25, y=330, width=240, height=70)
        self.botonLimpiar.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

        self.botonSalir = tk.Button(self.contenedorBotones, text="Salir", command=self.botonSalirFuncion)
        self.botonSalir.place(x=25, y=460, width=240, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")




    def botonSalirFuncion(self):
        self.destroy()

    def botonLimpiarFuncion(self):
        #self.entryIDUsuario.delete(0,tk.END)
        self.entryIDUsuario.delete(0,tk.END)
        self.entryTipoContacto.delete(0,tk.END)
        self.entryDescripcionContacto.delete(0,tk.END)

    def ponerValoresEnEntrysFuncion(self,valoresConsulta):
        idPropietario = valoresConsulta[0]
        idPropietarioSTR = str(idPropietario)
        self.entryIDUsuario.insert(0, idPropietarioSTR)
        self.entryTipoContacto.insert(0, valoresConsulta[1])
        self.entryDescripcionContacto.insert(0, valoresConsulta[2])

    def botonBuscarFuncion(self):
        try:
            IdBuscarContacto = self.entryIDContacto.get()
            consulta = Contacto.encontrarContacto(IdBuscarContacto)
            self.botonLimpiarFuncion()
            self.ponerValoresEnEntrysFuncion(consulta)
        except Exception as ErrorBuscarPropietario:
            ms.showerror("Error de busqueda","Asegurate de que el Id de propietario sea correcto")

    def botonEditarFuncion(self):
        try:
            # Id del contacto a cambiar
            idEdicion = self.entryIDContacto.get()
            # Obtengo los Valores
            tipoContacto = self.entryTipoContacto.get()
            descripcion = self.entryDescripcionContacto.get()
            # Hago los cambios
            Contacto.editarContacto(idEdicion,tipoContacto, descripcion)
        except Exception as ErrorEdicion:
            ms.showerror("Error de edicion","Verifica que los datos esten escritos correctamente")
