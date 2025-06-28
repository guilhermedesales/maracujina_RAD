from PyQt6.QtCore import QTimer, Qt

class Pomodoro:
    def __init__(self, ui):
        self.ui = ui
        self.em_pausa = False
        self.em_foco = True  # Começa com foco
        self.total_seconds = 25 * 60

        self.ui.lblTimer.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.ui.lblTimer.setText("25:00")

        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_timer)

        self.ui.btnStart.clicked.connect(self.toggle_timer)

    def toggle_timer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.ui.btnStart.setText("Iniciar")
        else:
            self.timer.start(1000)
            self.ui.btnStart.setText("Pausar")

    def atualizar_timer(self):
        if self.total_seconds > 0:
            self.total_seconds -= 1
            minutos = self.total_seconds // 60
            segundos = self.total_seconds % 60
            self.ui.lblTimer.setText(f"{minutos:02d}:{segundos:02d}")
        else:
            self.timer.stop()
            self.alternar_periodo()
            self.timer.start(1000)  # Reinicia automaticamente

    def alternar_periodo(self):
        if self.em_foco:
            self.total_seconds = 5 * 60
            self.em_foco = False
        else:
            self.total_seconds = 25 * 60
            self.em_foco = True

        minutos = self.total_seconds // 60
        segundos = self.total_seconds % 60
        self.ui.lblTimer.setText(f"{minutos:02d}:{segundos:02d}")
