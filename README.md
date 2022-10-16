# py-socket-programming2
Author: Phuvapit Mayrita Sribunwongsa
UPI:    psri981
This is the ReadMe file for the ChatHub App.

INSTALLATIONS TO RUN CHATHUB:

1. Conda
2. PyQt installed through Conda
3. VSCODE (or any IDE that can compile C code)
4. MinGW (or any other C compiler)

INSTRUCTIONS TO RUN CHATHUB:

First start the server:
1. Using VSCODE open the folder the project is in then create a new terminal. 
2. Run the server in the first terminal by typing: python chatServer.py --name=server --port=8888 (Note: The port number can be any number you like)

Connect new client:
1. Open a new terminal and type: pything getUserDetails.py. This will start the app.
2. Enter your name, IP Address (localhost) and port numer (e.g 8888). Make sure you enter in the same port number as the one you set for the server.
Note: Repeat this for how ever many clients you would like to connect!

App Usage: 
4. A new window will open and ask if you would like to start a group chat, chat one on one or join a group chat. Click on the option you would prefer.
5. Once you press any of the options a list of clients that are currently connected to the server will show. Select the client/clients you would like to chat with.

CURRENT VERSION:

Chat Hub currently can only display online clients and only the 1:1 chat room can be used. The messaging thread currently sends the whole socket information rather than the message appended when typing into the message box. Group chat has not yet sucessfully been implemented.




