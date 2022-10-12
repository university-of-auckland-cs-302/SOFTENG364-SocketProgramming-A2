## display clients connected to the server for Chat Hub
from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chat_server import *
from utils import *
from chat_client import* 
from datetime import datetime

#Create a class for the create chat room window widgets
class dispOnlineUsers(QWidget):
    
    def __init__(self, client, allClients, previousPage):
        super().__init__()
        self.layoutUI(client, allClients, previousPage)
        self.displayUsers()
        self.centre()
    
    def layoutUI(self, client, allClients, previousPage):  
        
        self.client = client
        self.connected = previousPage
        self.allClients = allClients
    
        self.setWindowTitle('Hi ' + self.client + '! These are the users currently online! Beep Boop ~')
        self.setWindowIcon(QIcon("C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"))
        self.resize(600, 600)
        self.setStyleSheet("background-color: rgb(19,19,19);")
        
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
        
        self.show()
    
    #display the users currently online
    def displayUsers(self):
        self.chatWindow.append("Users currently online: ")
        for key, value in self.allClients.items():
            self.chatWindow.append(value)
        self.chatWindow.append("")
        
    #function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())