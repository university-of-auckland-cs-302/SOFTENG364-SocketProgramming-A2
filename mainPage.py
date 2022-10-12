## Main page GUI for Chat Hub
from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chat_server import *
from chat_client import* 
from onlineUsers import*

#create a class for the main window widgets
class MainPage(QWidget):
    
    def __init__(self, client, previousPage):
        super().__init__()
        self.layoutUI(client, previousPage)
    
    def layoutUI(self, client, previousPage):   
        
        self.client = client
        self.connected = previousPage
        
        self.setWindowTitle("Hi! Beep Boop!")
        self.setWindowIcon(QIcon("C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"))
        self.resize(600, 600)
        self.centre
        self.setStyleSheet("background-color: rgb(19,19,19);")
        #Create label for welcome message
        welcomeMessage = QLabel("\\( .  '   ⌣   '  . )/\n\nWelcome to Chat Hub " + self.client.name + "\nwould you like to...", self)
        welcomeMessage.setStyleSheet("QLabel {font: 24pt; color: rgb(255, 255, 255);}")
        welcomeMessage.setAlignment(Qt.AlignHCenter)
        
        #create buttons for the main window
        startChat = QPushButton("Chat 1:1")
        startChat.setStyleSheet("QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        startChat.clicked.connect(self.createChatClicked);
        
        createChatRoom = QPushButton("Create Group Chat")
        createChatRoom.setStyleSheet("QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        # createChatRoom.clicked.connect(self.createGroupClicked);
        
        joinChatRoom = QPushButton("Join Group Chat")
        joinChatRoom.setStyleSheet("QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}")
        # joinChatRoom.clicked.connect(self.JoinChatClicked);
        # self.joinRoom = JoinRoom(self)
        
        #initialising horizontal box layout
        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(createChatRoom)
        hBox.addWidget(startChat)
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
    
    #function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def createChatClicked(self):
        #get all clients connected to server
        allClients = ChatClient.getOnlineClients(self)
        self.startChat = dispOnlineUsers(self.client,allClients,self)
        self.startChat.show()
        self.close()
    
    def createGroupClicked(self):
        # self.createGroup = CreateGroup()
        self.createGroup.show()
        self.close()
        
    def JoinChatClicked(self):
        self.joinRoom.show()
        self.close()
