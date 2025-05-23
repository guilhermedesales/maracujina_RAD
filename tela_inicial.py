from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from telas.ui_telaInicial import Ui_MainWindow

class TelaInicial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            self.ui.btn1.clicked.connect(
                lambda: self.ui.paginas.setCurrentWidget(self.ui.pg_tarefas))
            self.ui.btn2.clicked.connect(
                    lambda: self.ui.paginas.setCurrentWidget(self.ui.page_2))
            
        except Exception as e:
            print(f"erro ao iniciar a tela inicial {e}")