from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QLineEdit, QLabel,
    QInputDialog, QHBoxLayout, QMessageBox, QCheckBox, QFrame
)
from PyQt6.QtCore import Qt


class TarefasWidget(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.dados_listas = {}  # {nome_lista: [(tarefa, completa)]}
        self.lista_atual = None

        self.ui.btnCriarLista.clicked.connect(self.criar_lista)

    def criar_lista(self):
        if len(self.dados_listas) >= 5:
            QMessageBox.warning(self, "Limite", "Máximo de 5 listas.")
            return

        nome, ok = QInputDialog.getText(self, "Nova Lista", "Nome da lista:")
        if ok and nome:
            if nome in self.dados_listas:
                QMessageBox.warning(self, "Erro", "Lista já existe.")
                return

            self.dados_listas[nome] = []

            botao_lista = QPushButton(nome)
            botao_lista.clicked.connect(lambda _, n=nome: self.exibir_tarefas(n))
            self.ui.layoutListasTarefas.layout().addWidget(botao_lista)

            self.atualizar_contagem()

    def exibir_tarefas(self, nome_lista):
        self.lista_atual = nome_lista

        # Limpa a área addTask
        add_layout = self.ui.addTask.layout()
        if add_layout is None:
            add_layout = QHBoxLayout()
            self.ui.addTask.setLayout(add_layout)
        while add_layout.count():
            item = add_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        self.ui.addTask.setFixedWidth(400)

        # Limpa a área Tarefas
        tarefas_layout = self.ui.Tarefas.layout()
        tarefas_layout.setSpacing(10)
        while tarefas_layout.count():
            item = tarefas_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

        # Input de tarefa
        input_tarefa = QLineEdit()
        input_tarefa.setPlaceholderText("Digite uma nova tarefa...")
        btn_add = QPushButton("Adicionar")
        btn_add.clicked.connect(lambda: self.adicionar_tarefa(input_tarefa.text()))
        add_layout.addWidget(input_tarefa)
        add_layout.addWidget(btn_add)

        # Mostra tarefas
        for tarefa, completa in self.dados_listas[nome_lista]:
            tarefa_widget = QFrame()
            tarefa_widget.setFixedHeight(70)
            tarefa_widget.setStyleSheet("""
                QFrame {
                    background-color: #f0f0f0;
                    border-radius: 8px;
                    padding: 8px;
                }
            """)
            layout = QHBoxLayout(tarefa_widget)

            checkbox = QCheckBox()
            checkbox.setChecked(completa)
            # Passa o nome da tarefa atual para evitar problema com referência em lambda
            checkbox.stateChanged.connect(lambda _, t=tarefa: self.alternar_status(t))

            label = QLabel(tarefa)
            label.setStyleSheet("font-size: 14px;")
            layout.addWidget(checkbox)
            layout.addWidget(label)
            layout.addStretch()

            tarefas_layout.addWidget(tarefa_widget)

    def adicionar_tarefa(self, texto):
        if not texto or self.lista_atual is None:
            return

        # Verifica se já existe tarefa com o mesmo nome na lista atual
        tarefas_atual = [tarefa for tarefa, _ in self.dados_listas[self.lista_atual]]
        if texto in tarefas_atual:
            QMessageBox.warning(self, "Erro", "Já existe uma tarefa com esse nome nessa lista.")
            return

        if len(self.dados_listas[self.lista_atual]) >= 15:
            QMessageBox.warning(self, "Limite", "Máximo de 15 tarefas por lista.")
            return

        self.dados_listas[self.lista_atual].append((texto, False))
        self.exibir_tarefas(self.lista_atual)
        self.atualizar_contagem()

    def alternar_status(self, tarefa):
        lista = self.dados_listas[self.lista_atual]
        for i, (t, completa) in enumerate(lista):
            if t == tarefa:
                lista[i] = (t, not completa)
                break
        self.exibir_tarefas(self.lista_atual)
        self.atualizar_contagem()

    def contar_tarefas(self):
        total = completas = pendentes = 0
        for tarefas in self.dados_listas.values():
            for _, completa in tarefas:
                total += 1
                if completa:
                    completas += 1
                else:
                    pendentes += 1
        return total, pendentes, completas

    def atualizar_contagem(self):
        total, pendentes, completas = self.contar_tarefas()
        self.ui.lblTask.setText(str(total))
        self.ui.lblTaskPen.setText(str(pendentes))
        self.ui.lblTaskCom.setText(str(completas))
