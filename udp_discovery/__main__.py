import sys

import udp_discovery.discover as discover
import udp_discovery.broadcast as broadcast
import udp_discovery.serve as serve

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3:
        print("Usage: python -m udp_discovery discover port_number service_name")
        print("Usage: python -m udp_discovery broadcast port_number service_name")
    else:
        action, port, service_name = args[:3]
        port = int(port)

        timeout = 80
        if len(args) == 4:
            timeout = int(args[3])

        if action == "discover" or action == "discover_fast":
            service_ip_addr = None

            if action == "discover":
                service_ip_addr = discover.discover(port, service_name, timeout)
            else:
                service_ip_addr = discover.discover_fast(port, service_name, timeout)
            
            if service_ip_addr is None:
                print("Service not found")
            else:
                print("Service IP: {0:s}".format(service_ip_addr))

        elif action == "broadcast":
            broadcast.send_broadcast(port, service_name)

        elif action == "serve":
            serve.serve(port, service_name, timeout)
