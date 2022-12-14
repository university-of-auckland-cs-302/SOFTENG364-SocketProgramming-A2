from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chatServer import *
from utils import *
from chatClient import *


class RetrieveMsgThread(QThread):
    newMsg = pyqtSignal()

    def __init__(self, client):
        super().__init__()
        self.client = client
        self.runThread = True
        self.msg = []

    def getMsg(self):
        print(self.msg)
        return self.msg

    def run(self):
        while self.runThread:
            tempMsg = self.client.receiveMsg()
            if tempMsg != self.msg:
                self.msg = tempMsg
                print(self.msg)
                self.newMsg.emit()
            self.sleep(1)

    def stop(self):
        self.runThread = False
