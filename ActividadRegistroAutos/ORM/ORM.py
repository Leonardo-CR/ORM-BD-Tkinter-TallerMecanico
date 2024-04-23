from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy.orm import relationship
from tkinter import messagebox as ms



# Para conectar con la base de datos y crear las tablas
engine = create_engine('postgresql://postgres:admin@localhost:5432/practicaTaller')

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crea una instancia de la clase declarative_base
Base = declarative_base()

# Define la clase Propietario
class Propietario(Base):
    __tablename__ = 'propietarios'

    IdPropietario = Column(Integer, primary_key=True)
    Nombre = Column(String)
    Apellido = Column(String)
    RFC = Column(String)
    Domicilio = Column(String)
    # Relación uno a muchos con la tabla Contactos
    contactos = relationship('Contacto', backref='propietario')
    vehiculos = relationship('Vehiculo', backref='propietario')

    @classmethod
    def mostrarTodosLosValoresParaTreeView(cls):
        return session.query(Propietario.IdPropietario,Propietario.Nombre,Propietario.Apellido,
                             Propietario.RFC,Propietario.Domicilio).all()

    @classmethod
    def registrarUsuario(cls, Nombre, Apellido, RFC, Domicilio):
        usuarioNuevo = cls(Nombre=Nombre, Apellido= Apellido, RFC = RFC, Domicilio = Domicilio)
        session.add(usuarioNuevo)
        session.commit()
        session.close()

    @classmethod
    def encontrarUsuario(cls,IdPropietario):
        UsurioEncontrar = session.query(Propietario.IdPropietario, Propietario.Nombre, Propietario.Apellido,
                                        Propietario.RFC,Propietario.Domicilio).filter(
            Propietario.IdPropietario == IdPropietario
        ).first()
        return UsurioEncontrar #Retorno el usuario como una tupla[] para iterar en sus posiciones para ver los valores


    @classmethod
    def editarUsuario(cls,IdPropietario, Nombre, Apellido, RFC, Domicilio):
        usuarioEditar = session.query(Propietario).filter(Propietario.IdPropietario == IdPropietario).first()
        usuarioEditar.Nombre = Nombre
        usuarioEditar.Apellido = Apellido
        usuarioEditar.RFC = RFC
        usuarioEditar.Domicilio = Domicilio
        session.add(usuarioEditar)
        session.commit()

    @classmethod
    def eliminarUsuario(cls,IdPropietarioEliminar):
        UsuarioEliminar = session.query(Propietario).filter(Propietario.IdPropietario == IdPropietarioEliminar).delete()
        session.commit()


# Define la clase Contacto
class Contacto(Base):
    __tablename__ = 'contactos'

    IdContacto = Column(Integer, primary_key=True)
    IdPropietario = Column(Integer, ForeignKey('propietarios.IdPropietario'))
    tipo_contacto = Column(String)
    descripcion = Column(String)

    @classmethod
    def mostrarTodosLosValoresParaTreeView(cls):
        return session.query(Contacto.IdContacto, Contacto.IdPropietario,
                             Contacto.tipo_contacto,Contacto.descripcion).all()

    @classmethod
    def eliminarContacto(cls, IdContactoEliminar):
        ContactoEliminar = session.query(Contacto).filter(Contacto.IdContacto == IdContactoEliminar).delete()
        session.commit()


    @classmethod
    def verificarExistenciaUsuario(cls, IdPropetario):
        # Verificar si el IdPropietario existe en la tabla propietarios
        propietario_existente = session.query(Propietario.IdPropietario).filter(
            Propietario.IdPropietario == IdPropetario).first()
        if propietario_existente == None:
            return None
        else:
            return propietario_existente.IdPropietario  # Retorna el id como INTEGER

    @classmethod
    def registrarContacto(cls, IdPropietario, tipo_contacto, descripcion):
        IdValidado = cls.verificarExistenciaUsuario(IdPropietario)
        if IdValidado == None:
            ms.showerror("Error de registro","Verifica los datos y el ID del propietario")
        else:
            # Crear un nuevo objeto Contacto con el IdPropietario proporcionado
            contactoNuevo = cls(IdPropietario=IdValidado, tipo_contacto=tipo_contacto, descripcion=descripcion)
            # Agregar el nuevo contacto a la sesión y confirmar la transacción
            session.add(contactoNuevo)
            session.commit()
            session.close()

    @classmethod
    def editarContacto(cls,IdContacto, tipo_contacto, descripcion):
        usuarioEditar = session.query(Contacto).filter(Contacto.IdContacto == IdContacto).first()
        #No se puede editar el numero de usuario
        usuarioEditar.tipo_contacto = tipo_contacto
        usuarioEditar.descripcion = descripcion
        session.add(usuarioEditar)
        session.commit()

    @classmethod
    def encontrarContacto(cls, IdContacto):
        ContactoEncontrar = session.query(Contacto.IdPropietario, Contacto.tipo_contacto,
                                          Contacto.descripcion).filter(
            Contacto.IdContacto == IdContacto
        ).first()
        return ContactoEncontrar  # Retorno el usuario como una tupla[] para iterar en sus posiciones para ver los valores

