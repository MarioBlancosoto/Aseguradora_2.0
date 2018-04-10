from reportlab.platypus import Table
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Image
from reportlab.lib.pagesizes import  A4
from reportlab.lib import colors
import os
import sqlite3 as dbapi
import UiRexistro
import UiAseguradora
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk



class Controlador():

    """controlador,creada para separala vista e o controlador,cos método que reciben  os parámetros necesarios
        para interactuar coas clases das vistas,aquí están todos os métodos relacionados coa inserción,borrado,consulta e actualización
        de datos,manexa una soa base de datos chamada Asegurados e duas taboas unha pra os asegurados,chamada asegurados e outra para
        os administradores chamada admin."""


    def __init__(self):



        print("Versión da api :"+dbapi.apilevel)
        """
        threadsafety
        0   Threads may not share the module.
        1 	Threads may share the module, but not connections.
        2 	Threads may share the module and connections.
        3 	Threads may share the module, connections and cursors."""
        print(dbapi.threadsafety)
        """Paramstyle :
        Define """
        print(dbapi.paramstyle)
        """OLLO!!!!! se non funciona,cambiala dirección da de datos,ao estar na mesma carpeta non debería haber problema"""
        try:
            self.bbdd = dbapi.connect("Asegurados.db")
            print(self.bbdd)

            self.cursor = self.bbdd.cursor()
            print (self.cursor)



        except dbapi.OperationalError:
            print("No se pudo conectar a la base")
        except(dbapi.Miexcepcion, dbapi.Miexcepcion):
            print("Error Grave")




    def mostrarTabla(self):
        datos=[]
        try:

             data = self.cursor.execute("select * from asegurados").fetchall()


             for i in data:

                datos.append(i)
             return datos
        except dbapi.OperationalError:
            print("No se pudo conectar a la base")
        except(dbapi.Miexcepcion, dbapi.Miexcepcion):
            print("Error Grave")




    def modificarDatos(self,columna,contenido,contenido1):

        """Este e o metodo de cambialos datos dos asegurados,como xa se comentou no método da vista debemos recollelos datos do
        asegurado nesa fila na que se atopa seleccinada e a ID neste caso e sempre a columna 0,recibe os tres parámetros para poder
        recollelos na vista e non mezclar vista e controlador."""

        try:



           self.cursor.execute("Update asegurados set "+columna+" = '"+ contenido +"' where Poliza ='" +contenido1+"'")
           self.bbdd.commit()

        except dbapi.OperationalError:
            print("No se pudo conectar a la base")
        except(dbapi.Miexcepcion, dbapi.Miexcepcion):
            print("Error Grave")

    def borrarDatos(self,id):

         """O método de borrado que recolle o id do asegurado que se vai borrar,neste caso a fila e a columna seleccionada que sempre
         será 0."""

         consulta = "Delete from asegurados where Poliza = '"+id+"'"
         self.cursor.execute(consulta)
         self.bbdd.commit()



    def insertar_datos(self,Poliza,Nombre,Apellidos,Dni,Direccion,Telefono,Sexo,Seguro,Fechaini,Fechafin):

        """Neste método faise o insert e recibese por parámetro as dez variables pra poder chamalo na vista e inserttalos
        datos dos entrys e dos combos."""

        try:


            consulta = "Insert into asegurados  values (?,?,?,?,?,?,?,?,?,?)"
            print(consulta)
            self.cursor.execute(consulta,(Poliza,Nombre,Apellidos,Dni,Direccion,Telefono,Sexo,Seguro,Fechaini,Fechafin))
            self.bbdd.commit()

        except dbapi.OperationalError:
            print("No se pudo conectar a la base")




    def login(self,nombre,password):

        """Método dos admins realizado pra comprobar se o usuario e a contrasinal atopanse na base,se non o atopa saca o print erro
        contrasinal ou nome incorrectos,e non te deixa logear,pero se os atopa,pasa a chamar a ventá donde rexistramos aos
        asegurados."""

        self.ventanaUI = UiAseguradora.ventanaPrincipal()
        try:

            self.cursor.execute('Select * from Admin where Nombre =? and Password =?', (nombre,password))
            if self.cursor.fetchone() is  None :
              print('')
              """Añadido messagedialog 2.0 llamando al método de uiaseguradora error"""
              self.ventanaUI.error("Usuario ou contrasinal non validos")
            else:
                print("Benvido")
                UiRexistro.ventanaPrincipal()




        except dbapi.OperationalError:
            print("No se pudo conectar a la base")


    def print(self):

        """Usado para Crea-la taboa e chamar ao cursor e recheala taboa,nela damoslle as diferentes características a taboa,cor,tamaño,bordes e incluso imaxe."""


        imagen = Image(os.path.realpath("zs.jpg"),width=300,height=200)
        try:
            guion =[]
            guion.append(imagen)

            cabecera = [["Poliza", "Nombre", "Apellidos", "Dni", "Direccion", "Telefono", "Sexo", "Tipo", "Inicio","Fin"]]

            data = self.cursor.execute("select * from asegurados").fetchall()
            tabla = Table(cabecera+data)


        except dbapi.OperationalError:
            print("No se pudo conectar a la base")


        tabla.setStyle((["BOX",(0,0),(-1,-1),1.0,colors.black],["INNERGRID",(0,0),(-1,-1),0.25,colors.black],["TEXTCOLOR",(1,0),(9,0),colors.green],["TEXTCOLOR",(0,0),(0,0),colors.red],
                        ["BACKGROUND",(0,1),(9,9),colors.lightgrey]))
        guion.append(tabla)
        doc = SimpleDocTemplate("InformeAsegurados.pdf",pagesize=A4)
        doc.build(guion)


    def printPoliza(self):

        """Crease a taboa propia para a creación do informe de Pốliza."""

        imagen = Image(os.path.realpath("zs.jpg"), width=300, height=200)
        try:
            guion = []
            guion.append(imagen)

            cabecera = [["Poliza", "Tipo", "Inicio", "Fin"]]


            data = self.cursor.execute("select Poliza,Seguro,Fechaini,Fechafin from asegurados").fetchall()
            tabla = Table(cabecera + data)


        except dbapi.OperationalError:
            print("No se pudo conectar a la base")

        tabla.setStyle((["BOX", (0, 0), (-1, -1), 1.0, colors.black],
                        ["INNERGRID", (0, 0), (-1, -1), 0.25, colors.black],
                        ["TEXTCOLOR", (1, 0), (3, 0), colors.green], ["TEXTCOLOR", (0, 0), (0, 0), colors.red],
                        ["BACKGROUND", (0, 1), (-1, -1), colors.lightgrey]))
        guion.append(tabla)
        doc = SimpleDocTemplate("InformePolizas.pdf", pagesize=A4)
        doc.build(guion)