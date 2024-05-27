import socket
import argparse

host = '10.252.132.146'


def echo_client(port):
    """A Simple echo client"""
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the socket to the server
    server_address = (host, port)
    print("connecting to %s port %s" % server_address)
    sock.connect(server_address)
    # Send data
    # try:
    # Senda data
    message = "Test message. This will be echoed"
    print("Sending %s" % message)
    sock.sendall(message.encode('utf-8'))
    amount_received = 0
    amount_excepted = len(message)
    while amount_received < amount_excepted:
        data = sock.recv(16)
        amount_received += len(data)
        print("Received: %s" % data)
    # except socket.error as e:
    #     print("Socket error: %s" % str(e))
    # except Exception as e:
    #     print("Other exception: %s" % str(e))
    # finally:
    #     print("closing connection to the server")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action='store',
                        dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
