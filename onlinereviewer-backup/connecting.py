# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connecting.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3
import adminmain

class Ui_connecting(object):
    def setupUi(self, connecting):
        connecting.setObjectName("connecting")
        connecting.resize(338, 75)
        connecting.setMinimumSize(QtCore.QSize(338, 75))
        connecting.setMaximumSize(QtCore.QSize(338, 75))
        self.centralwidget = QtWidgets.QWidget(connecting)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 131, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 40, 93, 28))
        self.pushButton.setObjectName("pushButton")
        connecting.setCentralWidget(self.centralwidget)

        self.retranslateUi(connecting)
        QtCore.QMetaObject.connectSlotsByName(connecting)
        ##########################################################
        self.pushButton.clicked.connect(self.adminmainShow)
        self.pushButton.clicked.connect(connecting.close)
        ###########################################################
        try:
            con = sqlite3.connect("userlist.db")
            cur = con.cursor()
            cur.execute('SELECT * FROM users WHERE ID=1')
            data = cur.fetchall()
            con.commit()

            for row in data:
                usertype = row[1]
                name = row[2]
                username = row[3]
                password = row[4]

            cur.execute('UPDATE users SET TYPE=?,NAME=?,USERNAME=?,PASSWORD=? WHERE ID=1',(usertype,name,username,password))
            con.commit()
            con.close()
        except Exception:
            self.showMessageBox('Database Error','Could not access the database')

        ###############################################################
    
    def adminmainShow(self):
        self.adminmainWindow = QtWidgets.QMainWindow()
        self.ui = adminmain.Ui_admin_main()
        self.ui.setupUi(self.adminmainWindow)
        self.adminmainWindow.show()
        
    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def retranslateUi(self, connecting):
        _translate = QtCore.QCoreApplication.translate
        connecting.setWindowTitle(_translate("connecting", "Connecting..."))
        self.label.setText(_translate("connecting", "Updating Data Base..."))
        self.pushButton.setText(_translate("connecting", "Ok"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    connectingpage = QtWidgets.QMainWindow()
    ui = Ui_connecting()
    ui.setupUi(connectingpage)
    connectingpage.show()
    sys.exit(app.exec_())