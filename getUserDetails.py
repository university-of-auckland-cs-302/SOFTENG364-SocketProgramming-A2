## GUI for collecting client information
from multiprocessing.sharedctypes import Value
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chat_server import *
from utils import *
from chat_client import* 
from mainPage import MainPage

class GetUserDetails(QWidget):
    
    def __init__(self):
        super().__init__()
        self.layoutUI()
        self.centre()    
        
        # server = QProcess()
        # server.start("python", ['chat_server.py'] , "--name=server --port=5000")
    
    def layoutUI(self):
                
        self.setWindowTitle("Welcome to Chat Hub! Beep Boop ~")
        self.setWindowIcon(QIcon("C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"))
        self.resize(800, 150)
        self.setStyleSheet("background-color: rgb(19,19,19);")
        
        # creating a group box
        self.formGroupBox = QGroupBox("Your Details")
        self.formGroupBox.setStyleSheet("QGroupBox {font: 12pt; color: rgb(255, 255, 255);}")
        
        ##text boxes for user to enter information 
        self.name = QLineEdit()
        self.name.setStyleSheet("QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        self.ipAddy = QLineEdit()
        self.ipAddy.setStyleSheet("QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        self.portNum = QLineEdit()
        self.portNum.setStyleSheet("QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        
        #call function to store information
        self.createForm()
        
        #create buttons
        confirm = QPushButton("Confirm")
        confirm.clicked.connect(self.goToMainPage)
        confirm.setStyleSheet("QPushButton {font: 8pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        
        exit = QPushButton("Exit")
        exit.clicked.connect(self.exitApp);
        exit.setStyleSheet("QPushButton {font: 8pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        
        hBox = QHBoxLayout()
        hBox.addStretch(3)
        hBox.addWidget(confirm)                 
        hBox.addWidget(exit) 
        
        # creating a vertical layout
        mainLayout = QVBoxLayout()
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addLayout(hBox)
        
        # setting lay out
        self.setLayout(mainLayout)
        self.show()
    
    # exit application
    def exitApp(self):
        sys.exit()

    def goToMainPage(self):                
        ipAddy = self.ipAddy.text()
        portNum = int(self.portNum.text())
        name = self.name.text()
        #send client info to make client socket
        client = ChatClient(name, portNum, ipAddy)
        self.connected = MainPage(client, self)
        self.ipAddy.clear()
        self.portNum.clear()
        self.name.clear()
        self.connected.show()
        self.hide()
  
    # create form layout
    def createForm(self):

        # creating a form layout
        intstructions = QLabel("The name you choose will be your name in the chat room... so choose carefully!\n")
        intstructions.setStyleSheet("QLabel {font: 8pt; color: rgb(255, 255, 255);}")
        
        layout = QFormLayout()
        # adding rows for name and adding input text
        # set font size and color for label
        #change size of text and colour of label
        layout.addRow(intstructions)
        layout.addRow(QLabel("Name: "), self.name)
        layout.labelForField(self.name).setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255);}")
        layout.addRow(QLabel("IP Address: "), self.ipAddy)
        layout.labelForField(self.ipAddy).setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255);}")
        layout.addRow(QLabel("Port Number: "), self.portNum)
        layout.labelForField(self.portNum).setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255);}")
  
        # setting layout
        self.formGroupBox.setLayout(layout)
    
    #function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
#create main function that runs the program

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GetUserDetails()
    sys.exit(app.exec_())