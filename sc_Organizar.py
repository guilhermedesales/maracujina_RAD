from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, Qt
from tela_perfil import PerfilWindow
from telas.ui_scOrganizar import Ui_MainWindow
from funcionalidadesOrganizar.tarefas import Tarefas
from funcionalidadesOrganizar.pomodoro import Pomodoro
from funcionalidadesOrganizar.matriz import adicionar_tarefa_a_matriz
#from tela_login import LoginWindow

import pymysql

class ScOrganizarWindow(QMainWindow):
    def __init__(self, id_usuario):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.id_usuario = id_usuario

        self.ui.lblNome.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.ui.lblCurso.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        

        self.ui.btnPerfil.clicked.connect(self.telaPerfil)
        self.ui.btnMenuLargo.clicked.connect(self.expandir_menu)
        
        self.ui.btnUI.clicked.connect(self.adicionar_ui)
        self.ui.btnUN.clicked.connect(self.adicionar_un)
        self.ui.btnNI.clicked.connect(self.adicionar_ni)
        self.ui.btnNN.clicked.connect(self.adicionar_nn)
        
        self.ui.btnSair.clicked.connect(self.sair)

        self.carregar_tarefas_matriz()

        self.carregar_dados_usuario()

        self.botoes_menu = {
            self.ui.btnTarefas: self.ui.pgTarefas,
            self.ui.btnPomodoro: self.ui.pgPomodoro,
            self.ui.btnMatriz: self.ui.pgMatriz,
            #self.ui.btnCalendario: self.ui.pgCalendario,
            #self.ui.btnDesempenho: self.ui.pgDesempenho
        }

        for botao, pagina in self.botoes_menu.items():
            botao.clicked.connect(lambda checked, p=pagina, b=botao: self.trocar_pagina(p, b))

        self.trocar_pagina(self.ui.pgTarefas, self.ui.btnTarefas)

        #gerenciador de tarefas
        self.tarefas_widget = Tarefas(self.ui, self.id_usuario)

    def adicionar_ui(self):
        print("Botão UI clicado")
        nome = adicionar_tarefa_a_matriz(self, self.id_usuario, "UI")
        if nome:
            self.ui.listUI.addItem(nome)

    def adicionar_un(self):
        print("Botão UN clicado")
        nome = adicionar_tarefa_a_matriz(self, self.id_usuario, "UN")
        if nome:
            self.ui.listUN.addItem(nome)

    def adicionar_ni(self):
        print("Botão NI clicado")
        nome = adicionar_tarefa_a_matriz(self, self.id_usuario, "NI")
        if nome:
            self.ui.listNI.addItem(nome)

    def adicionar_nn(self):
        print("Botão NN clicado")
        nome = adicionar_tarefa_a_matriz(self, self.id_usuario, "NN")
        if nome:
            self.ui.listNN.addItem(nome)

    def carregar_tarefas_matriz(self):
        try:
            conexao = self.conectar_banco()
            with conexao.cursor() as cursor:
                cursor.execute("""
                    SELECT nome_tarefa, matriz
                    FROM tarefas
                    WHERE id_usuario = %s AND matriz IS NOT NULL
                """, (self.id_usuario,))
                tarefas = cursor.fetchall()

                for nome, matriz in tarefas:
                    if matriz == "UI":
                        self.ui.listUI.addItem(nome)
                    elif matriz == "UN":
                        self.ui.listUN.addItem(nome)
                    elif matriz == "NI":
                        self.ui.listNI.addItem(nome)
                    elif matriz == "NN":
                        self.ui.listNN.addItem(nome)
        except Exception as e:
            print(f"[ERRO] ao carregar tarefas da matriz: {e}")
        finally:
            conexao.close()

    
    def telaPerfil(self):
        self.perfil_window = PerfilWindow()
        self.perfil_window.show()
        self.close()
        
    def sair(self):
        from tela_login import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()


    def expandir_menu(self):
        width = self.ui.menuLateral.width()
        newWidth = 200 if width == 50 else 50
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

    def trocar_pagina(self, pagina, botao_ativo):
        self.ui.paginas.setCurrentWidget(pagina)
        for botao in self.botoes_menu.keys():
            botao.setChecked(botao == botao_ativo)
            
        if pagina == self.ui.pgPomodoro:
            self.pomodoro_widget = Pomodoro(self.ui)

    def conectar_banco(self):
        return pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='db_maracujina',
            connect_timeout=5
        )

    def carregar_dados_usuario(self):
        try:
            conexao = self.conectar_banco()
            cursor = conexao.cursor()
            query = """
                SELECT U.nome, U.curso
                FROM usuarios U
                WHERE U.id_usuario = %s
            """
            cursor.execute(query, (self.id_usuario,))
            resultado = cursor.fetchone()

            if resultado:
                nome, curso = resultado
                self.ui.lblNome.setText(nome)
                self.ui.lblCurso.setText(curso)
            else:
                print("Usuário não encontrado.")
                QMessageBox.critical(self, "Erro", "Usuário não encontrado.")
                self.ui.lblNome.setText("Aluno")
                self.ui.lblCurso.setText("Curso")

            cursor.close()
            conexao.close()
        except Exception as e:
            print(f"Erro ao carregar dados do usuário: {e}")
            QMessageBox.critical(self, "Erro", "Erro ao carregar dados do usuário.")
