from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from tela_perfil import PerfilWindow
from telas.ui_scOrganizar import Ui_MainWindow
import pymysql

class ScOrganizarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.lblNome.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.ui.lblCurso.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.ui.btnPerfil.clicked.connect(self.telaPerfil)

        #try:
        self.ui.btnTarefas.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.pgTarefas))
        self.ui.btnPomodoro.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.pgPomodoro))
        self.ui.btnMatriz.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.pgMatriz))
        self.ui.btnCalendario.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.pgCalendario))
        self.ui.btnDesempenho.clicked.connect(
            lambda: self.ui.paginas.setCurrentWidget(self.ui.pgDesempenho))
        
        self.ui.btnMenuLargo.clicked.connect(self.expandir_menu)
        
                    
    def telaPerfil(self):
        self.perfil_window = PerfilWindow()
        self.perfil_window.show()
        self.close()
            
    def expandir_menu(self):
        width = self.ui.menuLateral.width()
        if width == 50:
            newWidth = 200
        elif width == 200:
            newWidth = 50
            
        try:
            self.animation = QPropertyAnimation(self.ui.menuLateral, b"minimumWidth")
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setDuration(350)
            self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
            self.animation.start()
            
        except:
            
            self.animation.setStartValue(50)
            self.animation.setEndValue(50)
            self.animation.setDuration(350)
            self.animation.setEasingCurve(QEasingCurve.Type.InOutCubic)
            self.animation.start()
                    
    #def conectar_banco(self):
        