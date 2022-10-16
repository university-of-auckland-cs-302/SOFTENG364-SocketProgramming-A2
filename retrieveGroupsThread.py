from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from utils import *
from chatClient import *


class RetrieveGroupsThread(QThread):
    newGroups = pyqtSignal()

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.runThread = True
        self.gList = []

    def getClients(self):
        return self.cList

    def run(self):
        while self.runThread:
            tempList = self.client.getGroupChats()
            if tempList != self.gList:
                self.gList = tempList
                self.newGroups.emit()
            self.sleep(1)

    def stop(self):
        self.runThread = False
