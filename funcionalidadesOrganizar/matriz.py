from PyQt6.QtWidgets import QInputDialog, QMessageBox
import pymysql


def conectar_banco():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='db_maracujina',
        connect_timeout=5
    )


def buscar_tarefas_disponiveis(id_usuario):
    try:
        conexao = conectar_banco()
        with conexao.cursor() as cursor:
            cursor.execute("""
                SELECT id_tarefa, nome_tarefa
                FROM tarefas
                WHERE id_usuario = %s AND matriz IS NULL
            """, (id_usuario,))
            return cursor.fetchall()
    except Exception as e:
        print(f"[ERRO] ao buscar tarefas: {e}")
        return []
    finally:
        conexao.close()


def atualizar_matriz(id_tarefa, categoria_matriz):
    try:
        conexao = conectar_banco()
        with conexao.cursor() as cursor:
            cursor.execute("""
                UPDATE tarefas
                SET matriz = %s
                WHERE id_tarefa = %s
            """, (categoria_matriz, id_tarefa))
            conexao.commit()
    except Exception as e:
        print(f"[ERRO] ao atualizar tarefa: {e}")
    finally:
        conexao.close()


def adicionar_tarefa_a_matriz(parent, id_usuario, categoria_matriz):
    """
    parent: QWidget (a janela que chama)
    id_usuario: int
    categoria_matriz: str -> "UI", "UN", "NI" ou "NN"
    """
    tarefas = buscar_tarefas_disponiveis(id_usuario)
    if not tarefas:
        QMessageBox.information(parent, "Sem tarefas", "Não há tarefas disponíveis para adicionar.")
        return None

    nomes = [t[1] for t in tarefas]
    escolha, ok = QInputDialog.getItem(
        parent,
        "Escolher tarefa",
        "Qual tarefa deseja adicionar?",
        nomes,
        0,
        False
    )

    if ok and escolha:
        confirmacao = QMessageBox.question(
            parent,
            "Confirmar",
            f"Deseja adicionar a tarefa '{escolha}' ao quadrante {categoria_matriz}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmacao == QMessageBox.StandardButton.Yes:
            id_tarefa = next(t[0] for t in tarefas if t[1] == escolha)
            atualizar_matriz(id_tarefa, categoria_matriz)
            return escolha

    return None
