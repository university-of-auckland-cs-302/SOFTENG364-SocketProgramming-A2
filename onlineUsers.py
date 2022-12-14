## display clients connected to the server for Chat Hub
from ast import literal_eval
from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from utils import *
from chatClient import *
from chatOneOnOne import *

# Create a class for the create chat room window widgets
class OnlineUsers(QWidget):
    def __init__(self, client, thread, previousPage):
        super().__init__()
        self.retrieveClientsThread = thread
        self.retrieveClientsThread.start()
        self.retrieveClientsThread.newClients.connect(self.updateClientList)
        self.cList = self.retrieveClientsThread.getClients()
        while len(self.cList) == 0:
            self.cList = self.retrieveClientsThread.getClients()
        self.layoutUI(client, previousPage)
        self.centre()

    def updateClientList(self):
        self.cList = self.retrieveClientsThread.getClients()
        self.onlineUsers.clear()
        self.addOnlineClientsToList(self.cList)

    def layoutUI(self, client, previousPage):

        self.client = client
        self.connectedFrom = previousPage

        self.setWindowTitle(
            "Hi "
            + self.client.name
            + "! These are the users currently online! Beep Boop ~"
        )
        self.setWindowIcon(
            QIcon(
                "C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"
            )
        )

        # create list to display messages
        self.onlineUsers = QListWidget()
        self.onlineUsers.itemClicked.connect(self.nameClicked)
        # change size of chat box
        self.resize(600, 600)

        self.chatWith = QPushButton("Start Chat")
        self.chatWith.clicked.connect(self.startChatClicked)

        vBox = QVBoxLayout()
        vBox.addWidget(self.onlineUsers)
        vBox.addWidget(self.chatWith)

        self.setLayout(vBox)
        self.customise()
        self.show()

    def startChatClicked(self):
        self.createChatRoom = chatOneOnOne(self.client, self.chattingWith, self)
        self.createChatRoom.show()
        self.hide()

    def addOnlineClientsToList(self, allClients):
        cList = allClients
        for c in cList:
            self.onlineUsers.addItem(c[1])

    # function to customise the app
    def nameClicked(self, item):
        self.chattingWith = item.text()
        # get the socket associated with the name
        for c in self.cList:
            if c[1] == self.chattingWith:
                self.chattingWith = c

    def customise(self):
        self.setStyleSheet("background-color: rgb(19,19,19);")
        self.onlineUsers.setStyleSheet(
            "QListWidget {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}"
        )
        self.chatWith.setStyleSheet(
            "QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(51,51,51); padding: 20px;}"
        )

    def closeEvent(self, event):
        self.client.cleanup()
        self.retrieveClientsThread.stop()
        event.accept()

    # function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
