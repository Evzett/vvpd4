# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scoring_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from practice4 import deadline_score

class DeadlineScoresWindow(QWidget):
    """Класс окна, всплывающего при выборе "Определить оценку"
    на стартовом окне
    """
    def setupUi(self, deadline_scores_window):
        deadline_scores_window.setObjectName("deadline_scores_window")
        deadline_scores_window.resize(442, 365)
        deadline_scores_window.setStyleSheet("background-color: rgb(216, 229, 255);\n"
"font: 10pt \"Century Gothic\";\n"
"")
        self.widget = QtWidgets.QWidget(deadline_scores_window)
        self.widget.setGeometry(QtCore.QRect(0, 0, 441, 351))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pass_date_label = QtWidgets.QLabel(self.widget)
        self.pass_date_label.setObjectName("pass_date_label")
        self.verticalLayout.addWidget(self.pass_date_label)
        self.pass_date_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.pass_date_lineEdit.setStyleSheet("background-color: rgb(237, 242, 255);")
        self.pass_date_lineEdit.setObjectName("pass_date_lineEdit")
        self.verticalLayout.addWidget(self.pass_date_lineEdit)
        self.deadline_date_label = QtWidgets.QLabel(self.widget)
        self.deadline_date_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.deadline_date_label.setObjectName("deadline_date_label")
        self.verticalLayout.addWidget(self.deadline_date_label)
        self.deadline_date_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.deadline_date_lineEdit.setStyleSheet("background-color: rgb(237, 242, 255);")
        self.deadline_date_lineEdit.setObjectName("deadline_date_lineEdit")
        self.verticalLayout.addWidget(self.deadline_date_lineEdit)
        self.show_mark_Button = QtWidgets.QPushButton(self.widget)
        self.show_mark_Button.setStyleSheet("QPushButton:hover {\n"
"    background-color:rgb(170, 183, 255); \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255); \n"
"}")
        self.show_mark_Button.setObjectName("show_mark_Button")
        self.verticalLayout.addWidget(self.show_mark_Button)
        self.show_result_label = QtWidgets.QLabel(self.widget)
        self.show_result_label.setStyleSheet("background-color: rgb(237, 242, 255);\n"
"")
        self.show_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.show_result_label.setObjectName("show_result_label")
        self.verticalLayout.addWidget(self.show_result_label)
        self.show_mark_Button.clicked.connect(self.show_mark)
        self.retranslateUi(deadline_scores_window)
        QtCore.QMetaObject.connectSlotsByName(deadline_scores_window)
    def show_mark(self):
        """Метод, вызывающий функцию из модуля practice4,
        которая определяет оценку в зависимости от даты
        сдачи и дедлайна"""
        self.current_pass_date=self.pass_date_lineEdit.text()
        self.current_deadline_date=self.deadline_date_lineEdit.text()
        result=deadline_score(self.current_pass_date,self.current_deadline_date)
        self.show_result_label.setText(str(result))

    def retranslateUi(self, deadline_scores_window):
        _translate = QtCore.QCoreApplication.translate
        deadline_scores_window.setWindowTitle(_translate("deadline_scores_window", "Form"))
        self.pass_date_label.setText(_translate("deadline_scores_window", "   Дата сдачи работы:"))
        self.deadline_date_label.setText(_translate("deadline_scores_window", "   Дата дедлайна:"))
        self.show_mark_Button.setText(_translate("deadline_scores_window", "Показать оценку"))
        self.show_result_label.setText(_translate("deadline_scores_window", "Здесь будет показан результат"))
