import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
import UiRexistro
import ControladorAsegurados


class ventanaPrincipal(Gtk.Window):

    """Clase de login,e a primeira venta,usada simplemente pra poder acceder a xestion da aseguradora
     O contrasinal pra acceder que teño rexistrado e user mario,contrasinal 12345.
     """
    def __init__(self):

        Gtk.Window.__init__(self)
        self.set_border_width(10)
        self.set_position(3)

        cabecera = Gtk.HeaderBar(title="ZURICH.SL")
        cabecera.set_subtitle("V 2.0")
        cabecera.props.show_close_button = True

        self.caixaV =Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 6)
        self.cajaUsuario = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing=2)
        self.botonEntrar = Gtk.Button("Acceder")



        self.entradaUsuario = Gtk.Entry()
        self.entradaPass = Gtk.Entry()
        self.entradaUsuario.set_margin_right(10)
        self.entradaPass.set_margin_left(10)
        self.entradaPass.set_visibility(False)
        lblNombre = Gtk.Label("USUARIO")
        lblNombre.set_margin_right(10)
        lblNombre.set_margin_left(15)
        lblPassword = Gtk.Label("CONTRASEÑA")
        lblPassword.set_margin_left(20)

        lblPassword.set_margin_right(10)
        self.cajaLienzo = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing =3)
        image = Gtk.Image()
        """OLLO!!!! cambiala ruta se a imaxe non se visualiza correctamenente na portada"""
        image.set_from_file('ZURICH.png')
        self.add(self.caixaV)

        self.caixaV.add(cabecera)
        self.caixaV.add(image)
        self.caixaV.add(self.cajaUsuario)
        self.cajaUsuario.add(lblNombre)
        self.cajaUsuario.add(self.entradaUsuario)
        self.cajaUsuario.add(lblPassword)
        self.cajaUsuario.add(self.entradaPass)












        self.show_all()
        self.connect("delete-event",Gtk.main_quit)
        self.connect("key_press_event",self.login)


    def error(self,mensaje):

        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                   Gtk.ButtonsType.OK, "ERRO")
        dialog.format_secondary_text(
            mensaje)
        dialog.set_position(3)
        dialog.run()
        dialog.destroy()

    def login(self,usuario,password):

        """Accede insertando os datos de nome e password e pulsando a tecla enter,sen botón,faise a comprobación de que os campos
        non estean valeiros a través dun if,que di que se teñen lonxitude 0 nos de a mesaxe os campos non poden estar valeiros
        e se non,que chame ao método de login o cal fai a comprobación,no outro if else que podese ver no método login,se está
        pecha esta ventá e chama a de Uirexistro pra poder rexistrar un novo asegurado.

        """

        if(password.keyval==65293):

            usuari = self.entradaUsuario.get_text()
            passwor = self.entradaPass.get_text()

            if(len(usuari)==0 or len(passwor)==0):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                           Gtk.ButtonsType.OK, "ERRO")
                dialog.format_secondary_text(
                    "Non Pode haber campos valeiros.")
                dialog.set_position(3)
                dialog.run()
                dialog.destroy()

            else:

             comprobacion = ControladorAsegurados.Controlador()
             comprobacion.login(usuari,passwor)
             self.destroy()








if __name__ == "__main__":
    ventanaPrincipal()
    Gtk.main()
