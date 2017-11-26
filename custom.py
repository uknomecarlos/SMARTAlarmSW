import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel
from PyQt5 import QtWidgets, QtGui
#from main import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 387)
        self.Middle2 = QtWidgets.QLineEdit(Dialog)
        self.Middle2.setGeometry(QtCore.QRect(190, 140, 31, 27))
        self.Middle2.setObjectName("Middle2")
        self.Left2 = QtWidgets.QLineEdit(Dialog)
        self.Left2.setGeometry(QtCore.QRect(260, 140, 31, 27))
        self.Left2.setObjectName("Left2")
        self.OK_Button = QtWidgets.QPushButton(Dialog)
        self.OK_Button.setGeometry(QtCore.QRect(290, 330, 99, 27))
        self.OK_Button.setObjectName("OK_Button")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(190, 80, 67, 17))
        self.label_8.setObjectName("label_8")
        self.Right5 = QtWidgets.QLineEdit(Dialog)
        self.Right5.setGeometry(QtCore.QRect(120, 230, 31, 27))
        self.Right5.setObjectName("Right5")
        self.Middle4 = QtWidgets.QLineEdit(Dialog)
        self.Middle4.setGeometry(QtCore.QRect(190, 200, 31, 27))
        self.Middle4.setObjectName("Middle4")
        self.Left4 = QtWidgets.QLineEdit(Dialog)
        self.Left4.setGeometry(QtCore.QRect(260, 200, 31, 27))
        self.Left4.setObjectName("Left4")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 17))
        self.label.setObjectName("label")
        self.Left5 = QtWidgets.QLineEdit(Dialog)
        self.Left5.setGeometry(QtCore.QRect(260, 230, 31, 27))
        self.Left5.setObjectName("Left5")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(260, 80, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 80, 67, 17))
        self.label_7.setObjectName("label_7")
        self.Middle5 = QtWidgets.QLineEdit(Dialog)
        self.Middle5.setGeometry(QtCore.QRect(190, 230, 31, 27))
        self.Middle5.setObjectName("Middle5")
        self.Right1 = QtWidgets.QLineEdit(Dialog)
        self.Right1.setGeometry(QtCore.QRect(120, 110, 31, 27))
        self.Right1.setObjectName("Right1")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(20, 40, 201, 17))
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 67, 17))
        self.label_2.setObjectName("label_2")
        self.Middle3 = QtWidgets.QLineEdit(Dialog)
        self.Middle3.setGeometry(QtCore.QRect(190, 170, 31, 27))
        self.Middle3.setObjectName("Middle3")
        self.Middle1 = QtWidgets.QLineEdit(Dialog)
        self.Middle1.setGeometry(QtCore.QRect(190, 110, 31, 27))
        self.Middle1.setObjectName("Middle1")
        self.Right2 = QtWidgets.QLineEdit(Dialog)
        self.Right2.setGeometry(QtCore.QRect(120, 140, 31, 27))
        self.Right2.setObjectName("Right2")
        self.Right4 = QtWidgets.QLineEdit(Dialog)
        self.Right4.setGeometry(QtCore.QRect(120, 200, 31, 27))
        self.Right4.setObjectName("Right4")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(30, 230, 67, 17))
        self.label_6.setObjectName("label_6")
        self.Right3 = QtWidgets.QLineEdit(Dialog)
        self.Right3.setGeometry(QtCore.QRect(120, 170, 31, 27))
        self.Right3.setObjectName("Right3")
        self.Left1 = QtWidgets.QLineEdit(Dialog)
        self.Left1.setGeometry(QtCore.QRect(260, 110, 31, 27))
        self.Left1.setObjectName("Left1")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 170, 67, 17))
        self.label_4.setObjectName("label_4")
        self.Left3 = QtWidgets.QLineEdit(Dialog)
        self.Left3.setGeometry(QtCore.QRect(260, 170, 31, 27))
        self.Left3.setObjectName("Left3")

        self.OK_Button.clicked.connect(self.ok_button)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.OK_Button.setText(_translate("Dialog", "OK"))
        self.label_3.setText(_translate("Dialog", "Alarm 2:"))
        self.label_5.setText(_translate("Dialog", "Alarm 4:"))
        self.label_8.setText(_translate("Dialog", "Middle"))
        self.label.setText(_translate("Dialog", "Alarms Available: 1, 2, 3, 4, 5"))
        self.label_9.setText(_translate("Dialog", "Left"))
        self.label_7.setText(_translate("Dialog", "Right"))
        self.label_10.setText(_translate("Dialog", "Exits Available: 6, 7, 8"))
        self.label_2.setText(_translate("Dialog", "Alarm 1:"))
        self.label_6.setText(_translate("Dialog", "Alarm 5:"))
        self.label_4.setText(_translate("Dialog", "Alarm 3:"))

    def ok_button(self):
        print("ok button has been pressed")

        #confirm_custom = QMessageBox.question(self,"Message", "Are you sure you wish to monitor this custom setting?",
        #               QMessageBox.Yes | QMessageBox.No, QMessageBox.No)


        #if confirm_custom == QMessageBox.Yes:
            # 5 alarms, Straight line, exit on either side, middle alarm (3) detects fire
            # From Fig. 46 (p. 116) in "SMART Alarm System SD1 Documentation.pdf"

        all_pois = []  # list containing every POI in system
        visited = []  # a boolean value corresponding to each POI and it's ID

        set_poi(all_pois, visited, 5, 3)
        wall = all_pois[0]

        print(int(self.Middle1.text()))

        # initialize the connections from one alarm to another
        all_pois[1].set_all(all_pois[int(self.Right1.text())], all_pois[int(self.Middle1.text())], all_pois[int(self.Left1.text())])
        all_pois[2].set_all(all_pois[int(self.Right2.text())], all_pois[int(self.Middle2.text())], all_pois[int(self.Left2.text())])
        all_pois[3].set_all(all_pois[int(self.Right3.text())], all_pois[int(self.Middle3.text())], all_pois[int(self.Left3.text())])
        all_pois[4].set_all(all_pois[int(self.Right4.text())], all_pois[int(self.Middle4.text())], all_pois[int(self.Left4.text())])
        all_pois[5].set_all(all_pois[int(self.Right5.text())], all_pois[int(self.Middle5.text())], all_pois[int(self.Left5.text())])

        print " "
        print "Test Case 1: "
        print " "

        # set off fire at alarm 3
        fire_alarm(all_pois[3], visited)
        print_each_direction(all_pois)


        #else:
        #    pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
