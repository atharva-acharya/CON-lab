import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
print("Server is ready to receive")

while True:
    data, client_address = server_socket.recvfrom(4096)
    uppercase_data = data.decode().upper().encode()    
    server_socket.sendto(uppercase_data, client_address)
