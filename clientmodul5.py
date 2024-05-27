import socket

host = 'localhost'
data_payload = 2048


def echo_client(port):
    """A simple echo client"""
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)

    try:
        while True:
            # Get message from user
            message = input("Enter message to send (or type 'exit' to quit): ")
            if message.lower() == 'exit':
                break

            # Send Data
            sent = sock.sendto(message.encode('utf-8'), server_address)

            # Receive Data
            data, server = sock.recvfrom(data_payload)
            print("received %s" % data.decode('utf-8'))

    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    echo_client(12345)  # Change the port number as needed
