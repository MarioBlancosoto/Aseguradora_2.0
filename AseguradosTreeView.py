import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import ControladorAsegurados
import UiRexistro


class VentanaPrincipal(Gtk.Window):
    """Aquí podense ver,modificar e borralos datos refentes aos asegurados
    a mesma interactua con controladorAsegurados para poder acceder a base de datos"""

    def __init__(self):
        Gtk.Window.__init__(self,title ='TreeView')
        self.set_border_width(10)
        self.set_position(3)
        self.set_size_request(500,650)
        self.ventanaPrint = ControladorAsegurados.Controlador()


        self.cajaBotones = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.btnEliminar = Gtk.Button("ELIMINAR")
        self.btnVolver = Gtk.Button("VOLVER")

        self.btnInforme = Gtk.Button("INFORME XERAL")
        self.btnInformePoliza = Gtk.Button("INFORME PÓLIZAS")
        self.btnEliminar.set_margin_right(70)
        self.btnInforme.set_margin_right(70)
        self.btnInformePoliza.set_margin_right(70)
        self.cajaBotones.add(self.btnEliminar)
        self.cajaBotones.add(self.btnInforme)
        self.cajaBotones.add(self.btnInformePoliza)
        self.cajaBotones.add(self.btnVolver)
        cabecera = Gtk.HeaderBar(title="LISTADO ASEGURADOS")
        cabecera.set_subtitle("V 2.0")
        cabecera.props.show_close_button = True
        controlador = ControladorAsegurados.Controlador()

        columnas = ["Poliza","Nombre","Apellidos","Dni","Direccion","Telefono","Sexo","Seguro","Fechaini","Fechafin"]

        lista = controlador.mostrarTabla()
        modelo = Gtk.ListStore(str,str,str,str,str,str,str,str,str,str)
        #creamolo modelo coas columnas,e damoslle as caracteristicas de editable por celda e columna
        for i in lista:

            modelo.append(i)

        vista = Gtk.TreeView(model = modelo)
        caixaH  = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing=5)
        caixaH.add(cabecera)


        for i in range(len(columnas)):
            celda = Gtk.CellRendererText(editable=True)
            columna = Gtk.TreeViewColumn(columnas[i],celda,text =i)
            celda.connect("edited",self.on_celda_changed,modelo,i,columnas[i])

            vista.append_column(columna)


        vista.connect("key_press_event",self.on_celda_erase)
        caixaH.pack_start(vista,False,False,0)
        caixaH.add(self.cajaBotones)
        self.add(caixaH)

        self.btnEliminar.connect("clicked",self.borrar,vista)
        self.btnVolver.connect("clicked",self.volver)
        self.btnInforme.connect("clicked",self.printar)
        self.btnInformePoliza.connect("clicked",self.printarPoliza)

        self.show_all()
        self.connect("delete-event",Gtk.main_quit)


    """Este método e bastante completo,xa que recolle a iteración da fila,pero sempre a columna 0,isto debese a que cando chamamos
    ao método UPDATE este debe recoller sempre o primary key,neste caso e a columna 0,e temos que recoller tamén a fila na que se 
    atopa nese momento clikada,ao facer click e co evento edited podemos modificar a vez o módelo para aprecialo visualmente
    e a vez facemolo update na taboa,deste xeito facemolo todo mais sinsxelo ao poder modificalos datos directamente na mesma.
    o método modificar dato recibe os 3 parámetros,os novos datos,textocelda,da fila seleccinada,a id,sempre columna 0 e a fila neste
    caso o (fila) o indice"""

    def on_celda_changed(self,punteiro,fila,textoCelda,modelo,col,colName):

       actualizacion = ControladorAsegurados.Controlador()
       actualizacion.modificarDatos(colName,textoCelda,modelo[fila][0])
       modelo[fila][col] = textoCelda



    def on_celda_erase(self,modelo,evento):

        """Este tamén e outro método interesante,nel a través do evento keypressed podemos borrar o asegurado da fila na que se atopa
        seleccionada,de novo a través dun mnétodo,desta vez do getSelectedRow o cal recolle a columna,de novo neste caso borramos pola id
        que sempre e o 0 e iteramos polas filas co for,chamamos ao método borrarDatos e lle pasamos o ID,neste caso a fila seleccionada co
        [i] e sempre a coolumna 0 xa que ea primary key, e lle damos o valor da fila e columna a ID que e a variable que vai recollela
        función borrarDatos ."""

        #Dato de interes : recollín as teclas de retroceso e delete porque no macbook non teño a tecla de delete,so a de retroceso,con esas duas podese borrar
        borrar = ControladorAsegurados.Controlador()

        print(evento.keyval)
        if (evento.keyval==65288 or evento.keyval==65535):
            seleccion = modelo.get_selection().get_selected_rows()
            idSeleccion=modelo.get_model()
            for i in seleccion[1]:

                iter=modelo.get_model().get_iter(i)
                id = idSeleccion[i][0]
                print(id)
                borrar.borrarDatos(id)
                modelo.get_model().remove(iter)

    def borrar(self,boton,modelo):

        """Método 2.0 listener pra añadir un botón e un questionDialog para validar un borrado si clickamos en si."""

        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.QUESTION,
                                   Gtk.ButtonsType.YES_NO, "Está seguro de que quere borralo rexistro??")

        response = dialog.run()
        if response == Gtk.ResponseType.YES:

            borrar = ControladorAsegurados.Controlador()
            seleccion = modelo.get_selection().get_selected_rows()
            idSeleccion = modelo.get_model()

            for i in seleccion[1]:
                iter = modelo.get_model().get_iter(i)
                id = idSeleccion[i][0]
                borrar.borrarDatos(id)
                modelo.get_model().remove(iter)

                dialog2 = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                            Gtk.ButtonsType.CLOSE, "Eliminado con éxito")

                dialog2.set_position(3)
                dialog2.run()
                dialog2.destroy()
                dialog.destroy()


        elif response == Gtk.ResponseType.NO:

            dialog1 = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                       Gtk.ButtonsType.CLOSE, "Eliminación Cancelada")

            dialog1.set_position(3)
            dialog1.run()
            dialog1.destroy()
            dialog.destroy()





    def volver(self,boton):

        """Pra volver a pantalla anterior,neste caso UiRexistro."""

        ventanaRexistro = UiRexistro.ventanaPrincipal()
        ventanaRexistro.set_visible(True)
        self.destroy()


    def printar(self,boton):

        """Aquí chamase ao método pra poder xenera-lo inform,a chamada e a controladorAsegurados ,no que facemola taboa recheando os campos coa consulta da base
        Valido se a xeneración do informe foi correcta mediante o añadido de diálogos pra mostrar as diferentes accions por pantalla."""

        aux = True

        if aux == True :
            self.ventanaPrint.print()

            dialogo = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                        Gtk.ButtonsType.CLOSE, "Impresión realizada con éxito")

            dialogo.set_position(3)
            dialogo.run()
            dialogo.destroy()
            dialogo.destroy()

        else :
            aux ==False
            self.ventanaPrint.print()

            dialogo = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                        Gtk.ButtonsType.CLOSE, "Erro na impresión")

            dialogo.set_position(3)
            dialogo.run()
            dialogo.destroy()
            dialogo.destroy()



    def printarPoliza(self,boton):

        """Feito para xerar o segundo informe no cal recollemos so certos datos."""

        aux =True

        if aux == True :
            self.ventanaPrint.printPoliza()

            dialogo = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                        Gtk.ButtonsType.CLOSE, "Impresión realizada con éxito")

            dialogo.set_position(3)
            dialogo.run()
            dialogo.destroy()
            dialogo.destroy()

        else :
            aux ==False
            self.ventanaPrint.printPoliza()

            dialogo = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                        Gtk.ButtonsType.CLOSE, "Erro na impresión")

            dialogo.set_position(3)
            dialogo.run()
            dialogo.destroy()
            dialogo.destroy()















if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()

