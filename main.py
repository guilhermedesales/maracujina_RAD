from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from telas.ui_telaLogin import Ui_MainWindow
from tela_login import LoginWindow
import sys
import res_rc

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
