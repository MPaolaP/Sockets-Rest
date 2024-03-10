import socket

# Configura el socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))  # Host y puerto
server_socket.listen()

print("Servidor esperando conexiones...")
connection, address = server_socket.accept()
with connection:
    print(f"Conectado a {address}")
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f"Recibido del cliente: {data.decode('utf-8')}")
        connection.sendall(data)  # Eco del mensaje