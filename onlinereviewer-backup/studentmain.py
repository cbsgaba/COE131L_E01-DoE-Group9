# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentmain.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import login
import StudentTestAnswer
import studentquestionbank
import sys
import sqlite3


class Ui_student_main(object):
    def setupUi(self, student_main):
        student_main.setObjectName("student_main")
        student_main.resize(482, 142)
        self.centralwidget = QtWidgets.QWidget(student_main)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 61, 16))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(290, 20, 160, 112))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Answer_Question_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Answer_Question_button.setObjectName("Answer_Question_button")
        self.verticalLayout.addWidget(self.Answer_Question_button)
        self.question_bank_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.question_bank_button.setObjectName("question_bank_button")
        self.verticalLayout.addWidget(self.question_bank_button)
        self.logout_student_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.logout_student_button.setObjectName("logout_student_button")
        self.verticalLayout.addWidget(self.logout_student_button)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 251, 81))
        self.groupBox.setObjectName("groupBox")
        self.user_label = QtWidgets.QLabel(self.groupBox)
        self.user_label.setGeometry(QtCore.QRect(10, 30, 55, 16))
        self.user_label.setObjectName("user_label")
        self.username_label = QtWidgets.QLabel(self.groupBox)
        self.username_label.setGeometry(QtCore.QRect(80, 30, 151, 16))
        self.username_label.setObjectName("username_label")
        self.name_label = QtWidgets.QLabel(self.groupBox)
        self.name_label.setGeometry(QtCore.QRect(10, 50, 55, 16))
        self.name_label.setObjectName("name_label")
        self.nameuser_label = QtWidgets.QLabel(self.groupBox)
        self.nameuser_label.setGeometry(QtCore.QRect(80, 50, 161, 16))
        self.nameuser_label.setObjectName("nameuser_label")
        student_main.setCentralWidget(self.centralwidget)
        self.actionLogout = QtWidgets.QAction(student_main)
        self.actionLogout.setObjectName("actionLogout")
        self.actionExit = QtWidgets.QAction(student_main)
        self.actionExit.setObjectName("actionExit")
        
        self.score_label = QtWidgets.QLabel(self.groupBox)
        self.score_label.setGeometry(QtCore.QRect(170, 10, 55, 16))
        self.score_label.setObjectName("score_label")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(170, 30, 41, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(student_main)
        QtCore.QMetaObject.connectSlotsByName(student_main)
        ################################################################
        self.logout_student_button.clicked.connect(self.loginpageShow)
        self.logout_student_button.clicked.connect(student_main.close)
        ################################################################
        self.Answer_Question_button.clicked.connect(self.StudentTestAnswerShow)
        self.Answer_Question_button.clicked.connect(student_main.close)
        ################################################################
        self.question_bank_button.clicked.connect(self.studentquestionbankShow)
        self.question_bank_button.clicked.connect(student_main.close)
        ###############################################################
        name='null'
        username1='null'
        usertype='null'
        password1='null'
        #try:
        con = sqlite3.connect("userlist.db",timeout=10)
        cur = con.cursor()
        cur.execute('SELECT * FROM users WHERE ID=5')
        data = cur.fetchall()
        con.commit()
        for row in data:
            usertype = row[1]
            name = row[2]
            username1 = row[3]
            password1 = row[4]
            modify1 = row[5]
        print(modify1)
        cur.execute('SELECT * FROM users WHERE ID =?', (modify1,))
        data2 = cur.fetchall()
        con.commit()
        for row in data2:
            idq = row[0]
            score = row[6]
        print(idq)
        print(score)
        scorr= str(score)
        if scorr=='None':
            self.label_3.setText('')
        else:
            self.label_3.setText(scorr)
        con.close
    
        self.username_label.setText(username1)
        self.nameuser_label.setText(name)
            
        #except Exception:
         #   self.showMessageBox('Database Error','Could not access the database')

        ################################################################

    def loginpageShow(self):
        self.loginpageWindow = QtWidgets.QMainWindow()
        self.ui = login.Ui_LOGINPAGE()
        self.ui.setupUi(self.loginpageWindow)
        self.loginpageWindow.show()  

    def StudentTestAnswerShow(self):
        self.StudentTestAnswerWindow = QtWidgets.QMainWindow()
        self.ui = StudentTestAnswer.Ui_ReviewerTest()
        self.ui.setupUi(self.StudentTestAnswerWindow)
        self.StudentTestAnswerWindow.show()
    
    def studentquestionbankShow(self):
        self.studentquestionbankWindow = QtWidgets.QMainWindow()
        self.ui = studentquestionbank.Ui_Question_bank()
        self.ui.setupUi(self.studentquestionbankWindow)
        self.studentquestionbankWindow.show()
        
        ################################################################
    def retranslateUi(self, student_main):
        _translate = QtCore.QCoreApplication.translate
        student_main.setWindowTitle(_translate("student_main", "Online Reviewer"))
        self.label.setText(_translate("student_main", "WELCOME"))
        self.Answer_Question_button.setText(_translate("student_main", "ANSWER QUESTION TEST"))
        self.question_bank_button.setText(_translate("student_main", "VIEW QUESTION BANK"))
        self.logout_student_button.setText(_translate("student_main", "LOGOUT"))
        self.groupBox.setTitle(_translate("student_main", "Online Reviewer"))
        self.user_label.setText(_translate("student_main", "USER: "))
        self.username_label.setText(_translate("student_main", "USER1"))
        self.name_label.setText(_translate("student_main", "NAME:"))
        self.nameuser_label.setText(_translate("student_main", "NAME"))
        self.actionLogout.setText(_translate("student_main", "Logout"))
        self.actionExit.setText(_translate("student_main", "Exit"))
        self.score_label.setText(_translate("student_main", "SCORE:"))
        #self.label_3.setText(_translate("student_main", "100"))

    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    student_main = QtWidgets.QMainWindow()
    ui = Ui_student_main()
    ui.setupUi(student_main)
    student_main.show()
    sys.exit(app.exec_())
