import os
import socket

def send_broadcast(port, service_name):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    if not os.name == 'nt':
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.sendto(bytes(service_name, "utf8"), ('<broadcast>', port))
