import socket
import argparse

host = 'localhost'
data_payload = 2048


def echo_server(port):
    """A simple echo server"""
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to the port
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)

    while True:
        print("Waiting to receive message from client")
        data, address = sock.recvfrom(data_payload)
        print("Received %s bytes from %s" % (len(data), address))
        print("Received response from client: %s" %
              data.decode('utf-8'))  # Decode bytes to string
        if data:
            while True:

                message = input(
                    "Enter message to send back to client (type 'exit' to stop): ")
                if message.lower() == 'exit':
                    break
                # Encode string to bytes before sending
                sock.sendto(message.encode('utf-8'), address)
                # Receive response from client
                data, address = sock.recvfrom(data_payload)
                response, client_address = sock.recvfrom(data_payload)
                print("Received response from client: %s" %
                      response.decode('utf-8'))  # Decode bytes to string
                print("Received %s bytes from %s" % (len(data), address))

    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store",
                        dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)
