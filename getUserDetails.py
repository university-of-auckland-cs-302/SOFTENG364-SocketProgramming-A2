## GUI for collecting client information
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from utils import *
from chatClient import *
from mainPage import MainPage


class GetUserDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.layoutUI()
        self.centre()
        self.client = None

        # server = QProcess()
        # server.start("python", ['chat_server.py'] , "--name=server --port=5000")

    def layoutUI(self):
        self.setWindowTitle("Welcome to Chat Hub! Beep Boop ~")
        self.setWindowIcon(
            QIcon(
                "C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"
            )
        )
        self.resize(800, 150)
        self.setStyleSheet("background-color: rgb(19,19,19);")

        # add text boxes for user to enter information
        self.name = QLineEdit()
        self.ipAddy = QLineEdit()
        self.portNum = QLineEdit()

        # creating a group box
        self.formGroupBox = QGroupBox("Your Details")
        # call function to create form that stores information
        self.createForm(self.name, self.ipAddy, self.portNum)

        # create buttons
        self.confirm = QPushButton("Confirm")
        self.confirm.clicked.connect(self.goToMainPage)
        self.exit = QPushButton("Exit")
        self.exit.clicked.connect(self.exitApp)

        hBox = QHBoxLayout()
        hBox.addStretch(3)
        hBox.addWidget(self.confirm)
        hBox.addWidget(self.exit)

        # creating a vertical layout
        mainLayout = QVBoxLayout()
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addLayout(hBox)

        # setting lay out
        self.customise()
        self.setLayout(mainLayout)
        self.show()

    # set stylesheet for the app
    def customise(self):
        self.formGroupBox.setStyleSheet(
            "QGroupBox {font: 12pt; color: rgb(255, 255, 255);}"
        )
        self.name.setStyleSheet(
            "QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )
        self.ipAddy.setStyleSheet(
            "QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )
        self.portNum.setStyleSheet(
            "QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )
        self.confirm.setStyleSheet(
            "QPushButton {font: 8pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )
        self.exit.setStyleSheet(
            "QPushButton {font: 8pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )
        self.instructions.setStyleSheet(
            "QLabel {font: 8pt; color: rgb(255, 255, 255);}"
        )
        self.layout.labelForField(self.name).setStyleSheet(
            "QLabel {font: 12pt; color: rgb(255, 255, 255);}"
        )
        self.layout.labelForField(self.ipAddy).setStyleSheet(
            "QLabel {font: 12pt; color: rgb(255, 255, 255);}"
        )
        self.layout.labelForField(self.portNum).setStyleSheet(
            "QLabel {font: 12pt; color: rgb(255, 255, 255);}"
        )

    # create form layout
    def createForm(self, name, ipAddy, portNum):
        self.name = name
        self.ipAddy = ipAddy
        self.portNum = portNum
        self.instructions = QLabel(
            "The name you choose will be your name in the chat room... so choose carefully!\n"
        )
        self.layout = QFormLayout()
        # adding rows for name and adding input text
        self.layout.addRow(self.instructions)
        self.layout.addRow(QLabel("Name: "), self.name)
        self.layout.addRow(QLabel("IP Address: "), self.ipAddy)
        self.layout.addRow(QLabel("Port Number: "), self.portNum)
        # set layout
        self.formGroupBox.setLayout(self.layout)

    # function to go to main page
    def goToMainPage(self):
        # get user details
        ipAddy = self.ipAddy.text()
        portNum = int(self.portNum.text())
        name = self.name.text()
        # send client info to create client socket
        self.client = ChatClient(name, portNum, ipAddy)
        self.connectTo = MainPage(self.client, self)
        self.ipAddy.clear()
        self.portNum.clear()
        self.name.clear()
        self.connectTo.show()
        self.hide()

    # exit application
    def exitApp(self):
        self.client.cleanup()
        QCoreApplication.instance().quit()

    def closeEvent(self, event):
        self.client.cleanup()
        event.accept()

    # function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


# create main function that runs the program for testing purposes
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GetUserDetails()
    sys.exit(app.exec_())
