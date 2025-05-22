from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from telas.ui_telaLogin import Ui_MainWindow
from tela_registrar import RegistrarWindow
from tela_inicial import TelaInicial
from seguranca.senhaHash import verificar_senha
import pymysql
#import traceback

class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnConfirm.clicked.connect(self.verifica_login)
        self.ui.btnRegistrar.clicked.connect(self.telaRegistrar)

    # função abrir tela Registrar
    def telaRegistrar(self):
        self.registrar_window = RegistrarWindow()
        self.registrar_window.show()
        self.close()

    # função abrir tela Inicial
    def telaInicial(self):
        self.inicial_window = TelaInicial()
        self.inicial_window.show()
        self.close()

    # função conectar ao banco de dados
    def conectar_banco(self):
        return pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='db_maracujina',
                connect_timeout=5
            )
    
    # função pra validar o usuario
    def validar_usuario(self, matricula, senha):
        conexao = self.conectar_banco()
        cursor = conexao.cursor()

        query = """
                SELECT A.senha_hash 
                FROM autenticacoes A 
                JOIN usuarios U ON A.id_usuario = U.id_usuario
                WHERE U.matricula = %s 
         
            """
        try:
            cursor.execute(query, (matricula,)) 
            resultado = cursor.fetchone()

            if resultado:
                    senha_hash_banco = resultado[0]  # senha_hash armazenada no banco

                    if verificar_senha(senha, senha_hash_banco):
                        print("Login realizado com sucesso.")
                        self.telaInicial()
                    else:
                        print("Senha incorreta.")
                        mensagem = "Login ou senha incorretos."
                        self.ui.lblErro.setText(mensagem)
            else:
                    print("Usuário não encontrado.")
                    mensagem = "Login ou senha incorretos."
                    self.ui.lblErro.setText(mensagem)

            cursor.close()
            conexao.close()

        except Exception as e:
            print("Erro ao conectar:")
            mensagem = "Erro ao conectar ao banco de dados."
            self.ui.lblErro.setText(mensagem)

    # função verificar usuario no banco de dados
    def verifica_login(self):
        
            print("Botão clicado para verificar login")

            matricula = self.ui.txtLogin.text().strip() # pega o texto do campo de login
            senha = self.ui.txtSenha.text().strip() # pega o texto do campo de senha
            mensagem = self.ui.lblErro.text() # pega o texto do label de erro

            if not matricula or not senha: # verifica se os campos estão vazios
                mensagem = "Preencha todos os campos"
                self.ui.lblErro.setText(mensagem)
                return

            self.validar_usuario(matricula, senha)

        