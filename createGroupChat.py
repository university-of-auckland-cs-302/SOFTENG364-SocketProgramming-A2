## display clients connected to the server for Chat Hub
from ast import literal_eval
from multiprocessing.connection import wait
from multiprocessing.sharedctypes import Value
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from utils import *
from retrieveGroupsThread import *
from chatClient import *
from chatOneOnOne import *

# Create a class for the create chat room window widgets
class createGroupChat(QWidget):
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
            + "Who would you like to invite to your group chat? Beep Boop ~"
        )
        self.setWindowIcon(
            QIcon(
                "C:\\Users\\maysr\\Documents\\GitHub\\SOFTENG364-SocketProgramming-A2\\images\\robo.png"
            )
        )

        # labels
        self.onlineClients = QLabel("Online Clients")
        self.invited = QLabel("Online Clients")

        # create list to display messages
        self.onlineUsers = QListWidget()
        self.onlineUsers.itemClicked.connect(self.nameClicked)
        # change size of chat box
        self.resize(600, 600)

        # create list to display messages
        self.dispInvs = QListWidget()
        self.onlineUsers.itemClicked.connect(self.invClicked)
        # change size of chat box
        self.resize(600, 600)

        self.sendInv = QPushButton("Start Chat")
        self.sendInv.clicked.connect(self.startChatClicked)

        hBox1 = QHBoxLayout()
        hBox1.addWidget(self.onlineClients)
        hBox1.addWidget(self.invited)

        hBox2 = QHBoxLayout()
        hBox2.addWidget(self.onlineUsers)
        hBox2.addWidget(self.dispInvs)

        vBox = QVBoxLayout()
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        vBox.addWidget(self.sendInv)

        self.setLayout(vBox)
        self.customise()
        self.show()

    def startChatClicked(self):
        # show dialog box to confirm inv was sent
        self.createChatRoom = chatOneOnOne(self.client, self.sendInv, self)
        self.createChatRoom.show()
        self.hide()

    def addOnlineClientsToList(self, allClients):
        cList = allClients
        for c in cList:
            self.onlineUsers.addItem(c[1])

    # function to add someone to group chat
    def nameClicked(self, item):
        self.sendInv = item.text()
        # remove from online list
        self.onlineUsers.takeItem(self.onlineUsers.row(item))
        self.dispInvs.addItem(item.text())
        # get the socket associated with the name
        for c in self.cList:
            if c[1] == self.sendInv:
                self.sendInv = c

    def customise(self):
        self.setStyleSheet("background-color: rgb(19,19,19);")
        self.onlineClients.setStyleSheet(
            "QLabel {font: 12pt; color: rgb(255,255,255)};"
        )
        self.invited.setStyleSheet("QLabel {font: 12pt; color: rgb(255,255,255)};")
        self.onlineUsers.setStyleSheet(
            "QListWidget {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}"
        )
        self.dispInvs.setStyleSheet(
            "QListWidget {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}"
        )
        self.sendInv.setStyleSheet(
            "QPushButton {font: 12pt; color: rgb(255, 255, 255); background-color: rgb(19,19,19); padding: 20px;}"
        )

    def closeEvent(self, event):
        self.client.cleanup()
        self.retrieveGroupsThread.stop()
        event.accept()

    # function to center the app to open in the middle of the page
    def centre(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
