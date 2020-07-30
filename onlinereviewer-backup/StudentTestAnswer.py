# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentTestAnswer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import studentmain
import performanceassesment

import sys
import sqlite3


class Ui_ReviewerTest(object):
    def setupUi(self, ReviewerTest):
        ReviewerTest.setObjectName("ReviewerTest")
        ReviewerTest.resize(727, 590)
        self.centralwidget = QtWidgets.QWidget(ReviewerTest)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 511, 471))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 492, 972))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Q1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q1.setObjectName("Q1")
        self.verticalLayout.addWidget(self.Q1)
        self.Q1DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q1DB.setObjectName("Q1DB")
        self.verticalLayout.addWidget(self.Q1DB)
        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.Q2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q2.setObjectName("Q2")
        self.verticalLayout.addWidget(self.Q2)
        self.Q2DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q2DB.setObjectName("Q2DB")
        self.verticalLayout.addWidget(self.Q2DB)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.Q3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q3.setObjectName("Q3")
        self.verticalLayout.addWidget(self.Q3)
        self.Q3DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q3DB.setObjectName("Q3DB")
        self.verticalLayout.addWidget(self.Q3DB)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.Q4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q4.setObjectName("Q4")
        self.verticalLayout.addWidget(self.Q4)
        self.Q4DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q4DB.setObjectName("Q4DB")
        self.verticalLayout.addWidget(self.Q4DB)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.Q5DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q5DB.setObjectName("Q5DB")
        self.verticalLayout.addWidget(self.Q5DB)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout.addWidget(self.lineEdit_5)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.Q6DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q6DB.setObjectName("Q6DB")
        self.verticalLayout.addWidget(self.Q6DB)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout.addWidget(self.lineEdit_6)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.Q7DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q7DB.setObjectName("Q7DB")
        self.verticalLayout.addWidget(self.Q7DB)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout.addWidget(self.lineEdit_7)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.Q8DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q8DB.setObjectName("Q8DB")
        self.verticalLayout.addWidget(self.Q8DB)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout.addWidget(self.lineEdit_8)
        self.Q9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q9.setObjectName("Q9")
        self.verticalLayout.addWidget(self.Q9)
        self.Q9DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q9DB.setObjectName("Q9DB")
        self.verticalLayout.addWidget(self.Q9DB)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout.addWidget(self.lineEdit_9)
        self.Q10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q10.setObjectName("Q10")
        self.verticalLayout.addWidget(self.Q10)
        self.Q10DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q10DB.setObjectName("Q10DB")
        self.verticalLayout.addWidget(self.Q10DB)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout.addWidget(self.lineEdit_10)
        self.Q10_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q10_2.setObjectName("Q10_2")
        self.verticalLayout.addWidget(self.Q10_2)
        self.Q11DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q11DB.setObjectName("Q11DB")
        self.verticalLayout.addWidget(self.Q11DB)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout.addWidget(self.lineEdit_11)
        self.Q10_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q10_3.setObjectName("Q10_3")
        self.verticalLayout.addWidget(self.Q10_3)
        self.Q12DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q12DB.setObjectName("Q12DB")
        self.verticalLayout.addWidget(self.Q12DB)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout.addWidget(self.lineEdit_12)
        self.Q10_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q10_4.setObjectName("Q10_4")
        self.verticalLayout.addWidget(self.Q10_4)
        self.Q13DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q13DB.setObjectName("Q13DB")
        self.verticalLayout.addWidget(self.Q13DB)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.verticalLayout.addWidget(self.lineEdit_13)
        self.Q10_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q10_5.setObjectName("Q10_5")
        self.verticalLayout.addWidget(self.Q10_5)
        self.Q14DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q14DB.setObjectName("Q14DB")
        self.verticalLayout.addWidget(self.Q14DB)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.verticalLayout.addWidget(self.lineEdit_14)
        self.Q10_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q10_6.setObjectName("Q10_6")
        self.verticalLayout.addWidget(self.Q10_6)
        self.Q15DB = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Q15DB.setObjectName("Q15DB")
        self.verticalLayout.addWidget(self.Q15DB)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.verticalLayout.addWidget(self.lineEdit_15)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(180, 20, 231, 31))
        self.Title.setObjectName("Title")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 80, 61, 31))
        self.label.setObjectName("label")
        self.ScoreDB = QtWidgets.QLabel(self.centralwidget)
        self.ScoreDB.setGeometry(QtCore.QRect(580, 130, 71, 16))
        self.ScoreDB.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ScoreDB.setFont(font)
        self.ScoreDB.setObjectName("ScoreDB")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 440, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 480, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.ScoreDB_2 = QtWidgets.QLabel(self.centralwidget)
        self.ScoreDB_2.setGeometry(QtCore.QRect(580, 170, 71, 16))
        self.ScoreDB_2.setObjectName("ScoreDB_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(580, 150, 71, 20))
        self.label_3.setObjectName("label_3")
        ReviewerTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ReviewerTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 21))
        self.menubar.setObjectName("menubar")
        ReviewerTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ReviewerTest)
        self.statusbar.setObjectName("statusbar")
        ReviewerTest.setStatusBar(self.statusbar)

        self.retranslateUi(ReviewerTest)
        QtCore.QMetaObject.connectSlotsByName(ReviewerTest)
        ################################
        self.pushButton.clicked.connect(self.SubmitAnswer)
        self.pushButton.clicked.connect(self.showperformanceassess)
        self.pushButton.clicked.connect(ReviewerTest.close)
        ################################
        self.pushButton_2.clicked.connect(self.studentmainShow)
        self.pushButton_2.clicked.connect(ReviewerTest.close)
        data = 'null'
        question = []
        try:
            con = sqlite3.connect("userlist.db",timeout=10)
            cur = con.cursor()
            cur.execute('SELECT * FROM questionbank ORDER BY RANDOM() LIMIT 15')
            data = cur.fetchall()
            con.commit
            for row in data:
                data = row[1]
                question.append(data)
            con.close
            
            self.Q1DB.setText(question[0])
            self.Q2DB.setText(question[1])
            self.Q3DB.setText(question[2])
            self.Q4DB.setText(question[3])
            self.Q5DB.setText(question[4])
            self.Q6DB.setText(question[5])
            self.Q7DB.setText(question[6])
            self.Q8DB.setText(question[7])
            self.Q9DB.setText(question[8])
            self.Q10DB.setText(question[9])
            self.Q11DB.setText(question[10])
            self.Q12DB.setText(question[11])
            self.Q13DB.setText(question[12])
            self.Q14DB.setText(question[13])
            self.Q15DB.setText(question[14])
        except Exception:
            self.showMessageBox('Database Error','Could not access the database')
        ##########################################################################
    
        




    def retranslateUi(self, ReviewerTest):
        _translate = QtCore.QCoreApplication.translate
        ReviewerTest.setWindowTitle(_translate("ReviewerTest", "Reviewer Test"))
        self.Q1.setText(_translate("ReviewerTest", "Question 1"))
        self.Q1DB.setText(_translate("ReviewerTest", "Q1DB"))
        self.Q2.setText(_translate("ReviewerTest", "Question 2 :"))
        self.Q2DB.setText(_translate("ReviewerTest", "Q2DB"))
        self.Q3.setText(_translate("ReviewerTest", "Question 3 :"))
        self.Q3DB.setText(_translate("ReviewerTest", "Q3DB"))
        self.Q4.setText(_translate("ReviewerTest", "Question 4 :"))
        self.Q4DB.setText(_translate("ReviewerTest", "Q4DB"))
        self.label_10.setText(_translate("ReviewerTest", "Question 5 :"))
        self.Q5DB.setText(_translate("ReviewerTest", "Q5DB"))
        self.label_12.setText(_translate("ReviewerTest", "Question 6 :"))
        self.Q6DB.setText(_translate("ReviewerTest", "Q6DB"))
        self.label_14.setText(_translate("ReviewerTest", "Question 7 :"))
        self.Q7DB.setText(_translate("ReviewerTest", "Q7DB"))
        self.label_16.setText(_translate("ReviewerTest", "Question 8:"))
        self.Q8DB.setText(_translate("ReviewerTest", "Q8DB"))
        self.Q9.setText(_translate("ReviewerTest", "Question 9:"))
        self.Q9DB.setText(_translate("ReviewerTest", "Q9DB"))
        self.Q10.setText(_translate("ReviewerTest", "Question 10:"))
        self.Q10DB.setText(_translate("ReviewerTest", "Q10DB"))
        self.Q10_2.setText(_translate("ReviewerTest", "Question 11:"))
        self.Q11DB.setText(_translate("ReviewerTest", "Q11DB"))
        self.Q10_3.setText(_translate("ReviewerTest", "Question 12:"))
        self.Q12DB.setText(_translate("ReviewerTest", "Q12DB"))
        self.Q10_4.setText(_translate("ReviewerTest", "Question 13:"))
        self.Q13DB.setText(_translate("ReviewerTest", "Q13DB"))
        self.Q10_5.setText(_translate("ReviewerTest", "Question 14:"))
        self.Q14DB.setText(_translate("ReviewerTest", "Q14DB"))
        self.Q10_6.setText(_translate("ReviewerTest", "Question 15:"))
        self.Q15DB.setText(_translate("ReviewerTest", "Q15DB"))
        self.Title.setText(_translate("ReviewerTest", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Reviewer Test</span></p></body></html>"))
        self.label.setText(_translate("ReviewerTest", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Score</span></p></body></html>"))
        self.ScoreDB.setText(_translate("ReviewerTest", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">0</span></p></body></html>"))
        self.pushButton.setText(_translate("ReviewerTest", "Submit"))
        self.pushButton_2.setText(_translate("ReviewerTest", "Back"))
        self.ScoreDB_2.setText(_translate("ReviewerTest", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">15</span></p></body></html>"))
        self.label_3.setText(_translate("ReviewerTest", "<html><head/><body><p><span style=\" font-weight:600;\">-------------------------</span></p></body></html>"))

    ############################################
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
   
    def showperformanceassess(self):
       self.asseswindow = QtWidgets.QMainWindow()
       self.ui = performanceassesment.Ui_performanceassesment()
       self.ui.setupUi(self.asseswindow)
       self.asseswindow.show()

    def SubmitAnswer(self):
        score = 0
        q1 = self.Q1DB.text()
        ans1 = self.lineEdit.text()
        q2 = self.Q2DB.text()
        ans2 = self.lineEdit_2.text()
        q3 = self.Q3DB.text()
        ans3 = self.lineEdit_3.text()
        q4 = self.Q4DB.text()
        ans4 = self.lineEdit_4.text()
        q5 = self.Q5DB.text()
        ans5 = self.lineEdit_5.text()
        q6 = self.Q6DB.text()
        ans6 = self.lineEdit_6.text()
        q7 = self.Q7DB.text()
        ans7 = self.lineEdit_7.text()
        q8 = self.Q8DB.text()
        ans8 = self.lineEdit_8.text()
        q9 = self.Q9DB.text()
        ans9 = self.lineEdit_9.text()
        q10 = self.Q10DB.text()
        ans10 = self.lineEdit_10.text()
        q11 = self.Q11DB.text()
        ans11 = self.lineEdit_11.text()
        q12 = self.Q12DB.text()
        ans12 = self.lineEdit_12.text()
        q13 = self.Q13DB.text()
        ans13 = self.lineEdit_13.text()
        q14 = self.Q14DB.text()
        ans14 = self.lineEdit_14.text()
        q15 = self.Q15DB.text()
        ans15 = self.lineEdit_15.text()
        
        try:
            con = sqlite3.connect("userlist.db")
            cur = con.cursor()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q1,ans1)) 
            final1 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q2,ans2)) 
            final2 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q3,ans3)) 
            final3 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q4,ans4)) 
            final4 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q5,ans5)) 
            final5 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q6,ans6)) 
            final6 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q7,ans7)) 
            final7 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q8,ans8)) 
            final8 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q9,ans9)) 
            final9 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q10,ans10)) 
            final10 = cur.fetchone()

            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q11,ans11)) 
            final11 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q12,ans12)) 
            final12 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q13,ans13)) 
            final13 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q14,ans14)) 
            final14 = cur.fetchone()
            cur.execute('SELECT * FROM questionbank WHERE QUESTION = ? AND ANSWER = ?',(q15,ans15)) 
            final15 = cur.fetchone()
            con.commit()
            print(final1)
            print(final2)
            print(final3)
            print(final4)
            print(final5)
            print(final6)
            print(final7)
            print(final8)
            print(final9)
            print(final10)
            print(final11)
            print(final12)
            print(final13)
            print(final14)
            print(final15)
            if final1 != None:
                score = score + 1
            if final2 != None:
                score = score + 1
            if final3 != None:
                score = score + 1
            if final4 != None:
                score = score + 1
            if final5 != None:
                score = score + 1
            if final6 != None:
                score = score + 1
            if final7 != None:
                score = score + 1
            if final8 != None:
                score = score + 1
            if final9 != None:
                score = score + 1
            if final10 != None:
                score = score + 1
            if final11 != None:
                score = score + 1
            if final12 != None:
                score = score + 1
            if final13 != None:
                score = score + 1
            if final14 != None:
                score = score + 1
            if final15 != None:
                score = score + 1
            else:
                score = score + 0


            print(score)
            cur.execute('UPDATE questionbank SET MODIFY=? WHERE ID=1',(score,))
            cur.execute('UPDATE users SET SCORE=? WHERE ID= 5',(score,))
            con.commit()
            cur.execute('SELECT MODIFY FROM users WHERE ID= 5')
            data=cur.fetchall()
            con.commit()
            for row in data:
                idq = row[0]
            cur.execute('UPDATE users SET SCORE = ? WHERE ID= ?', (score,idq,))
            con.commit()

            self.ScoreDB.setText(str(score))
            print(idq)
            con.close()
                    
        except:
            self.showMessageBox('Database Error','Could not access the database')

           


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReviewerTest = QtWidgets.QMainWindow()
    ui = Ui_ReviewerTest()
    ui.setupUi(ReviewerTest)
    ReviewerTest.show()
    sys.exit(app.exec_())
