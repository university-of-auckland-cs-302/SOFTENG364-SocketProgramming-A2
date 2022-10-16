## Main page GUI for Chat Hub
from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from chatClient import *
from onlineUsers import *
from retrieveClientsThread import *
from createGroupChat import *

# create a class for the main window widgets
class MainPage(QWidget):
    def __init__(self, client, previousPage):
        super().__init__()
        self.retrieveClientsThread = RetrieveClientsThread(client)
        self.layoutUI(client, previousPage)
        self.centre()

    def layoutUI(self, client, previousPage):

        self.client = client
        self.connectedFrom = previousPage

        self.setWindowTitle("Hi! Beep Boop!")
        self.setWindowIcon(
            QIcon(
                "C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"
            )
        )
        self.resize(600, 600)
        # Create label for welcome message
        self.welcomeMessage = QLabel(
            "\\( .  '   ⌣   '  . )/\n\nWelcome to Chat Hub "
            + self.client.name
            + "\nwould you like to...",
            self,
        )
        self.welcomeMessage.setAlignment(Qt.AlignHCenter)

        # create buttons for the main window
        self.startChat = QPushButton("Chat 1:1")
        self.startChat.clicked.connect(self.startChatClicked)

        self.createChatRoom = QPushButton("Create Group Chat")
        self.createChatRoom.clicked.connect(self.createGroupClicked)

        self.joinChatRoom = QPushButton("Join Group Chat")
        # joinChatRoom.clicked.connect(self.JoinChatClicked);
        # self.joinRoom = JoinRoom(self)

        # initialising horizontal box layout
        hBox = QHBoxLayout()
        hBox.addStretch(1)
        hBox.addWidget(self.createChatRoom)
        hBox.addWidget(self.startChat)
        hBox.addWidget(self.joinChatRoom)
        hBox.addStretch(1)

        # initialising vertical box layout
        vBox = QVBoxLayout()
        vBox.addStretch(5)
        vBox.addWidget(self.welcomeMessage)
        vBox.addStretch(1)
        vBox.addLayout(hBox)
        vBox.addStretch(5)

        # set the layout and show all widgets
        self.customise()
        self.setLayout(vBox)
        self.show()

    # set style sheet for the main page
    def customise(self):
        self.setStyleSheet("background-color: rgb(19,19,19);")
        self.welcomeMessage.setStyleSheet(
            "QLabel {font: 24pt; color: rgb(255, 255, 255);}"
        )
        self.startChat.setStyleSheet(
            "QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )
        self.createChatRoom.setStyleSheet(
            "QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )
        self.joinChatRoom.setStyleSheet(
            "QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 10px;}"
        )

    # function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # exit application

    def closeEvent(self, event):
        self.client.cleanup()
        self.retrieveClientsThread.stop()
        event.accept()

    def startChatClicked(self):
        # get all clients connected to server
        client = self.client
        # allClients = ChatClient.getOnlineClients(self)
        self.startChat = OnlineUsers(client, self.retrieveClientsThread, self)
        self.startChat.show()
        self.hide()

    def createGroupClicked(self):
        # self.createGroup = CreateGroup()
        client = self.client
        # allClients = ChatClient.getOnlineClients(self)
        self.createChatRoom = createGroupChat(client, self.retrieveClientsThread, self)
        self.createChatRoom.show()
        self.hide()

    def JoinChatClicked(self):
        self.joinRoom.show()
        self.hide()
