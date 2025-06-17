import pymysql
from PyQt6.QtWidgets import QMessageBox, QListWidgetItem
from PyQt6.QtGui import QKeySequence, QShortcut
from PyQt6.QtCore import Qt

class Tarefas:
    def __init__(self, ui, id_usuario):
        self.ui = ui
        self.id_usuario = id_usuario
        
        self.ui.btnAddTask.clicked.connect(self.adicionar_tarefa)
        self.ui.btnDeleteTask.clicked.connect(self.remover_tarefa)
        self.ui.btnCleanTaskList.clicked.connect(self.limpar_lista)
        self.ui.btnSalvar.clicked.connect(self.salvar_status_tarefas)

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

    def adicionar_tarefa(self):
        task = self.ui.txtTask.text().strip()
        if not task:
            QMessageBox.warning(None, "Aviso", "Digite uma tarefa antes de adicionar.")
            return

        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tarefas (id_usuario, nome_tarefa, status)
                VALUES (%s, %s, %s)
            """, (self.id_usuario, task, "NAO"))
            conn.commit()
            cursor.close()
            conn.close()

            item = QListWidgetItem(task)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.taskList.addItem(item)

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
                SELECT nome_tarefa, status FROM tarefas
                WHERE id_usuario = %s
            """, (self.id_usuario,))
            tarefas = cursor.fetchall()
            cursor.close()
            conn.close()

            self.ui.taskList.clear()
            for nome, status in tarefas:
                item = QListWidgetItem(nome)
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
                item.setCheckState(Qt.CheckState.Checked if status == "SIM" else Qt.CheckState.Unchecked)
                self.ui.taskList.addItem(item)
        except Exception as e:
            print(f"Erro ao carregar tarefas do banco: {e}")
            QMessageBox.critical(None, "Erro", "Erro ao carregar tarefas do banco.")

    def salvar_status_tarefas(self):
        try:
            conn = self.conectar_banco()
            cursor = conn.cursor()

            for i in range(self.ui.taskList.count()):
                item = self.ui.taskList.item(i)
                nome = item.text()
                status = "SIM" if item.checkState() == Qt.CheckState.Checked else "NAO"

                cursor.execute("""
                    UPDATE tarefas
                    SET status = %s
                    WHERE id_usuario = %s AND nome_tarefa = %s
                """, (status, self.id_usuario, nome))

            conn.commit()
            cursor.close()
            conn.close()

            QMessageBox.information(None, "Sucesso", "Status das tarefas atualizado.")
        except Exception as e:
            print(f"Erro ao salvar status das tarefas: {e}")
            QMessageBox.critical(None, "Erro", "Erro ao salvar status das tarefas.")
