from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.uic import loadUi
from telas.ui_telaLogin import Ui_MainWindow
from tela_registrar import RegistrarWindow
from sc_Organizar import ScOrganizarWindow
from db_config import dbConnect
import pymysql

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loadUi("ui/login.ui", self)
        #self.ui = Ui_MainWindow()
        #self.ui.setupUi(self)

        self.btnConfirm.clicked.connect(self.verifica_login)
        self.btnRegistrar.clicked.connect(self.telaRegistrar)

    def telaRegistrar(self):
        self.registrar_window = RegistrarWindow()
        self.registrar_window.show()
        self.close()

    def telaInicial(self, id_usuario):
        self.inicial_window = ScOrganizarWindow(id_usuario)
        self.inicial_window.show()
        self.close()

    def conectar_banco(self):
        return dbConnect()

    def validar_usuario(self, matricula, senha):
        conexao = self.conectar_banco()
        cursor = conexao.cursor()

        query = """
            SELECT U.id_usuario, A.senha 
            FROM autenticacoes A 
            JOIN usuarios U ON A.id_usuario = U.id_usuario
            WHERE U.matricula = %s
        """
        try:
            cursor.execute(query, (matricula,))
            resultado = cursor.fetchone()

            if resultado:
                id_usuario = resultado[0]
                senha_banco = resultado[1]

                if senha == senha_banco:
                    print("Login realizado com sucesso.")
                    self.telaInicial(id_usuario)
                else:
                    print("Senha incorreta.")
                    self.lblErro.setText("Login ou senha incorretos.")
            else:
                print("Usuário não encontrado.")
                self.lblErro.setText("Login ou senha incorretos.")

            cursor.close()
            conexao.close()

        except Exception as e:
            print("Erro ao conectar:")
            self.lblErro.setText("Falha ao conectar ao banco.")

    def verifica_login(self):
        print("Botão clicado para verificar login")

        matricula = self.txtLogin.text().strip()
        senha = self.txtSenha.text().strip()

        if not matricula or not senha:
            self.lblErro.setText("Preencha todos os campos")
            return

        self.validar_usuario(matricula, senha)
