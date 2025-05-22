from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from telas.ui_telaInicial import Ui_MainWindow

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    