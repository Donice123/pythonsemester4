import argparse
import socket
import psutil
import nmap

SAMPLE_PORTS = '21-23'


def get_interface_status(ifname):
    # Get the IP address associated with the interface
    addresses = psutil.net_if_addrs()
    if ifname in addresses:
        for addr in addresses[ifname]:
            if addr.family == socket.AF_INET:
                ip_address = addr.address
                break
        else:
            return "IP address not found"
    else:
        return "Interface not found"

    # Scan the IP address for the specified ports
    nm = nmap.PortScanner()
    nm.scan(ip_address, SAMPLE_PORTS)

    # Ensure that the scan was successful and the IP address was found
    if ip_address in nm.all_hosts():
        return nm[ip_address].state()
    else:
        return "unknown"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python networking utils')
    parser.add_argument('--ifname', action="store",
                        dest="ifname", required=True)
    given_args = parser.parse_args()
    ifname = given_args.ifname
    print("Interface [%s] is: %s" % (ifname, get_interface_status(ifname)))
