import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from tela_login import LoginWindow
import res_rc # importa os icons/imagens da tela ui
from criarBD import ensure_database

if __name__ == "__main__":

    try:
        ensure_database()
    except Exception as exc:
        #QMessageBox.critical(
            #None,
            #"Erro no banco",
            #f"Não foi possível criar/acessar o banco:\n{exc}",
        #)
        print(f"Erro ao criar/acessar banco: {exc}")
        sys.exit(1)


    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
