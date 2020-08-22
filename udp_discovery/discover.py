import os
import socket
import time

from udp_discovery.broadcast import send_broadcast

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
            pass

        except Exception as exception:
            pass

    return None

def discover_fast(port, service_name, timeout=80):
    send_broadcast(port + 1, service_name)
    return discover(port, service_name, timeout)
