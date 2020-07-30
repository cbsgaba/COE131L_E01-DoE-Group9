# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questionbank.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import adminmain
import sqlite3
import addquestion
import sys
import modifyquestion
import adminmain

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
        self.verticalLayoutWidget = QtWidgets.QWidget(self.question_group_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 110, 161, 132))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.update_question_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.update_question_button.setObjectName("update_question_button")
        self.verticalLayout_2.addWidget(self.update_question_button)
        self.add_question_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_question_button.setObjectName("add_question_button")
        self.verticalLayout_2.addWidget(self.add_question_button)
        self.modify_question_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.modify_question_button.setObjectName("modify_question_button")
        self.verticalLayout_2.addWidget(self.modify_question_button)
        self.delete_question_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_question_button.setObjectName("delete_question_button")
        self.verticalLayout_2.addWidget(self.delete_question_button)
        self.tableWidget = QtWidgets.QTableWidget(self.question_group_box)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 251, 281))
        self.tableWidget.setObjectName("tableWidget")
        #######################################################################
        self.tableWidget.verticalHeader().setVisible(False)
        #self.tableWidget.horizontalHeader().setVisible(False)
        
        ###########################################################################
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setColumnHidden(0,True)
        ##########################################################
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 370, 461, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_question_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.save_question_button.setObjectName("save_question_button")
        self.horizontalLayout.addWidget(self.save_question_button)
        self.cancel_question_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_question_button.setObjectName("cancel_question_button")
        self.horizontalLayout.addWidget(self.cancel_question_button)
        Question_bank.setCentralWidget(self.centralwidget)

        try:
            con = sqlite3.connect("userlist.db")
            cur = con.cursor()
            query = "SELECT id,question,answer FROM questionbank WHERE ID!=1 and ID!=2"
            #query = "SELECT id,question,answer FROM questionbank"
            result = cur.execute(query)
            self.tableWidget.setRowCount(0)

            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
            con.close

        except Exception:
            self.showMessageBox('Error',('Could not load the database'))


        QtCore.QMetaObject.connectSlotsByName(Question_bank)
        ########################################################################
        self.save_question_button.clicked.connect(self.showadminMain)
        self.cancel_question_button.clicked.connect(self.showadminMain)
        self.cancel_question_button.clicked.connect(Question_bank.close)
        self.save_question_button.clicked.connect(Question_bank.close)

        self.add_question_button.clicked.connect(self.showaddquestions)
        self.add_question_button.clicked.connect(Question_bank.close)
        self.delete_question_button.clicked.connect(self.deletequestion)
        self.modify_question_button.clicked.connect(self.modifyquestion)
        self.modify_question_button.clicked.connect(Question_bank.close)
        #self.delete_question_button.clicked.connect(self.)
        #self.update_question_button.clicked.connect(self.loaddata)
        #self.tableWidget.setHorizontalHeader
        self.update_question_button.hide()
        self.retranslateUi(Question_bank)


    # #def loaddata(self):
    #  #   try:
    # #        con = sqlite3.connect("userlist.db")
    # #        cur = con.cursor()
    # #        query = "SELECT id,question,answer FROM questionbank WHERE ID!=1 and ID!=2"
    # #        result = cur.execute(query)
    # #        self.tableWidget.setRowCount(0)
    # ##   
    # #  #      for row_number, row_data in enumerate(result):
    #             self.tableWidget.insertRow(row_number)
    # #            for column_number, data in enumerate(row_data):
    #                 self.tableWidget.setItem(row_number, column_number,QtWidgets.QTableWidgetItem(str(data)))
            
    #         con.close
    #     except Exception:
    #         self.showMessageBox('Error',('Could not load the database'))

 #   def modifyquestion(self):
        
    def showaddquestions(self):
        self.addquestionwindow =  QtWidgets.QMainWindow()
        self.ui = addquestion.Ui_add_question()
        self.ui.setupUi(self.addquestionwindow)
        self.addquestionwindow.show()

    def modifyquestion(self):
        if self.tableWidget.selectionModel().hasSelection():
            row = self.tableWidget.currentRow()
            question_id=(self.tableWidget.item(row,0).text())
            print(question_id) 

        try:
            con = sqlite3.connect("userlist.db")
            cur = con.cursor()   
            cur.execute("SELECT * FROM questionbank WHERE ID=?",(question_id,))
            data = cur.fetchall()
            con.commit()
            for row in data:
                question = row[1]
                answer = row[2]


            cur.execute('UPDATE questionbank SET QUESTION=?,ANSWER=?,MODIFY=? WHERE ID=2',(question,answer,question_id,))
            con.commit()
            con.close()

        except Exception:
            self.showMessageBox('Error', 'Could not load the database.')    

        self.modifyquestionWindow = QtWidgets.QMainWindow()
        self.ui = modifyquestion.Ui_modify_question()
        self.ui.setupUi(self.modifyquestionWindow)
        self.modifyquestionWindow.show()

    
    def deletequestion(self):
        if self.tableWidget.selectionModel().hasSelection():
            row = self.tableWidget.currentRow()
            question_id=(self.tableWidget.item(row,0).text())
            print(question_id)
       # try:
        con = sqlite3.connect("userlist.db")
        cur = con.cursor()
        cur.execute("DELETE from questionbank WHERE ID = ?",(question_id,))
        print(question_id)
        self.tableWidget.removeRow(row)
        con.commit()
        con.close()
        self.showMessageBox('Successful','Deleted From Table Successful')
       # except Exception:
            #self.showMessageBox('Error', 'Could not Delete student from the database.')
    
    def showadminMain(self):
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

    def retranslateUi(self, Question_bank):
        _translate = QtCore.QCoreApplication.translate
        Question_bank.setWindowTitle(_translate("Question_bank", "Question Bank"))
        self.question_group_box.setTitle(_translate("Question_bank", "Question Bank"))
        self.update_question_button.setText(_translate("Question_bank", "Update"))
        self.add_question_button.setText(_translate("Question_bank", "Add"))
        self.modify_question_button.setText(_translate("Question_bank", "Modify"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Question"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Answer"))
        self.delete_question_button.setText(_translate("Question_bank", "Delete"))
        self.save_question_button.setText(_translate("Question_bank", "Save"))
        self.cancel_question_button.setText(_translate("Question_bank", "Cancel"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    questionbankpage = QtWidgets.QMainWindow()
    ui = Ui_Question_bank()
    ui.setupUi(questionbankpage)
    questionbankpage.show()
    sys.exit(app.exec_())