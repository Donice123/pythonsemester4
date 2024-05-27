import socket

# Input IP server dan port
server_ip = input("Masukkan IP Server: ")
server_port = int(input("Masukkan port server: "))

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))
print("Koneksi berhasil")

# Send messages
while True:
    message = input("Client: ")
    client.send(message.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print("Msg dari server:", response)
