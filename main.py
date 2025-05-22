from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from telas.ui_telaLogin import Ui_MainWindow
from tela_login import TelaLogin
import sys
import res_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaLogin()
    window.show()
    sys.exit(app.exec())
