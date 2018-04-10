import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import UiAseguradora
import ControladorAsegurados
import AseguradosTreeView




class ventanaPrincipal(Gtk.Window):

    """Nesta vista recollense os datos dos asegurados,por medio de métodos chamados da clase ComtropladorAsegurados interacciono cos eventos e botons
    usada pra recollelos datos dos asegurados,chamando aos diferentes métodos da clase Controlador asegurados e pasandolle parámetros."""

    def __init__(self):

        Gtk.Window.__init__(self)
        self.set_border_width(10)
        self.set_position(3)
        self.set_size_request(500,650)

        cabecera = Gtk.HeaderBar(title="REXISTRO")
        cabecera.set_subtitle("V 2.0")
        cabecera.props.show_close_button = True
        self.insertar = ControladorAsegurados.Controlador()
        self.cajaV  = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing =5)
        self.cajaLienzo = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing =3)
        self.cajaLienzo1 = Gtk.Box(orientation =Gtk.Orientation.VERTICAL,spacing =3)
        self.cajaLienzo2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=3)
        self.cajaNombre = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL,spacing=5)
        self.cajaDni = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL,spacing=5)
        self.cajaDireccion = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL,spacing=5)
        self.cajaPoliza = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL,spacing=5)
        self.cajaBotones = Gtk.Box(orientation =Gtk.Orientation.VERTICAL,spacing=5)
        self.cajaTipo = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL,spacing=5)
        self.cajaMarca = Gtk.Box(orientation =Gtk.Orientation.HORIZONTAL,spacing=5)
        self.cajaMarca.set_margin_top(10)
        self.cajaMarca.set_margin_bottom(10)
        self.cajaDireccion.set_margin_bottom(10)
        self.cajaBotones.set_margin_top(20)
        self.cajaBotones.set_margin_bottom(10)
        self.cajaPoliza.set_margin_top(10)
        self.cajaPoliza.set_margin_bottom(10)
        self.cajaDireccion.set_margin_top(10)
        self.cajaDni.set_margin_top(10)



        self.lienzo = Gtk.Frame()
        self.lienzo1 = Gtk.Frame()
        self.lienzo2 = Gtk.Frame()
        self.lienzo.set_margin_bottom(20)
        self.lienzo.set_label("Datos Personales Del Asegurado")
        self.lienzo1.set_label("Datos De la Póliza")
        self.btnGuardar = Gtk.Button("GUARDAR")
        self.lblFechaIni = Gtk.Label("Fecha de inicio")
        self.lblFechaIni.set_padding(10,10)
        self.lblFechaFinal = Gtk.Label("Fecha Finalización Póliza")
        self.lblFechaFinal.set_padding(10,10)
        self.btnEliminar = Gtk.Button("ELIMINAR")
        self.btnGuardar.set_margin_bottom(10)

        self.btnEliminar.set_margin_bottom(10)
        self.btnBuscar = Gtk.Button("CONSULTAR")
        self.btnBuscar.set_margin_bottom(10)
        self.btnModificar = Gtk.Button("MODIFICAR")
        self.btnModificar.set_margin_bottom(10)
        self.btnVolver = Gtk.Button("VOLVER")
        self.btnVolver.set_margin_bottom(10)
        self.lblNombre = Gtk.Label("Nombre")
        self.lblMatricula = Gtk.Label("Número de Póliza")
        self.lblMatricula.set_padding(10,10)
        self.entradaMatricula = Gtk.Entry()
        self.comboSexo = Gtk.ComboBoxText()
        self.comboSexo.set_margin_left(40)
        self.comboSexo.insert(0,"0","Mujer")
        self.comboSexo.insert(1,"1","Hombre")
        self.lblTipo = Gtk.Label("Tipo")
        self.lblTipo.set_padding(10,10)

        self.entradaInicio = Gtk.Entry()
        self.entradaInicio.set_margin_left(15)
        self.entradaFinal  = Gtk.Entry()



        self.comboTipo = Gtk.ComboBoxText()
        self.comboTipo.set_margin_left(73)
        self.comboTipo.insert(0,"0","tipo")
        self.comboTipo.insert(1,"1","Hogar")
        self.comboTipo.insert(2,"2","Coche")
        self.comboTipo.insert(3,"3","Vida")
        self.comboTipo.insert(4,"4","Salud")
        self.comboTipo.insert(5,"5","Dental")
        self.lblPoliza = Gtk.Label("Número de Póliza")
        self.lblPoliza.set_padding(10,10)
        self.entradaPóliza = Gtk.Entry()
        self.entradaPóliza.set_margin_left(1)
        self.lblTelefono = Gtk.Label("Teléfono")
        self.lblTelefono.set_padding(10,10)
        self.lblTelefono.set_margin_left(54)
        self.lblTelefono.set_margin_right(10)
        self.entradaTelf = Gtk.Entry()
        self.entradaTelf.set_margin_right(10)
        self.entradaTelf.set_margin_left(10)
        self.lblDireccion = Gtk.Label("Dirección")
        self.lblDireccion.set_padding(10,10)
        self.entradaDir = Gtk.Entry()

        self.lblNombre.set_padding(10,10)
        self.lblApellidos = Gtk.Label("Apellidos")
        self.lblApellidos.set_margin_left(55)
        self.lblApellidos.set_margin_right(20)
        self.lblDni = Gtk.Label("DNI")
        self.lblDni.set_padding(10,10)
        self.cajaNombre.set_margin_top(10)
        self.cajaDni.set_margin_top(10)
        self.lblSexo = Gtk.Label("Sexo")
        self.lblSexo.set_padding(10,10)
        self.lblSexo.set_margin_left(55)
        self.cajaDireccion.add(self.lblDireccion)
        self.cajaDireccion.add(self.entradaDir)
        self.cajaDireccion.add(self.lblTelefono)
        self.cajaDireccion.add(self.entradaTelf)
        self.cajaPoliza.add(self.lblPoliza)
        self.cajaPoliza.add(self.entradaPóliza)
        self.cajaTipo.add(self.lblTipo)
        self.cajaTipo.add(self.comboTipo)


        self.cajaMarca.add(self.lblFechaIni)
        self.cajaMarca.add(self.entradaInicio)
        self.cajaMarca.add(self.lblFechaFinal)
        self.cajaMarca.add(self.entradaFinal)


        self.entradaDNI = Gtk.Entry()
        self.entradaDNI.set_margin_left(30)
        self.entradaNombre = Gtk.Entry()
        self.entradaNombre.set_margin_left(9)
        self.entradaNombre.set_margin_right(10)
        self.entradaApellidos = Gtk.Entry()
        self.entradaApellidos.set_margin_right(1)
        self.entradaApellidos.set_margin_left(5)
        self.cajaNombre.add(self.lblNombre)
        self.cajaNombre.add(self.entradaNombre)
        self.cajaNombre.add(self.lblApellidos)
        self.cajaNombre.add(self.entradaApellidos)
        self.cajaDni.add(self.lblDni)
        self.cajaDni.add(self.entradaDNI)
        self.cajaDni.add(self.lblSexo)
        self.cajaDni.add(self.comboSexo)



        self.cajaBotones.add(self.btnGuardar)
        self.cajaBotones.add(self.btnModificar)
        self.cajaBotones.add(self.btnBuscar)
        self.cajaBotones.add(self.btnEliminar)
        self.cajaBotones.add(self.btnVolver)
        self.cajaLienzo.add(self.cajaNombre)
        self.cajaLienzo.add(self.cajaDni)
        self.cajaLienzo.add(self.cajaDireccion)
        self.cajaLienzo1.add(self.cajaPoliza)
        self.cajaLienzo1.add(self.cajaTipo)
        self.cajaLienzo1.add(self.cajaMarca)
        self.cajaLienzo2.add(self.cajaBotones)

        #Empiezo a recoger las entradas de texto y combos
        #Recollo os datos a través de combos e entradas de texto


        self.lienzo.add(self.cajaLienzo)
        self.lienzo1.add(self.cajaLienzo1)
        self.lienzo2.add(self.cajaLienzo2)
        self.cajaV.add(cabecera)
        self.cajaV.add(self.lienzo)
        self.cajaV.add(self.lienzo1)
        self.cajaV.add(self.lienzo2)
        self.add(self.cajaV)
        self.show_all()

        self.btnVolver.connect("clicked", self.on_button_clicked)
        self.btnModificar.connect("clicked", self.on_button_clicked)
        self.btnBuscar.connect("clicked",self.on_button_clicked)
        self.connect("delete-event",Gtk.main_quit)
        self.btnGuardar.connect("clicked",self.on_button_clicked)
        self.btnEliminar.connect("clicked",self.on_button_clicked)

    def inserta(self):

        """Usado para recoller os campos a rechear na base de datos e chama ao método insertar datos da clase ControladorAsegurados
        Recibindo as entradas por parámetro."""

        self.nombre = self.entradaNombre.get_text()
        self.apellidos = self.entradaApellidos.get_text()
        self.dni = self.entradaDNI.get_text()
        self.direccion = self.entradaDir.get_text()
        self.telefono = self.entradaTelf.get_text()
        self.poliza = self.entradaPóliza.get_text()
        self.fechaini = self.entradaInicio.get_text()
        self.fechafin = self.entradaFinal.get_text()
        self.seguro = self.comboTipo.get_active_text()
        self.sexo  = self.comboSexo.get_active_text()
        self.insertar.insertar_datos(self.poliza,self.nombre,self.apellidos,self.dni,self.direccion,self.telefono,self.sexo,self.seguro,self.fechaini,self.fechafin)


    def limpiar(self):

        """Usado para resetealos campos do rexistro."""

        self.entradaNombre.set_text("")
        self.entradaPóliza.set_text("")
        self.entradaInicio.set_text("")
        self.entradaApellidos.set_text("")
        self.entradaPóliza.set_text("")
        self.entradaTelf.set_text("")
        self.entradaMatricula.set_text("")
        self.entradaFinal.set_text("")
        self.entradaDNI.set_text("")

        self.comboTipo.set_active(False)
        self.comboSexo.set_active(False)


    def on_button_clicked(self, boton):


        """Neste outro método recollense os botóns
        no boton volver ocultase esta ventá e chamase a ventanaUI
        o botón buscar queda para ampliación do proxecto,inda non teño decidido como implementalo no futuro
        o botón modificar que chama a ventá asegurados treeview e oculta este,en aseguradosTreeView temos as
        taboas que acceden a base de datos e donde temos todos os asegurados,mellorado pra con un auxiliar validar e mostrar o cadro de dialogo e infdrmar
        de que a insercción fixose con éxito"""

        if boton == self.btnVolver:
            #self.ventanaUI.set_visible(True)
            self.set_visible(False)
        if boton == self.btnBuscar:
            self.ventanaAsegurados = AseguradosTreeView.VentanaPrincipal()
            self.set_visible(False)
            self.ventanaAsegurados.set_visible(True)
        if boton== self.btnGuardar:
            aux = True

            if aux == True:
                self.inserta()

                dialogo = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                            Gtk.ButtonsType.CLOSE, "Cliente añadido con éxito")

                dialogo.set_position(3)
                dialogo.run()
                dialogo.destroy()
                dialogo.destroy()
            else:
                aux==False
        if boton == self.btnModificar:
            self.ventanaAsegurados = AseguradosTreeView.VentanaPrincipal()
            self.set_visible(False)
            self.ventanaAsegurados.set_visible(True)

        if boton == self.btnEliminar:
           self.limpiar()







if __name__ == "__main__":
    ventanaPrincipal()
    Gtk.main()
