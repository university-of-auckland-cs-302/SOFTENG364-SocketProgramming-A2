from threading import Thread
from time import sleep 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from chat_server import *
from utils import *
from chat_client import* 
from requests import Session

name = '' # Enter your name here!
chat_url = 'https://build-system.fman.io/chat'
server = Session()

# GUI:
app = QApplication([])
text_area = QTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)
window = QWidget()
window.setLayout(layout)
window.show()

new_messages = []
def fetch_new_messages():
    while True:
        response = server.get(chat_url).text
        if response:
            new_messages.append(response)
        sleep(.5)

thread = Thread(target=fetch_new_messages, daemon=True)
thread.start()

def display_new_messages():
    while new_messages:
        text_area.append(new_messages.pop(0))

# Signals:
message.returnPressed.connect(send_message)
timer = QTimer()
timer.timeout.connect(display_new_messages)
timer.start(1000)

app.exec()