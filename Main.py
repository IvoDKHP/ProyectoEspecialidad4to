import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot

"""
from Archivo convertido con pyside2-uic archivo.ui > interfaz.py
import nombre de la clase del archivo convertido
"""
from Ui_menu import Ui_MainWindow
from Ui_configuracion import Ui_MainWindow

class MainWindow(QMainWindow):  #Clase MainWindow heredada de QMainWindow, que es una clase de PyQt para crear la ventana principal de la app.
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.ui = Ui_MainWindow() #crea una instancia de Ui_MainWindow class, la cual es la definición de la interfaz del usuario para la ventana principal.
        self.ui.setupUi(self) #llama al método setupUi() de la instancia Ui_MainWindow, para setear los componenetes de la interfaz del usuario dentro de main window.

    def cambiarventana(self):
        self.ui.pushButton.Ui_configuracion(Ui_MainWindow)
        self.Ui_configuracion.show()

    def volver(self):
        self.Menu = Ui_MainWindow()
        self.ui.pushButton.self.Menu.show()
        self.Ui_menu.show()

if __name__ == "__main__": #checkea si el script está siendo ejecutado como el prog principal (no importado como un modulo).
    app = QApplication(sys.argv)    # Crea un Qt widget, la cual va ser nuestra ventana.
    window = MainWindow() #crea una intancia de MainWindow 
    window.show()   # IMPORTANT!!!!! la ventanas estan ocultas por defecto.
    sys.exit(app.exec_()) # Start the event loop.