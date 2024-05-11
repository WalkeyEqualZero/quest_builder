import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 580)
        MainWindow.setMinimumSize(QtCore.QSize(800, 580))
        MainWindow.setMaximumSize(QtCore.QSize(800, 580))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.first_btn = QtWidgets.QPushButton(self.centralwidget)
        self.first_btn.setGeometry(QtCore.QRect(60, 300, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.first_btn.setFont(font)
        self.first_btn.setCheckable(False)
        self.first_btn.setAutoRepeat(False)
        self.first_btn.setAutoExclusive(False)
        self.first_btn.setObjectName("first_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 50, 531, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.second_btn = QtWidgets.QPushButton(self.centralwidget)
        self.second_btn.setGeometry(QtCore.QRect(50, 350, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.second_btn.setFont(font)
        self.second_btn.setAcceptDrops(False)
        self.second_btn.setAutoDefault(False)
        self.second_btn.setDefault(False)
        self.second_btn.setFlat(False)
        self.second_btn.setObjectName("second_btn")
        self.res = QtWidgets.QPushButton(self.centralwidget)
        self.res.setGeometry(QtCore.QRect(330, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.res.setFont(font)
        self.res.setObjectName("res")
        self.bef = QtWidgets.QPushButton(self.centralwidget)
        self.bef.setGeometry(QtCore.QRect(350, 440, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.bef.setFont(font)
        self.bef.setObjectName("bef")
        self.third_btn = QtWidgets.QPushButton(self.centralwidget)
        self.third_btn.setGeometry(QtCore.QRect(30, 380, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.third_btn.setFont(font)
        self.third_btn.setObjectName("third_btn")
        self.fourth_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fourth_btn.setGeometry(QtCore.QRect(360, 320, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fourth_btn.setFont(font)
        self.fourth_btn.setObjectName("fourth_btn")
        self.fifth_btn = QtWidgets.QPushButton(self.centralwidget)
        self.fifth_btn.setGeometry(QtCore.QRect(530, 390, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.fifth_btn.setFont(font)
        self.fifth_btn.setObjectName("fifth_btn")
        self.deadpool = QtWidgets.QLabel(self.centralwidget)
        self.deadpool.setGeometry(QtCore.QRect(30, 50, 331, 241))
        self.deadpool.setText("")
        # self.deadpool.setPixmap(QtGui.QPixmap(resource_path("deadpool.png")))
        self.deadpool.setObjectName("deadpool")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.first_btn.setText(_translate("MainWindow", "Да"))
        self.second_btn.setText(_translate("MainWindow", "Нет"))
        self.res.setText(_translate("MainWindow", "Перезапуск"))
        self.bef.setText(_translate("MainWindow", "Назад"))
        self.third_btn.setText(_translate("MainWindow", "e"))
        self.fourth_btn.setText(_translate("MainWindow", "ё"))
        self.fifth_btn.setText(_translate("MainWindow", "у"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self, slovar):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Помощник')
        self.questions = slovar
        self.start = '001'
        self.now = self.start
        self.was = []
        self.change()
        self.first_btn.clicked.connect(self.first_pressed)
        self.second_btn.clicked.connect(self.second_pressed)
        self.third_btn.clicked.connect(self.third_pressed)
        self.fourth_btn.clicked.connect(self.fourth_pressed)
        self.fifth_btn.clicked.connect(self.fifth_pressed)
        self.res.clicked.connect(self.restart)
        self.bef.clicked.connect(self.before)

    def first_pressed(self):
        print(self.questions[self.now]['answers'][self.first_btn.text()])
        self.was.append(self.now)
        self.now = self.questions[self.now]['answers'][self.first_btn.text()]
        self.change()

    def second_pressed(self):
        print(self.questions[self.now]['answers'][self.second_btn.text()])
        self.was.append(self.now)
        self.now = self.questions[self.now]['answers'][self.second_btn.text()]
        self.change()

    def third_pressed(self):
        print(self.questions[self.now]['answers'][self.third_btn.text()])
        self.was.append(self.now)
        self.now = self.questions[self.now]['answers'][self.third_btn.text()]
        self.change()

    def fourth_pressed(self):
        print(self.questions[self.now]['answers'][self.fourth_btn.text()])
        self.was.append(self.now)
        self.now = self.questions[self.now]['answers'][self.fourth_btn.text()]
        self.change()

    def fifth_pressed(self):
        print(self.questions[self.now]['answers'][self.fifth_btn.text()])
        self.was.append(self.now)
        self.now = self.questions[self.now]['answers'][self.fifth_btn.text()]
        self.change()

    def change(self):
        list_answers = list(self.questions[self.now]['answers'].keys())
        if len(list_answers) == 0:
            self.first_btn.setGeometry(1000, 300, 131, 41)
            self.second_btn.setGeometry(1000, 300, 131, 41)
            self.third_btn.setGeometry(1000, 300, 131, 41)
            self.fourth_btn.setGeometry(1000, 300, 131, 41)
            self.fifth_btn.setGeometry(1000, 300, 131, 41)
            self.deadpool.setGeometry(30, 50, 331, 241)
            self.label.setStyleSheet("background-color: rgb(91, 195, 68);")
        else:
            self.deadpool.setGeometry(2000, 50, 331, 241)
            self.label.setStyleSheet('')
            if len(list_answers) == 1:
                self.first_btn.setText(list_answers[0])
                self.first_btn.setGeometry(230, 300, 131, 41)
                self.second_btn.setGeometry(1000, 300, 131, 41)
                self.third_btn.setGeometry(1000, 300, 131, 41)
                self.fourth_btn.setGeometry(1000, 300, 131, 41)
                self.fifth_btn.setGeometry(1000, 300, 131, 41)
            elif len(list_answers) == 2:
                self.first_btn.setText(list_answers[0])
                self.second_btn.setText(list_answers[1])
                self.first_btn.setGeometry(230, 300, 131, 41)
                self.second_btn.setGeometry(430, 300, 131, 41)
                self.third_btn.setGeometry(1000, 300, 131, 41)
                self.fourth_btn.setGeometry(1000, 300, 131, 41)
                self.fifth_btn.setGeometry(1000, 300, 131, 41)
            elif len(list_answers) == 3:
                self.first_btn.setText(list_answers[0])
                self.second_btn.setText(list_answers[1])
                self.third_btn.setText(list_answers[2])
                self.first_btn.setGeometry(120, 300, 131, 41)
                self.second_btn.setGeometry(330, 300, 131, 41)
                self.third_btn.setGeometry(540, 300, 131, 41)
                self.fourth_btn.setGeometry(1000, 300, 131, 41)
                self.fifth_btn.setGeometry(1000, 300, 131, 41)
            elif len(list_answers) == 4:
                self.first_btn.setText(list_answers[0])
                self.second_btn.setText(list_answers[1])
                self.third_btn.setText(list_answers[2])
                self.fourth_btn.setText(list_answers[3])
                self.first_btn.setGeometry(60, 300, 131, 41)
                self.second_btn.setGeometry(240, 300, 131, 41)
                self.third_btn.setGeometry(420, 300, 131, 41)
                self.fourth_btn.setGeometry(600, 300, 131, 41)
                self.fifth_btn.setGeometry(1000, 300, 131, 41)
            elif len(list_answers) == 5:
                self.first_btn.setText(list_answers[0])
                self.second_btn.setText(list_answers[1])
                self.third_btn.setText(list_answers[2])
                self.fourth_btn.setText(list_answers[3])
                self.fifth_btn.setText(list_answers[4])
                self.first_btn.setGeometry(30, 300, 131, 41)
                self.second_btn.setGeometry(180, 300, 131, 41)
                self.third_btn.setGeometry(330, 300, 131, 41)
                self.fourth_btn.setGeometry(480, 300, 131, 41)
                self.fifth_btn.setGeometry(630, 300, 131, 41)
        self.label.setText(self.questions[self.now]['text'])
        # if self.questions[self.now]['type'] == 'end':
        #     self.deadpool.setGeometry(30, 50, 331, 241)
        #     self.label.setStyleSheet("background-color: rgba(207, 13, 13, 200);")
        # else:
        #     self.deadpool.setGeometry(2000, 50, 331, 241)
        #     self.label.setStyleSheet('')

    def before(self):
        if self.was:
            self.now = self.was.pop(-1)
            self.change()
            print(self.was)

    def restart(self):
        self.was = [self.start]
        self.now = self.start
        self.change()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget(slov)
    ex.show()
    sys.exit(app.exec_())
