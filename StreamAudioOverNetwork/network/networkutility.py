import socket


def getLocalIP():
    return socket.gethostbyname(socket.gethostname())
