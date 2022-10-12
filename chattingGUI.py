## GUI for chatting app using socket programming in python
from multiprocessing.sharedctypes import Value
from re import X
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import QThread, pyqtSignal
from pathlib import Path
import os, gzip, shutil
from chat_server import *
from utils import *
from chat_client import* 
from datetime import datetime

class MainPage(QMainWindow):
    #create a title for the window that is displayed in the center of the layout
    def __init__(self):
        super().__init__()
        self.MainPageWidgets = MainPageWidgets(self)
        self.setCentralWidget(self.MainPageWidgets)
        self.resize(600, 600)
        self.setStyleSheet("background-color: rgb(19,19,19);")
        self.createLayout()
    
    #function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def createLayout(self):

        #create a label to hold the title
        self.setWindowTitle("Hi!. This is the main page of Chat Hub! Beep Boop!")
        self.centre()
        self.show()

#create a class for the main window widgets
class MainPageWidgets(QWidget):
    
    def __init__(self, parent):
        super(MainPageWidgets, self).__init__(parent)
        
        #Create label for welcome message
        welcomeMessage = QLabel("\\( .  '   ⌣   '  . )/\n\nWelcome to Chat Hub\nwould you like to...", self)
        welcomeMessage.setStyleSheet("QLabel {font: 24pt; color: rgb(255, 255, 255);}")
        welcomeMessage.setAlignment(Qt.AlignHCenter)
        
        #create buttons for the main window
        createChatRoom = QPushButton("Create a chat room")
        createChatRoom.setStyleSheet("QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        # createChatRoom.clicked.connect(self.createChatClicked);
        self.collectDetails = GetUserDetails(self)
        
        joinChatRoom = QPushButton("Join a chat room")
        joinChatRoom.setStyleSheet("QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        # joinChatRoom.clicked.connect(self.JoinChatClicked);
        # self.joinRoom = joinRoom(self)
        
        #initialising horizontal box layout
        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(createChatRoom)
        hBox.addWidget(joinChatRoom)
        hBox.addStretch(1)
        
        #initialising vertical box layout
        vBox = QVBoxLayout()
        vBox.addStretch(5)
        vBox.addWidget(welcomeMessage)
        vBox.addStretch(1)
        vBox.addLayout(hBox)
        vBox.addStretch(5)
        
        #set the layout and show all widgets
        self.setLayout(vBox)
        self.show()
        
    def createChatClicked(self):
        self.collectDetails.show()
        self.close()
        
    def JoinChatClicked(self):
        self.joinRoom.show()
        self.close()
    
    def StartRoom(self):
        self.startRoom.show()
        self.close()
        
    
class GetUserDetails(QWidget):
    
    def __init__(self, parent):
        super(GetUserDetails, self).__init__(parent)
        
        self.setWindowTitle("The name you choose will be your name in the chat room... so choose carefully! Beep Boop ~")
        self.resize(800, 200)
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
        
        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
  
        # adding action when form is rejected
        self.buttonBox.rejected.connect(self.reject)
  
        # creating a vertical layout
        mainLayout = QVBoxLayout()
        # adding form group box to the layout
        mainLayout.addWidget(self.formGroupBox)                 
        # adding button box to the layout
        mainLayout.addWidget(self.buttonBox)
        
        # setting lay out
        self.setLayout(mainLayout)
        self.show()
  
    # creat form method
    def createForm(self):
  
        # creating a form layout
        layout = QFormLayout()
  
        # adding rows
        # for name and adding input text
        layout.addRow(QLabel("Name: "), self.name)
        layout.labelForField(self.name).setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255);}")
        layout.addRow(QLabel("IP Address: "), self.ipAddy)
        layout.labelForField(self.ipAddy).setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255);}")
        layout.addRow(QLabel("Port Number: "), self.portNum)
        layout.labelForField(self.portNum).setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255);}")
  
        # setting layout
        self.formGroupBox.setLayout(layout)
        
# class OpenRoom(QMainWindow):
    
#     def __init__(self, parent):
#         super(OpenRoom, self).__init__(parent)
#         self.OpenRoomWidgets = OpenRoomWidgets(self)
#         self.setCentralWidget(self.OpenRoomWidgets)
#         self.resize(600, 600)
#         self.setStyleSheet("background-color: rgb(19,19,19);")
#         self.createLayout()
    
#     #function to center the app to open in the middle of the page
#     def centre(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
    
#     def createLayout(self):

#         #create a label to hold the title
#         self.setWindowTitle("Chat Room")
#         self.centre()
#         self.show()
        
# class OpenRoomWidgets(QWidget):
    
#     def __init__(self, parent):
#         super(OpenRoomWidgets, self).__init__(parent)
#         #Create label for welcome message
#         welcomeMessage = QLabel('Chat Room', self)
#         welcomeMessage.setStyleSheet("QLabel {font: 10pt; color: rgb(255, 255, 255);}")
#         welcomeMessage.setAlignment(Qt.AlignHCenter)
        
#         #create buttons for the main window
#         sendMessage = QPushButton("Send")
#         sendMessage.setStyleSheet("QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")

#         #initialising horizontal box layout
#         hBox = QHBoxLayout()
#         hBox.addStretch(6)
#         hBox.addWidget(sendMessage)
#         hBox.addStretch(1)
        
#         #initialising vertical box layout
#         vBox = QVBoxLayout()
#         vBox.addStretch(6)
#         vBox.addLayout(hBox)
#         vBox.addStretch(1)
        
#         #set the layout and show all widgets
#         self.setLayout(vBox)
#         self.show()


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"))
    ex = MainPage()
    sys.exit(app.exec_())