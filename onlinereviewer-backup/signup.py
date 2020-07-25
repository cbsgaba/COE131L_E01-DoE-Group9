# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import login
import sqlite3
import sys



class Ui_SIGNUPPAGE(object):
    def setupUi(self, SIGNUPPAGE):
        SIGNUPPAGE.setObjectName("SIGNUPPAGE")
        SIGNUPPAGE.resize(327, 313)
        SIGNUPPAGE.setMinimumSize(QtCore.QSize(327, 313))
        SIGNUPPAGE.setMaximumSize(QtCore.QSize(327, 451))
        self.centralwidget = QtWidgets.QWidget(SIGNUPPAGE)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(30, 140, 71, 20))
        self.username_label.setObjectName("username_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(30, 190, 71, 16))
        self.password_label.setObjectName("password_label")
        self.signup_button = QtWidgets.QPushButton(self.centralwidget)
        self.signup_button.setGeometry(QtCore.QRect(50, 250, 93, 28))
        self.signup_button.setObjectName("signup_button")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(160, 250, 93, 28))
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 120, 191, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.userline = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.userline.setObjectName("userline")
        self.verticalLayout_2.addWidget(self.userline)
        self.passline = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.passline.setObjectName("passline")
        #################################################
        self.passline.setEchoMode(QtWidgets.QLineEdit.Password)
        ##############################################
        self.verticalLayout_2.addWidget(self.passline)
        self.registration_label = QtWidgets.QLabel(self.centralwidget)
        self.registration_label.setGeometry(QtCore.QRect(110, 20, 91, 20))
        self.registration_label.setObjectName("registration_label")
        self.firstname_label = QtWidgets.QLabel(self.centralwidget)
        self.firstname_label.setGeometry(QtCore.QRect(140, 100, 81, 20))
        self.firstname_label.setObjectName("firstname_label")
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setGeometry(QtCore.QRect(70, 60, 189, 22))
        self.name_line.setObjectName("name_line")
        SIGNUPPAGE.setCentralWidget(self.centralwidget)

        self.retranslateUi(SIGNUPPAGE)
        QtCore.QMetaObject.connectSlotsByName(SIGNUPPAGE)
        ######################################
        self.cancel_button.clicked.connect(SIGNUPPAGE.close)
        self.cancel_button.clicked.connect(self.loginpageShow)
        self.signup_button.clicked.connect(self.register)
        self.signup_button.clicked.connect(SIGNUPPAGE.close)
        #self.signup_button.clicked.connect(self.loginpageShow)
        #######################################

    def register(self):
        name = self.name_line.text()
        username = self.userline.text()
        password = self.passline.text()
        con = sqlite3.connect("userlist.db", timeout=10)
        admin="admin"
        if username!='' and password !='':
            try:
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS "users" ( "ID" INTEGER NOT NULL UNIQUE, "TYPE" TEXT NOT NULL, "NAME" TEXT NOT NULL, "USERNAME" TEXT NOT NULL, "PASSWORD"	TEXT NOT NULL, PRIMARY KEY("ID" AUTOINCREMENT))')
                cur.execute("INSERT INTO users(TYPE,NAME,USERNAME,PASSWORD) VALUES (?,?,?,?)",(admin,name,username,password))
                con.commit()
                cur.close()
                con.close()
                self.showMessageBox('Success', 'User has been registered as admin')
                self.loginpageShow()
            except Exception:
                self.showMessageBox('Database Error','Could not register the the database')
        else:
            self.showMessageBox('Error','Enter some values')
            self.signuppageShow()
    
    def loginpageShow(self):
        self.loginpageWindow = QtWidgets.QMainWindow()
        self.ui = login.Ui_LOGINPAGE()
        self.ui.setupUi(self.loginpageWindow)
        self.loginpageWindow.show()   
    
    def signuppageShow(self):
        self.signuppageWindow =  QtWidgets.QMainWindow()
        self.ui = Ui_SIGNUPPAGE()
        self.ui.setupUi(self.signuppageWindow)
        self.signuppageWindow.show()
    
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def retranslateUi(self, SIGNUPPAGE):
        _translate = QtCore.QCoreApplication.translate
        SIGNUPPAGE.setWindowTitle(_translate("SIGNUPPAGE", "MainWindow"))
        self.username_label.setText(_translate("SIGNUPPAGE", "Username:"))
        self.password_label.setText(_translate("SIGNUPPAGE", "Password:"))
        self.signup_button.setText(_translate("SIGNUPPAGE", "SIGN-UP"))
        self.cancel_button.setText(_translate("SIGNUPPAGE", "CANCEL"))
        self.registration_label.setText(_translate("SIGNUPPAGE", "REGISTRATION"))
        self.firstname_label.setText(_translate("SIGNUPPAGE", "NAME"))


if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        signuppage = QtWidgets.QMainWindow()
        ui = Ui_SIGNUPPAGE()
        ui.setupUi(signuppage)
        signuppage.show()
        sys.exit(app.exec_())