"""ORM del Vehiculo la ultima que me falta """
# Define la clase Vehiculo
class Vehiculo(Base):
    __tablename__ = 'vehiculos'

    IdVehiculo = Column(Integer, primary_key=True)
    IdPropietario = Column(Integer, ForeignKey('propietarios.IdPropietario'))
    marca = Column(String)
    modelo = Column(String)
    año = Column(Integer)
    placas = Column(String)
    numero_serie = Column(String)


    @classmethod
    def mostrarTodosLosValoresParaTreeView(cls):
        return session.query(Vehiculo.IdVehiculo, Vehiculo.IdPropietario,
                             Vehiculo.marca, Vehiculo.modelo,
                             Vehiculo.año, Vehiculo.placas,
                             Vehiculo.numero_serie).all()

    @classmethod
    def eliminarVehiculo(cls, IdVehiculoEliminar):
        VehiculoEliminar = session.query(Vehiculo).filter(Vehiculo.IdVehiculo == IdVehiculoEliminar).delete()
        session.commit()



    @classmethod
    def verificarExistenciaUsuario(cls,IdPropetario):
        # Verificar si el IdPropietario existe en la tabla propietarios
        propietario_existente = session.query(Propietario.IdPropietario).filter(Propietario.IdPropietario==IdPropetario).first()
        if propietario_existente==None:
            return None
        else:

            return propietario_existente.IdPropietario #Retorna el id como INTEGER

    @classmethod
    def registrarVehiculo(cls, IdPropietario, marca, modelo, año, placas, numero_serie):
        IdValidado = cls.verificarExistenciaUsuario(IdPropietario)
        if IdValidado==None:
            ms.showerror("Error de registro", "Verifica los datos y el ID del propietario")

        else:
            # Crear un nuevo objeto Contacto con el IdPropietario proporcionado
            vehiculoNuevo = cls(IdPropietario=IdValidado, marca=marca, modelo = modelo, año = año, placas=placas,
                            numero_serie=numero_serie)
            # Agregar el nuevo contacto a la sesión y confirmar la transacción
            session.add(vehiculoNuevo)
            session.commit()
            session.close()

    @classmethod
    def editarVehiculo(cls,IdVehiculo,marca, modelo, año, placas, numero_serie):
        vehiculoEditar = session.query(Vehiculo).filter(Vehiculo.IdVehiculo == IdVehiculo).first()
        #No se puede editar el numero de usuario
        vehiculoEditar.marca = marca
        vehiculoEditar.modelo = modelo
        vehiculoEditar.año = año
        vehiculoEditar.placas = placas
        vehiculoEditar.numero_serie = numero_serie
        session.add(vehiculoEditar)
        session.commit()

    @classmethod
    def encontrarVehiculo(cls, IdVehiculoEncontrar):
        VehiculoEncontrar = session.query(Vehiculo.IdPropietario,Vehiculo.marca,
                                          Vehiculo.modelo, Vehiculo.año, Vehiculo.placas,
                                          Vehiculo.numero_serie).filter(
            Vehiculo.IdVehiculo == IdVehiculoEncontrar
        ).first()
        return VehiculoEncontrar  # Retorno el usuario como una tupla[] para iterar en sus posiciones para ver los valores



Base.metadata.create_all(engine)

Contacto.encontrarContacto(4)

propietario_existente = session.query(Propietario.IdPropietario).filter(
    Propietario.IdPropietario == 1000).first()
#Pone NONE
print(propietario_existente)