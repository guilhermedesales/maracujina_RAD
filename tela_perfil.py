from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from telas.ui_telaPerfil import Ui_MainWindow

class PerfilWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)