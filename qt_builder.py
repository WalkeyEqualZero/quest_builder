import sys
from PyQt5 import uic, QtCore, QtGui
import subprocess
import os
import PyInstaller.__main__
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItem, QFileDialog, QInputDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 725)
        MainWindow.setMinimumSize(QtCore.QSize(994, 725))
        MainWindow.setMaximumSize(QtCore.QSize(994, 725))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.questions = QtWidgets.QTreeWidget(self.centralwidget)
        self.questions.setEnabled(True)
        self.questions.setGeometry(QtCore.QRect(10, 20, 631, 661))
        self.questions.setStyleSheet("font: 12pt \"Courier New\";")
        self.questions.setObjectName("questions")
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(670, 190, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(15)
        self.add_btn.setFont(font)
        self.add_btn.setObjectName("add_btn")
        self.change_name_btn = QtWidgets.QPushButton(self.centralwidget)
        self.change_name_btn.setGeometry(QtCore.QRect(670, 120, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(15)
        self.change_name_btn.setFont(font)
        self.change_name_btn.setObjectName("change_name_btn")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(750, 80, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.name_edit.setFont(font)
        self.name_edit.setText("")
        self.name_edit.setObjectName("name_edit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(670, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.main_label = QtWidgets.QLabel(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(780, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        self.main_label.setFont(font)
        self.main_label.setText("")
        self.main_label.setObjectName("main_label")
        self.label_ico1 = QtWidgets.QLabel(self.centralwidget)
        self.label_ico1.setGeometry(QtCore.QRect(1500, 30, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        self.label_ico1.setFont(font)
        self.label_ico1.setText("")
        self.label_ico1.setPixmap(QtGui.QPixmap("resources/qu_ico.png"))
        self.label_ico1.setScaledContents(True)
        self.label_ico1.setObjectName("label_ico1")
        self.label_ico2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ico2.setGeometry(QtCore.QRect(1500, 30, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        self.label_ico2.setFont(font)
        self.label_ico2.setText("")
        self.label_ico2.setPixmap(QtGui.QPixmap("resources/qu_ico.png"))
        self.label_ico2.setScaledContents(True)
        self.label_ico2.setObjectName("label_ico2")
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn.setGeometry(QtCore.QRect(670, 260, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(15)
        self.delete_btn.setFont(font)
        self.delete_btn.setObjectName("delete_btn")
        self.done = QtWidgets.QLabel(self.centralwidget)
        self.done.setGeometry(QtCore.QRect(790, 640, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(15)
        self.done.setFont(font)
        self.done.setText("")
        self.done.setObjectName("done")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 21))
        self.menubar.setObjectName("menubar")
        self.upper_menu = QtWidgets.QMenu(self.menubar)
        self.upper_menu.setObjectName("upper_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_btn = QtWidgets.QAction(MainWindow)
        self.open_btn.setObjectName("open_btn")
        self.save_btn = QtWidgets.QAction(MainWindow)
        self.save_btn.setObjectName("save_btn")
        self.make_btn = QtWidgets.QAction(MainWindow)
        self.make_btn.setObjectName("make_btn")
        self.upper_menu.addAction(self.open_btn)
        self.upper_menu.addAction(self.save_btn)
        self.upper_menu.addSeparator()
        self.upper_menu.addAction(self.make_btn)
        self.menubar.addAction(self.upper_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.questions.headerItem().setText(0, _translate("MainWindow", "Вопросы"))
        self.questions.headerItem().setText(1, _translate("MainWindow", "New Column"))
        self.questions.headerItem().setText(2, _translate("MainWindow", "New Column"))
        self.add_btn.setText(_translate("MainWindow", "➕ Добавить ветку"))
        self.change_name_btn.setText(_translate("MainWindow", "Сохранить"))
        self.label.setText(_translate("MainWindow", "Текст:"))
        self.delete_btn.setText(_translate("MainWindow", "⛔ Удалить ветку"))
        self.upper_menu.setTitle(_translate("MainWindow", "Проект"))
        self.open_btn.setText(_translate("MainWindow", "Открыть проект"))
        self.save_btn.setText(_translate("MainWindow", "Сохранить проект"))
        self.make_btn.setText(_translate("MainWindow", "Собрать приложение"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Сборщик приложений')
        self.questions.itemSelectionChanged.connect(self.open_ui)
        self.project = {"001": {'text': 'Стартовый вопрос', 'answers': {}, 'image': ''}}
        self.add_btn.clicked.connect(self.new_question)
        self.change_name_btn.clicked.connect(self.change_name)
        self.questions.addTopLevelItem(QTreeWidgetItem(['Стартовый вопрос', '001']))
        self.icon_quest = QtGui.QIcon('./resources/qu_ico.png')
        self.delete_btn.clicked.connect(self.delete_branch)
        self.questions.topLevelItem(0).setIcon(0, self.icon_quest)
        self.open_btn.triggered.connect(self.open_project)
        self.save_btn.triggered.connect(self.save_project)
        self.make_btn.triggered.connect(self.dlg_make)
        self.questions.setColumnHidden(1, True)
        self.questions.setColumnHidden(2, True)
        self.project_name = ''
        self.first = False
        # self.questions.setCurrentItem(QtCore.Qt.No)
        # self.questions.topLevelItem(0).setSelected(True)

    def dlg_make(self):
        self.done.setText('')
        dlg = QInputDialog(self)
        dlg.setInputMode(QInputDialog.TextInput)
        dlg.setLabelText("Имя файла")
        dlg.setTextValue(self.project_name)
        dlg.setWindowTitle('Сохранение проекта')
        dlg.setCancelButtonText('Отмена')
        dlg.resize(300, 200)
        ok = dlg.exec_()
        name = dlg.textValue()
        if ok:
            self.make_project(name)

    def make_project(self, text):
        with open('qt_main.py', 'r', encoding='utf-8') as f:
            lines = f.read().split('\n')
            new_line = f'slov = {self.project}'
            new_file = '\n'.join(lines[:6] + [new_line] + lines[7:])
        f.close()

        with open('qt_main1.py', 'w', encoding='utf-8') as f:
            f.write(new_file)
        f.close()

        subprocess.call(fr'pyinstaller --noconfirm --windowed --onefile --icon "{os.path.abspath("cok.ico")}" --name "{text}" {os.path.abspath("qt_main1.py")}')

        # PyInstaller.__main__.run([
        #     'qt_main1.py',
        #     '--noconfirm', '--onefile', '--windowed',
        #     '--icon', 'cok.ico',
        #     '--name', text
        # ])
        self.done.setText('Done!')

    def delete_branch(self):
        if self.first:
            if self.questions.currentItem() != self.questions.topLevelItem(0) and not self.questions.currentItem().isSelected():
                self.project[self.questions.currentItem().text(1)]['answers'].pop(self.questions.currentItem().text(0))
                list_del = {self.questions.currentItem().text(2)}
                length = 0
                while len(list_del) != length:
                    length = len(list_del)
                    for ids in list_del:
                        list_del = list_del | set(self.project[ids]['answers'].values())
                for del_ids in list_del:
                    self.project.pop(del_ids)
                parent = self.questions.currentItem()
                for i in range(parent.childCount()):
                    parent.removeChild(parent.child(i))
                self.questions.currentItem().parent().removeChild(parent)

    def save_project(self):
        dlg = QInputDialog(self)
        dlg.setInputMode(QInputDialog.TextInput)
        dlg.setLabelText("Имя проекта")
        dlg.setTextValue(self.project_name)
        dlg.setWindowTitle('Сохранение проекта')
        dlg.setCancelButtonText('Отмена')
        dlg.resize(300, 200)
        ok = dlg.exec_()
        name = dlg.textValue()
        if ok:
            fu = open(f"projects/{name}.txt", 'w', encoding="utf‐8")
            fu.write(str(self.project))
            self.project_name = name
            fu.close()

    def open_project(self):
        f_name = QFileDialog.getOpenFileName(
            self, 'Выбрать проект', '',
            'Проект (*.txt);;Все файлы (*)')[0]
        if f_name != '':
            pr_name = f_name.split('/')
            self.project_name = pr_name[-1][:-4]
            self.questions.clear()
            self.first = False
            f = open(f_name, mode="r", encoding="utf‐8")
            d = eval(f.read())
            f.close()
            self.project = d.copy()
            self.questions.addTopLevelItem(QTreeWidgetItem([d['001']['text'], '001']))
            self.questions.topLevelItem(0).setIcon(0, self.icon_quest)
            for qu_id, val in d.items():
                if qu_id != '001':
                    item = QTreeWidgetItem([val['text'], qu_id])
                    item.setIcon(0, self.icon_quest)
                    self.questions.findItems(qu_id, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive, column=2)[0].addChild(item)
                for text_ans, ans_id in val['answers'].items():
                    item_ans = QTreeWidgetItem([text_ans, qu_id, ans_id])
                    item_ans.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.questions.findItems(qu_id, QtCore.Qt.MatchContains | QtCore.Qt.MatchRecursive, column=1)[0].addChild(item_ans)

    def open_ui(self):
        self.first = True
        if self.questions.currentItem().isSelected():
            self.main_label.setText('Вопрос')
            self.label_ico1.setGeometry(750, 30, 21, 21)
            self.label_ico2.setGeometry(870, 30, 21, 21)
            self.add_btn.setGeometry(670, 190, 301, 51)
            self.delete_btn.setGeometry(1500, 260, 301, 51)
            self.name_edit.setText(self.questions.currentItem().text(0))
        else:
            self.label_ico1.setGeometry(1500, 30, 21, 21)
            self.label_ico2.setGeometry(1500, 30, 21, 21)
            self.add_btn.setGeometry(1500, 190, 301, 51)
            self.delete_btn.setGeometry(670, 190, 301, 51)
            self.main_label.setText('Ответ')
            self.name_edit.setText(self.questions.currentItem().text(0))

    def new_question(self):
        if self.questions.currentItem().isSelected():
            self.first = True
            if self.questions.currentItem().childCount() < 5:

                listop = str(int(list(self.project.keys())[-1]) + 1)
                listop = (3 - len(listop)) * '0' + listop
                self.project[listop] = {'text': 'новый вопрос', 'answers': {}, 'image': ''}
                for nums in range(1, 6):
                    name = 'новый ответ' + str(nums)
                    if name not in self.project[self.questions.currentItem().text(1)]['answers']:
                        self.questions.currentItem().addChild(QTreeWidgetItem([name, self.questions.currentItem().text(1), listop]))
                        self.project[self.questions.currentItem().text(1)]['answers'][name] = listop
                        self.questions.currentItem().child(self.questions.currentItem().childCount() - 1).setFlags(
                            QtCore.Qt.ItemIsEnabled)
                        break
                self.questions.currentItem().child(self.questions.currentItem().childCount() - 1).addChild(QTreeWidgetItem(['новый вопрос', listop]))
                self.questions.currentItem().child(self.questions.currentItem().childCount() - 1).child(
                    self.questions.currentItem().child(
                        self.questions.currentItem().childCount() - 1).childCount() - 1).setIcon(0, self.icon_quest)

    def change_name(self):
        if self.first:
            if self.questions.currentItem().isSelected():
                self.questions.currentItem().setText(0, self.name_edit.text())
                self.project[self.questions.currentItem().text(1)]['text'] = self.name_edit.text()
            elif self.questions.currentItem():
                for val in self.project[self.questions.currentItem().text(1)]['answers'].keys():
                    if val == self.questions.currentItem().text(0):
                        self.project[self.questions.currentItem().text(1)]['answers'][self.name_edit.text()] = self.project[self.questions.currentItem().text(1)]['answers'].pop(val)
                        break
                # self.project =
                self.questions.currentItem().setText(0, self.name_edit.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
