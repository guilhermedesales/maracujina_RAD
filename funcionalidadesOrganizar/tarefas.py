from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QInputDialog
from PyQt6.QtCore import Qt

class TarefasWidget(QWidget):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui  # Ui_MainWindow vindo de fora
        self.dados_listas = {}

        self.ui.btnCriarLista.clicked.connect(self.criar_lista_tarefas)

    def criar_lista_tarefas(self):
        nome_lista, ok = QInputDialog.getText(self, "Nova Lista", "Nome da lista:")
        if ok and nome_lista:
            self.adicionar_lista(nome_lista)

    def adicionar_lista(self, nome_lista):
        botao = QPushButton(nome_lista)
        botao.setCheckable(True)
        botao.setStyleSheet("text-align: left; padding: 5px;")
        botao.clicked.connect(lambda: self.exibir_tarefas_da_lista(nome_lista))

        self.ui.layoutListasTarefas.layout().addWidget(botao)
        self.dados_listas[nome_lista] = []

    def exibir_tarefas_da_lista(self, nome_lista):

        container = self.ui.containerTarefas
        layout_anterior = container.layout()

        if layout_anterior is not None:
            while layout_anterior.count():
                item = layout_anterior.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)

        novo_layout = QVBoxLayout()
        novo_layout.setSpacing(10)
        novo_layout.setContentsMargins(10, 10, 10, 10)

        for tarefa in self.dados_listas[nome_lista]:
            card = QLabel(tarefa)
            card.setStyleSheet("background: white; border: 1px solid #ccc; padding: 10px;")
            novo_layout.addWidget(card)

        container.setLayout(novo_layout)
        self.layoutCardsTarefas = novo_layout