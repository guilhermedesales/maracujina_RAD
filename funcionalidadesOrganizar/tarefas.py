import pymysql
from PyQt6.QtWidgets import QMessageBox, QInputDialog
from PyQt6.QtGui import QKeySequence, QShortcut
from .gerar_pdf import gerar_pdf


class Tarefas:
    def __init__(self, ui, id_usuario):
        self.ui = ui
        self.id_usuario = id_usuario
        
        self.ui.btnAddTask.clicked.connect(self.adicionar_tarefa)
        self.ui.btnDeleteTask.clicked.connect(self.remover_tarefa)
        self.ui.btnCleanTaskList.clicked.connect(self.limpar_lista)
        self.ui.btnEditTask.clicked.connect(self.editar_tarefa)
        self.ui.btnPDF.clicked.connect(self.gerar_pdf_usuario)


        self.carregar_do_bd()

        # Atalhos de teclado
        QShortcut(QKeySequence("E"), self.ui.taskList, self.remover_tarefa)
        self.ui.txtTask.returnPressed.connect(self.adicionar_tarefa)
        
    def conectar_banco(self):
        return pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='db_maracujina',
            connect_timeout=5
        )
        
    def gerar_pdf_usuario(self):
        caminho = gerar_pdf(self.id_usuario)
        if caminho:
            QMessageBox.information(None, "PDF Gerado", f"PDF salvo em:\n{caminho}")
        else:
            QMessageBox.critical(None, "Erro", "Erro ao gerar o PDF.")


    # add tarefa ao bd e a lista de tarefas
    def adicionar_tarefa(self):
        task = self.ui.txtTask.text().strip()
        if not task:
            QMessageBox.warning(None, "Aviso", "Digite uma tarefa antes de adicionar.")
            return

        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tarefas (id_usuario, nome_tarefa)
                VALUES (%s, %s)
            """, (self.id_usuario, task))
            conn.commit()
            cursor.close()
            conn.close()

            self.ui.taskList.addItem(task)
            self.ui.txtTask.setText("")
        except Exception as e:
            print(f"Erro ao salvar tarefa no banco: {e}")
            QMessageBox.critical(None, "Erro", "Erro ao salvar tarefa no banco.")

    def remover_tarefa(self):
        row = self.ui.taskList.currentRow()
        if row == -1:
            QMessageBox.information(None, "Aviso", "Selecione uma tarefa para remover.")
            return

        tarefa = self.ui.taskList.item(row).text()
        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM tarefas
                WHERE id_usuario = %s AND nome_tarefa = %s
                LIMIT 1
            """, (self.id_usuario, tarefa))
            conn.commit()
            cursor.close()
            conn.close()

            self.ui.taskList.takeItem(row)
        except Exception as e:
            print(f"Erro ao remover tarefa do banco: {e}")
            QMessageBox.critical(None, "Erro", "Erro ao remover tarefa do banco.")
            
    ##função para editar tarefa
    def editar_tarefa(self):
        row = self.ui.taskList.currentRow()
        if row == -1:
            QMessageBox.information(None, "Aviso", "Selecione uma tarefa para editar.")
            return

        tarefa_antiga = self.ui.taskList.item(row).text()

        nova_tarefa, ok = QInputDialog.getText(
            None,

            "Editar Tarefa",
            "Digite o novo nome da tarefa:",
            text=tarefa_antiga
        )

        if ok and nova_tarefa.strip():
            nova_tarefa = nova_tarefa.strip()
            try:
                conn = self.conectar_banco()
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE tarefas
                    SET nome_tarefa = %s
                    WHERE id_usuario = %s AND nome_tarefa = %s
                    LIMIT 1
                """, (nova_tarefa, self.id_usuario, tarefa_antiga))
                conn.commit()
                cursor.close()
                conn.close()

                self.ui.taskList.item(row).setText(nova_tarefa)
            except Exception as e:
                print(f"Erro ao editar tarefa no banco: {e}")
                QMessageBox.critical(None, "Erro", "Erro ao editar tarefa no banco.")
        else:
            QMessageBox.information(None, "Aviso", "Nenhuma alteração feita.")

    

    def limpar_lista(self):
        if self.ui.taskList.count() == 0:
            QMessageBox.information(None, "Aviso", "A lista já está vazia.")
            return

        resposta = QMessageBox.question(
            None,
            "Confirmação",
            "Tem certeza que deseja apagar todas as tarefas?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if resposta == QMessageBox.StandardButton.Yes:
            try:
                conn = self.conectar_banco()
                cursor = conn.cursor()
                cursor.execute("""
                    DELETE FROM tarefas WHERE id_usuario = %s
                """, (self.id_usuario,))
                conn.commit()
                cursor.close()
                conn.close()

                self.ui.taskList.clear()
            except Exception as e:
                print(f"Erro ao limpar tarefas do banco: {e}")
                QMessageBox.critical(None, "Erro", "Erro ao limpar tarefas do banco.")

    def carregar_do_bd(self):
        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT nome_tarefa FROM tarefas
                WHERE id_usuario = %s
            """, (self.id_usuario,))
            tarefas = cursor.fetchall()
            cursor.close()
            conn.close()

            for tarefa in tarefas:
                self.ui.taskList.addItem(tarefa[0])
        except Exception as e:
            print(f"Erro ao carregar tarefas do banco: {e}")
            QMessageBox.critical(None, "Erro", "Erro ao carregar tarefas do banco.")
