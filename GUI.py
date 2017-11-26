import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QLabel, QDialog
from custom import Ui_Dialog
#from main import *


class window(QMainWindow):

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 691, 451)
        self.setWindowTitle('SMART Alarm Manager')
        self.setWindowIcon(QIcon('logo.jpeg'))
        self.status = 'None Selected'
        self.monitoring = False
        self.home()

    def home(self):
        LineButton = QPushButton('In-Line', self)
        LineButton.resize(111,91)
        LineButton.move(0,0)
        TButton = QPushButton('T-Shape', self)
        TButton.resize(111,91)
        TButton.move(0,90)
        LButton = QPushButton('L-Shape', self)
        LButton.resize(111,91)
        LButton.move(0,180)
        CustomButton = QPushButton('Custom', self)
        CustomButton.resize(111,91)
        CustomButton.move(0,270)
        ResetButton = QPushButton('Reset', self)
        ResetButton.resize(111,91)
        ResetButton.move(0,360)
        MonitorButton = QPushButton('Run Monitoring', self)
        MonitorButton.resize(131,61)
        MonitorButton.move(560,0)
        myButtons = {LineButton, TButton, LButton, CustomButton, ResetButton, MonitorButton}

        status = QLabel(self)
        status.setText(self.status)
        status.setGeometry(560,60,131,61)
        status.setStyleSheet('background: white')
        status.setAlignment(QtCore.Qt.AlignCenter)

        label = QLabel(self)
        pixmap = QPixmap('logo450.jpg')
        label.setPixmap(pixmap)
        label.move(110,0)
        label.resize(450,450)

        LineButton.clicked.connect(lambda: self.line_button(label, myButtons, LineButton, status))

        TButton.clicked.connect(lambda: self.tshape_button(label, myButtons, TButton, status))

        LButton.clicked.connect(lambda: self.lshape_button(label, myButtons, LButton, status))

        CustomButton.clicked.connect(lambda: self.custom_button(label, myButtons, CustomButton, MonitorButton, status))

        ResetButton.setEnabled(False)
        ResetButton.clicked.connect(lambda: self.reset_button(label, myButtons, ResetButton, MonitorButton, status))

        MonitorButton.setEnabled(False)
        MonitorButton.clicked.connect(lambda: self.monitor_button(label, myButtons, ResetButton, status))

        self.show()

    def line_button(self, label, btns, this_btn, status):
        print("set Alarms in Line formation")
        self.status = "Line"
        pixmap = QPixmap('line450.jpg')
        label.setPixmap(pixmap)
        for btn in btns:
            btn.setEnabled(True)
        this_btn.setEnabled(False)
        status.setText(self.status + "\nSelected")

    def tshape_button(self, label, btns, this_btn, status):
        print("set Alarms in T-Shape formation")
        self.status = "T-Shape"
        pixmap = QPixmap('t-shape450.jpg')
        label.setPixmap(pixmap)
        for btn in btns:
            btn.setEnabled(True)
        this_btn.setEnabled(False)
        status.setText(self.status + "\nSelected")

    def lshape_button(self, label, btns, this_btn, status):
        print("set Alarms in L-Shape formation")
        self.status = "L-Shape"
        pixmap = QPixmap('l-shape450.jpg')
        label.setPixmap(pixmap)
        for btn in btns:
            btn.setEnabled(True)
        this_btn.setEnabled(False)
        status.setText(self.status + "\nSelected")

    def custom_button(self, label, btns, this_btn, monitor_btn, status):
        print("set Alarms in Custom formation")
        self.status = "Custom"
        pixmap = QPixmap('logo450.jpg')
        label.setPixmap(pixmap)
        for btn in btns:
            btn.setEnabled(True)
        this_btn.setEnabled(False)
        monitor_btn.setEnabled(False)
        status.setText("Monitoring \n" + self.status + "...")
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()


    def reset_button(self, label, btns, reset, monitor,status):
        print("Reset Alarms")

        reset_check = QMessageBox.question(self, 'Message', "Are you sure you wish to reset the application?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reset_check == QMessageBox.Yes:
            pixmap = QPixmap('logo450.jpg')
            label.setPixmap(pixmap)
            for btn in btns:
                btn.setEnabled(True)
            reset.setEnabled(False)
            monitor.setEnabled(False)
            status.setText("None Selected")

            # stop directional algorithm

    def monitor_button(self, label, btns, reset, status):
        monitor = QMessageBox.question(self, 'Message', "Are you sure you want to monitor the alarms in the "
                                       + self.status + " configuration?", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.No)
        if monitor == QMessageBox.Yes:
            pixmap = QPixmap('logo450.jpg')
            label.setPixmap(pixmap)
            self.monitoring = True
            for btn in btns:
                btn.setEnabled(False)
            reset.setEnabled(True)


            print("Monitoring " + self.status + "...")
            status.setText("Monitoring \n" + self.status + "...")
        else:
            pass


def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()
