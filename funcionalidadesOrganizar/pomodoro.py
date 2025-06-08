from PyQt6.QtCore import QTimer, Qt

class Pomodoro:
    def __init__(self, ui):
        self.ui = ui
        self.total_seconds = 25 * 60

        self.ui.lblTimer.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        #self.ui.lblTimer.setText("25:00")

        self.timer = QTimer()
        self.timer.timeout.connect(self.atualizar_timer)

        self.ui.btnStart.clicked.connect(self.iniciar_timer)

    def iniciar_timer(self):
        self.total_seconds = 25 * 60
        self.timer.start(1000)

    def atualizar_timer(self):
        if self.total_seconds > 0:
            self.total_seconds -= 1
            minutos = self.total_seconds // 60
            segundos = self.total_seconds % 60
            self.ui.lblTimer.setText(f"{minutos:02d}:{segundos:02d}")
        else:
            self.timer.stop()
            self.ui.lblTimer.setText("00:00")
