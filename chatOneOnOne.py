## creatChatRoom GUI for 1:1 Chat Hub
from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from utils import *
from chatClient import* 
from messagingThread import *

#Create a class for the create chat room window widgets
class chatOneOnOne(QWidget):
    
    def __init__(self, client, chattingWith, previousPage):
        
        super().__init__()
        self.layoutUI(client, chattingWith, previousPage)
        self.centre()
    
    def layoutUI(self, client, chattingWith, previousPage):  
        
        self.client = client
        self.chattingWith = chattingWith
        self.connected = previousPage 

        self.setWindowTitle('Chatting with ' + chattingWith[1] + '! Beep Boop ~')
        # self.setWindowTitle('You are in ' + self.client + '\'s chat room! Beep Boop ~')
        self.setWindowIcon(QIcon("C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"))
        self.resize(600, 600)
        
        #display name of person you are chatting with above chat box
        self.chattingWith = QLabel(self.chattingWith[1],self)
        
        #create message box to send messages
        self.messageBox = QLineEdit()
        #append the message to the chat box when enter is pressed
        self.messageBox.returnPressed.connect(self.append_message)
        self.messageThread = RetrieveMsgThread(client)
        self.messageThread.start()
        self.messageThread.newMsg.connect(self.updateChat)
        
        #create chat box to display messages
        self.chatWindow = QTextEdit()
        self.chatWindow.setAcceptRichText(True)
        self.chatWindow.setReadOnly(True)
        # self.chatWindow.setOpenExternalLinks(True)
        #change size of chat box
        self.chatWindow.resize(600,600)
        
        grid = QGridLayout()
        grid.addWidget(self.chattingWith,0,0)
        grid.addWidget(self.chatWindow,1,0)
        grid.addWidget(self.messageBox,2,0)
        self.setLayout(grid)
        self.customise()
        self.show()
    
    def customise(self):
        self.setStyleSheet("background-color: rgb(19,19,19);")
        self.chattingWith.setStyleSheet("QLabel {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}")
        self.messageBox.setStyleSheet("QLineEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 20px;}")
        self.chatWindow.setStyleSheet("QTextEdit {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}")
    
    def updateChat(self): 
        print("Updating Chat")
        self.msg = self.messageThread.getMsg()
        print(self.msg)
        while len(self.msg) == 0:
            self.msg = self.messageThread.getMsg()
        self.messageBox.clear()
    
    #function to append the message to the chat window
    def append_message(self):
        #get text from message box and append to chat window
        self.message = self.messageBox.text()
        self.updateChat()
        self.messageBox.clear()
        self.chatWindow.append(self.client.name + ": " + self.message)
        print("Sending client information")
        self.client.sendMsg(self.message)
        
    #function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        