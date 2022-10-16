import select
import socket
import sys
import signal
import argparse

from utils import *

SERVER_HOST = "localhost"


class ChatServer(object):
    """An example chat server using select"""

    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.cList = []
        self.groupChats = {}
        self.grounpChatNames = {}
        self.outputs = []  # list output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        self.server.listen(backlog)
        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

        print(f"Server listening to port: {port} ...")

    def sighandler(self, signum, frame):
        """Clean up client outputs"""
        print("Shutting down server...")

        # Close existing client sockets
        for output in self.outputs:
            output.close()

        self.server.close()

    def get_client_name(self, client):
        """Return the name of the client"""
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return "@".join((name, host))

    # create function that sends list of connected clients to client
    def sendOnlineClients(self):
        self.cList = []

        for key in self.clientmap:
            self.cList.append(self.clientmap[key])
        for output in self.outputs:
            send(output, self.cList)

    def run(self):
        # inputs = [self.server, sys.stdin]
        inputs = [self.server]
        self.outputs = []
        running = True
        while running:
            try:
                readable, writeable, exceptional = select.select(
                    inputs, self.outputs, []
                )
            except select.error as e:
                break

            for sock in readable:
                sys.stdout.flush()
                if sock == self.server:
                    # handle the server socket
                    client, address = self.server.accept()

                    # Read the login name
                    cname = receive(client).split("NAME: ")[1]

                    # print client name and join message
                    print(cname + " has joined the server from " + str(address))

                    # Compute client name and send back
                    self.clients += 1
                    send(client, f"CLIENT: {str(address[0])}")
                    inputs.append(client)

                    self.clientmap[client] = (address, cname)
                    self.outputs.append(client)

                # elif sock == sys.stdin:
                #     # didn't test sys.stdin on windows system
                #     # handle standard input
                #     cmd = sys.stdin.readline().strip()
                #     if cmd == 'list':
                #         print(self.clientmap.values())
                #     elif cmd == 'quit':
                #         running = False
                else:
                    # handle all other sockets
                    try:
                        data = receive(sock)
                        if data:
                            # Send as new client's message...

                            if data == "getOnlineClients":
                                self.sendOnlineClients()

                            if data == "getGroupChats":
                                self.sendOnlineClients()

                        else:
                            print(f"Chat server: {sock.fileno()} hung up")
                            self.clients -= 1
                            sock.close()  # disconnect client from server
                            # remove disconnected client from client list
                            inputs.remove(sock)
                            self.outputs.remove(sock)
                            # self.cList.remove(sock)
                            self.clientmap.pop(sock)
                            # remove client from allClients dictionary

                            # remove client from allClients list
                            # send updated list to all clients
                            self.sendOnlineClients()
                    except socket.error as e:
                        # Remove
                        inputs.remove(sock)
                        self.outputs.remove
                        self.clientmap.pop(sock)(sock)
                        self.sendOnlineClients()

        self.server.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Socket Server Example with Select")
    parser.add_argument("--name", action="store", dest="name", required=True)
    parser.add_argument("--port", action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    name = given_args.name

    server = ChatServer(port)
    server.run()
