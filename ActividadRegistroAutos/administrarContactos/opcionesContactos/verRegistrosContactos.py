import tkinter as tk
from tkinter import font
from ActividadRegistroAutos.ORM.ORM import Contacto
from tkinter import messagebox as ms
from tkinter.ttk import Treeview



class frameVerRegistrosContactos(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        #Comienzo desarrollo de la GUI
        #Desarrollo apartado bienvenida
        self.geometry("1100x650")
        self.resizable(False, False)

        self.contenedorTitulo = tk.Frame(self)
        self.contenedorTitulo.place(x=0, y =0, width =1100, height =100)
        self.contenedorTitulo.config( bg="#031E66")

        self.labelTitulo = tk.Label(self.contenedorTitulo, text="Ver contactos de Usuarios (Propietarios)")
        self.labelTitulo.place(x=20, y=0, width =1100, height =100)
        self.labelTitulo.config(font=("Monserrat",25,"bold"), bg="#031E66", fg="white")

        self.contenedorContenido = tk.Frame(self)
        self.contenedorContenido.place(x=0, y =100, width =1100, height =550)
        self.contenedorContenido.config( bg="#C4C4C4")

        self.contenedorTreeView = tk.Frame(self.contenedorContenido)
        self.contenedorTreeView.place(x=20, y =20, width =1060, height =435)
        self.contenedorTreeView.config( bg="black")

        #####        #Desarrollo tabla  Treeview
        self.tablaRegistros = Treeview(self.contenedorTreeView, columns=(
            "colIdContacto", "colIdUsuario", "colTipo", "colDescripcion"))
        self.tablaRegistros.place(x=0, y=0, width=1060, height=435)

        # tablaPaises.heading("#0",text="ID")
        self.tablaRegistros.heading("colIdContacto", text="ID Contacto")
        self.tablaRegistros.heading("colIdUsuario", text="Id Usuario")
        self.tablaRegistros.heading("colTipo", text="Tipo")
        self.tablaRegistros.heading("colDescripcion", text="Descripcion")
        # Oculto la columna por defecto para que no moleste
        self.tablaRegistros.column("#0", width=0, stretch=tk.NO)
        self.tablaRegistros.heading("#0", text="")

        self.scrollVertical = tk.Scrollbar(self.tablaRegistros, command=self.tablaRegistros.yview())
        self.scrollVertical.pack(side=tk.RIGHT, fill=tk.Y)
        # listaCarreras.configure(yscrollcommand=scroll.set)
        self.tablaRegistros.configure(yscrollcommand=self.scrollVertical.set)

        self.scrollHorizontal = tk.Scrollbar(self.contenedorTreeView, orient="horizontal",
                                             command=self.tablaRegistros.xview)
        self.scrollHorizontal.place(x=0, y=420, width=1060)

        # Configurar el Treeview para usar el scroll horizontal
        self.tablaRegistros.configure(xscrollcommand=self.scrollHorizontal.set)
        # Obtener registros
        self.registrosBD = Contacto.mostrarTodosLosValoresParaTreeView()
        # Poner registros en el Treeveew
        # Este for pone los valores en las columnas correspondientes del TreeView segun la variable "valores"
        for registro in self.registrosBD:
            self.tablaRegistros.insert("", "end", values=(
                registro.IdContacto,
                registro.IdPropietario,
                registro.tipo_contacto,
                registro.descripcion
            ))
        ##Evento para mostrar los registros en la tabla principal
        self.tablaRegistros.bind("<<TreeviewSelect>>", self.mostrar_valores_seleccionados)

        self.botonSalir = tk.Button(self.contenedorContenido, text="Salir", command=self.botonSalirFuncion)
        self.botonSalir.place(x=25, y=470, width=240, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")

    def mostrar_valores_seleccionados(self, event):  ###Esta funcion me muestra el registro seleccionado en el treeview
        itemSeleccionado = self.tablaRegistros.selection()
        valores = self.tablaRegistros.item(itemSeleccionado, 'values')
        return valores
        ####################################################



        self.botonSalir = tk.Button(self.contenedorContenido, text="Salir", command=self.botonSalirFuncion)
        self.botonSalir.place(x=25, y=470, width=240, height=70)
        self.botonSalir.config(font=("Monserrat", 19,), bg="#031E66", fg="white")




    def botonSalirFuncion(self):
        self.destroy()


