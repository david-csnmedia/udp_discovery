import os
import socket
import time

def discover(port, service_name, timeout=80):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    if not os.name == 'nt':
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", port))
    client.settimeout(timeout)

    end_time = time.time() + timeout
    
    while end_time > time.time():
        try:
            packet = client.recvfrom(1024)
            if packet:
                data, addr = packet

                if data == bytes(service_name, "utf8"):
                    return addr[0]

        except RuntimeError as runtime_error:
            print(runtime_error)

        except Exception as exception:
            print(exception)

    return None
