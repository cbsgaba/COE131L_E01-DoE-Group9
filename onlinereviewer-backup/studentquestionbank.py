# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentquestionbank.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
import studentmain

class Ui_Question_bank(object):
    def setupUi(self, Question_bank):
        Question_bank.setObjectName("Question_bank")
        Question_bank.resize(501, 419)
        Question_bank.setMinimumSize(QtCore.QSize(501, 419))
        Question_bank.setMaximumSize(QtCore.QSize(501, 419))
        self.centralwidget = QtWidgets.QWidget(Question_bank)
        self.centralwidget.setObjectName("centralwidget")
        self.question_group_box = QtWidgets.QGroupBox(self.centralwidget)
        self.question_group_box.setGeometry(QtCore.QRect(10, 20, 461, 331))
        self.question_group_box.setObjectName("question_group_box")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 461, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_question_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_question_button.setObjectName("cancel_question_button")
        self.horizontalLayout.addWidget(self.cancel_question_button)
        ###############################################################
        self.tableWidget = QtWidgets.QTableWidget(self.question_group_box)
        self.tableWidget.setGeometry(QtCore.QRect(90, 30, 251, 281))
        self.tableWidget.setObjectName("tableWidget")
        #######################################################################
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnHidden(0,True)
        ##########################################################
        self.cancel_question_button.clicked.connect(self.studentmainShow)
        self.cancel_question_button.clicked.connect(Question_bank.close)
    
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 200, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        Question_bank.setCentralWidget(self.centralwidget)

        self.retranslateUi(Question_bank)
        QtCore.QMetaObject.connectSlotsByName(Question_bank)




        try:
            con = sqlite3.connect("userlist.db")
            cur = con.cursor()
            query = "SELECT id,question,answer FROM questionbank WHERE ID!=1 and ID!=2"
            result = cur.execute(query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
            con.close

        except Exception:
            self.showMessageBox('Error',('Could not load the database'))

    def retranslateUi(self, Question_bank):
        _translate = QtCore.QCoreApplication.translate
        Question_bank.setWindowTitle(_translate("Question_bank", "Question Bank"))
        self.question_group_box.setTitle(_translate("Question_bank", "Question Bank"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Question_bank", "Question"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Question_bank", "Answer"))
        self.cancel_question_button.setText(_translate("Question_bank", "Back"))
        
       


    def showMessageBox(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    
    def studentmainShow(self):
        self.studentmainWindow = QtWidgets.QMainWindow()
        self.ui = studentmain.Ui_student_main()
        self.ui.setupUi(self.studentmainWindow)
        self.studentmainWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Question_bank = QtWidgets.QMainWindow()
    ui = Ui_Question_bank()
    ui.setupUi(Question_bank)
    Question_bank.show()
    sys.exit(app.exec_())
