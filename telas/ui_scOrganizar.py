# Form implementation generated from reading ui file 'ui/scOrganizar.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QtCore.QSize(960, 540))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuLateral = QtWidgets.QFrame(parent=self.frame_2)
        self.menuLateral.setMinimumSize(QtCore.QSize(50, 0))
        self.menuLateral.setMaximumSize(QtCore.QSize(50, 16777215))
        self.menuLateral.setStyleSheet("background-color: rgb(203, 209, 221);")
        self.menuLateral.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.menuLateral.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menuLateral.setObjectName("menuLateral")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menuLateral)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(parent=self.menuLateral)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.btnMenuLargo = QtWidgets.QPushButton(parent=self.frame_5)
        self.btnMenuLargo.setGeometry(QtCore.QRect(0, 0, 200, 65))
        self.btnMenuLargo.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnMenuLargo.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"background:transparent;\n"
"padding:10px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: rgb(214, 214, 214);\n"
"\n"
"}")
        self.btnMenuLargo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/login/user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnMenuLargo.setIcon(icon)
        self.btnMenuLargo.setIconSize(QtCore.QSize(30, 30))
        self.btnMenuLargo.setObjectName("btnMenuLargo")
        self.lblCurso = QtWidgets.QLabel(parent=self.frame_5)
        self.lblCurso.setGeometry(QtCore.QRect(50, 20, 141, 21))
        self.lblCurso.setAutoFillBackground(False)
        self.lblCurso.setStyleSheet("background:transparent;\n"
"font: 8pt \"Helvetica Light\";\n"
"")
        self.lblCurso.setObjectName("lblCurso")
        self.lblNome = QtWidgets.QLabel(parent=self.frame_5)
        self.lblNome.setGeometry(QtCore.QRect(50, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Rounded")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lblNome.setFont(font)
        self.lblNome.setStyleSheet("background: transparent;\n"
"font: 75 10pt \"Helvetica Rounded\";\n"
"color: black;")
        self.lblNome.setObjectName("lblNome")
        self.btnPerfil = QtWidgets.QPushButton(parent=self.frame_5)
        self.btnPerfil.setGeometry(QtCore.QRect(50, 40, 61, 16))
        self.btnPerfil.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnPerfil.setStyleSheet("QPushButton{\n"
"    background:transparent;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    color:white;\n"
"\n"
"}")
        self.btnPerfil.setObjectName("btnPerfil")
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.menuLateral)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.btnTarefas = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnTarefas.setGeometry(QtCore.QRect(0, 20, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnTarefas.setFont(font)
        self.btnTarefas.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnTarefas.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"background:transparent;\n"
"padding:10px;\n"
"text-align:left;\n"
"\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/img/icon/task.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(":/iconActive/img/icon/iconActive/task2.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.btnTarefas.setIcon(icon1)
        self.btnTarefas.setIconSize(QtCore.QSize(30, 30))
        self.btnTarefas.setCheckable(True)
        self.btnTarefas.setObjectName("btnTarefas")
        self.btnMatriz = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnMatriz.setGeometry(QtCore.QRect(0, 120, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnMatriz.setFont(font)
        self.btnMatriz.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnMatriz.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"background:transparent;\n"
"padding:10px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/img/icon/matrix.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon2.addPixmap(QtGui.QPixmap(":/iconActive/img/icon/iconActive/matrix2.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.btnMatriz.setIcon(icon2)
        self.btnMatriz.setIconSize(QtCore.QSize(30, 30))
        self.btnMatriz.setCheckable(True)
        self.btnMatriz.setObjectName("btnMatriz")
        self.btnPomodoro = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnPomodoro.setGeometry(QtCore.QRect(0, 70, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnPomodoro.setFont(font)
        self.btnPomodoro.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnPomodoro.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"background:transparent;\n"
"padding:10px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/img/icon/pomodoro-technique.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon3.addPixmap(QtGui.QPixmap(":/iconActive/img/icon/iconActive/pomodoro2.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.btnPomodoro.setIcon(icon3)
        self.btnPomodoro.setIconSize(QtCore.QSize(30, 30))
        self.btnPomodoro.setCheckable(True)
        self.btnPomodoro.setObjectName("btnPomodoro")
        self.btnCalendario = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnCalendario.setGeometry(QtCore.QRect(0, 170, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnCalendario.setFont(font)
        self.btnCalendario.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnCalendario.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"background:transparent;\n"
"padding:10px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/img/icon/calendar-silhouette.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon4.addPixmap(QtGui.QPixmap(":/iconActive/img/icon/iconActive/calendar-silhouette2.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.btnCalendario.setIcon(icon4)
        self.btnCalendario.setIconSize(QtCore.QSize(30, 30))
        self.btnCalendario.setCheckable(True)
        self.btnCalendario.setObjectName("btnCalendario")
        self.btnDesempenho = QtWidgets.QPushButton(parent=self.frame_6)
        self.btnDesempenho.setGeometry(QtCore.QRect(0, 220, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnDesempenho.setFont(font)
        self.btnDesempenho.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnDesempenho.setStyleSheet("QPushButton{\n"
"\n"
"border:none;\n"
"background:transparent;\n"
"padding:10px;\n"
"text-align:left;\n"
"\n"
"}\n"
"\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/img/icon/line-chart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon5.addPixmap(QtGui.QPixmap(":/iconActive/img/icon/iconActive/line-chart2.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        self.btnDesempenho.setIcon(icon5)
        self.btnDesempenho.setIconSize(QtCore.QSize(30, 30))
        self.btnDesempenho.setCheckable(True)
        self.btnDesempenho.setObjectName("btnDesempenho")
        self.verticalLayout_2.addWidget(self.frame_6)
        self.horizontalLayout_2.addWidget(self.menuLateral)
        self.telas = QtWidgets.QFrame(parent=self.frame_2)
        self.telas.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.telas.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.telas.setObjectName("telas")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.telas)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.paginas = QtWidgets.QStackedWidget(parent=self.telas)
        self.paginas.setObjectName("paginas")
        self.pgTarefas = QtWidgets.QWidget()
        self.pgTarefas.setObjectName("pgTarefas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pgTarefas)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(parent=self.pgTarefas)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.paginas.addWidget(self.pgTarefas)
        self.pgPomodoro = QtWidgets.QWidget()
        self.pgPomodoro.setObjectName("pgPomodoro")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pgPomodoro)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(parent=self.pgPomodoro)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.paginas.addWidget(self.pgPomodoro)
        self.pgMatriz = QtWidgets.QWidget()
        self.pgMatriz.setObjectName("pgMatriz")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.pgMatriz)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.pgMatriz)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.paginas.addWidget(self.pgMatriz)
        self.pgCalendario = QtWidgets.QWidget()
        self.pgCalendario.setObjectName("pgCalendario")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pgCalendario)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.pgCalendario)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.paginas.addWidget(self.pgCalendario)
        self.pgDesempenho = QtWidgets.QWidget()
        self.pgDesempenho.setObjectName("pgDesempenho")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pgDesempenho)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_5 = QtWidgets.QLabel(parent=self.pgDesempenho)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.paginas.addWidget(self.pgDesempenho)
        self.verticalLayout_3.addWidget(self.paginas)
        self.horizontalLayout_2.addWidget(self.telas)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.paginas.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblCurso.setText(_translate("MainWindow", "Curso Teste preencher"))
        self.lblNome.setText(_translate("MainWindow", "Nome do Usuario"))
        self.btnPerfil.setText(_translate("MainWindow", "Exibir Perfil"))
        self.btnTarefas.setText(_translate("MainWindow", "   Tarefas"))
        self.btnMatriz.setText(_translate("MainWindow", "   Matriz de Eisenhower"))
        self.btnPomodoro.setText(_translate("MainWindow", "   Pomodoro"))
        self.btnCalendario.setText(_translate("MainWindow", "   Calendário"))
        self.btnDesempenho.setText(_translate("MainWindow", "   Desempenho"))
        self.label.setText(_translate("MainWindow", "task"))
        self.label_2.setText(_translate("MainWindow", "Pomodoro"))
        self.label_3.setText(_translate("MainWindow", "Matriz de Eisenhower"))
        self.label_4.setText(_translate("MainWindow", "Calendário"))
        self.label_5.setText(_translate("MainWindow", "Desempenho"))
