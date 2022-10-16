from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from utils import *
from chatClient import *


class RetrieveClientsThread(QThread):
    newClients = pyqtSignal()

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.runThread = True
        self.cList = []

    def getClients(self):
        return self.cList

    def run(self):
        while self.runThread:
            tempList = self.client.getOnlineClients()
            if tempList != self.cList:
                self.cList = tempList
                self.newClients.emit()
            self.sleep(1)

    def stop(self):
        self.runThread = False
