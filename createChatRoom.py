## creatChatRoom GUI for Chat Hub
from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chat_server import *
from utils import *
from chat_client import* 
from datetime import datetime

#Create a class for the create chat room window widgets
class CreateRoom(QWidget):
    
    def __init__(self, client, chattingWith, previousPage):
        super().__init__()
        self.layoutUI(client, chattingWith, previousPage)
        self.centre()
    
    def layoutUI(self, client, chattingWith, previousPage):  
        
        self.client = client
        self.chattingWith = chattingWith
        self.connected = previousPage 

        self.setWindowTitle('Chatting with ' + chattingWith.name + '! Beep Boop ~')
        # self.setWindowTitle('You are in ' + self.client + '\'s chat room! Beep Boop ~')
        self.setWindowIcon(QIcon("C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"))
        self.resize(600, 600)
        self.setStyleSheet("background-color: rgb(19,19,19);")
        
        #display name of person you are chatting with above chat box
        self.chattingWith = QLabel(self.chattingWith.name,self)
        self.chattingWith.setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}")
        
        #create message box to send messages
        self.messageBox = QLineEdit()
        #append the message to the chat box when enter is pressed
        self.messageBox.returnPressed.connect(self.append_message)
        self.messageBox.setStyleSheet("QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 20px;}")
        
        #create chat box to display messages
        self.chatWindow = QTextEdit()
        self.chatWindow.setAcceptRichText(True)
        self.chatWindow.setReadOnly(True)
        # self.chatWindow.setOpenExternalLinks(True)
        self.chatWindow.setStyleSheet("QTextEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}")
        #change size of chat box
        self.chatWindow.setFixedHeight(500)
        
        grid = QGridLayout()
        self.setLayout(grid)
        
        grid.addWidget(self.chatWindow,0,0)
        grid.addWidget(self.messageBox,1,0)
        
        self.show()
    
    #function to append the message to the chat window
    def append_message(self):
        #get text from message box and append to chat window
        message = self.messageBox.text()
        self.chatWindow.append(self.client.name + ": " + message)
        self.messageBox.clear()
        
    #function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        