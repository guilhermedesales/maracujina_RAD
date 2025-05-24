from PyQt6.QtWidgets import QMainWindow, QMessageBox
from telas.ui_telaRegistrar import Ui_MainWindow
from sc_Organizar import ScOrganizarWindow
from seguranca.senhaHash import gerar_hash
import pymysql
from PyQt6.QtCore import QDate

class RegistrarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnRegister.clicked.connect(self.registrar_usuario)
        self.ui.btnLogin.clicked.connect(self.telaLogin)

    def telaInicial(self): # abre a tela inicial
        self.inicial_window = ScOrganizarWindow()
        self.inicial_window.show()
        self.close()

    def telaLogin(self):
        from tela_login import LoginWindow
        self.inicial_window = LoginWindow()
        self.inicial_window.show()
        self.close()

    def registrar_usuario(self):

        nome = self.ui.txtNome.text().strip()
        matricula = self.ui.txtMatricula.text().strip()
        curso = self.ui.txtCurso.text().strip()
        celular = self.ui.txtCelular.text().strip()
        #dataNasc = self.ui.txtDtNasc.text().strip()
        senha = self.ui.txtSenha.text().strip()
        email = self.ui.txtEmail.text().strip()

        senha_hash = gerar_hash(senha)

        if not email or not senha:
                QMessageBox.warning(self, "Campos vazios", "Preencha todos os campos.")
                return
        try:
            conexao = pymysql.connect(
                 
                host='localhost',
                user='root',
                password='root',
                database='db_maracujina',
                connect_timeout=5
            )
            cursor = conexao.cursor()

            cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
            if cursor.fetchone():
                QMessageBox.warning(self, "Email já cadastrado", "Esse email já está cadastrado.")
                cursor.close()
                conexao.close()
                return
            
            query = "INSERT INTO usuarios (nome, email, matricula, curso, celular) VALUES (%s, %s,%s, %s, %s)"
            cursor.execute(query, (nome, email, matricula, curso, celular))

            id_usuario = cursor.lastrowid

            query = "INSERT INTO autenticacoes (id_usuario, senha_hash) VALUES (%s, %s)"
            cursor.execute(query, (id_usuario, senha_hash))

            conexao.commit()

            if cursor.rowcount > 0:
                print("Usuário registrado com sucesso.")
                self.telaInicial()


            QMessageBox.information(self, "Sucesso", "Usuário registrado com sucesso!")

            cursor.close()
            conexao.close()

        except Exception as e:
            QMessageBox.critical(self, "Erro de conexão", f"Erro:\n{e}")