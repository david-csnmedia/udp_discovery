import time

from udp_discovery.discover import discover
from udp_discovery.broadcast import send_broadcast

def serve(port, service_name, timeout):
    start_time = time.time()
    end_time = start_time + timeout

    while end_time > time.time():
        if not discover(port + 1, service_name, 1) is None:
            time.sleep(0.15)
            send_broadcast(port, service_name)
            
            time.sleep(0.15)
            send_broadcast(port, service_name)
