import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12345)

message = input("Enter a sentence in lowercase: ").encode()
client_socket.sendto(message, server_address)
data, server = client_socket.recvfrom(4096)
print("Received from server:", data.decode())
