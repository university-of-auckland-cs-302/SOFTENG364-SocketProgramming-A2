import socket
import pickle
import struct

## semds clients to server
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)


## receives clients from server
def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error as e:
        return ""
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size - len(buf))
    return pickle.loads(buf)[0]


# create a function that returns all clients and sends it to the server
def get_clients(clients, channel):
    send(channel, clients)


# create a function that returns all client names and sends it to the server
def get_client_names(client_names, channel):
    names = []
    for clientItems, (address, name) in map.items():
        names.append(name)
    send(channel, client_names)
