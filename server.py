import socket
import threading

# Setup server

hostname = socket.gethostname()
server_ip = socket.gethostbyname(hostname)
server_port = 9900
data_payload = 2048
backlog = 1
def handle_client(client_socket, addr):
    while True:
        data = client_socket.recv(data_payload).decode('utf-8')
        if not data:
            print(f"Connection closed by {addr}")
            break
        print(f"Msg from client {addr}: {data}")
        # Echo message back to client
        send_message(client_socket)

def send_message(client_socket):
        message = input("Server: ")
        client_socket.send(message.encode('utf-8'))



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((server_ip, server_port))
server.listen(backlog)

print("Server listening on port", server_port)
print("Server listening on ip", server_ip)

# Accept incoming connections
while True:
    client_socket, addr = server.accept()
    print(f"Koneksi berhasil dari {addr}")
    # Handle client in a separate thread
    client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_handler.start()
